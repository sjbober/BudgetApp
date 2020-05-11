from django.shortcuts import get_object_or_404, render


# will remove HttpResponse once we convert all of the stubs
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

# Models
from .models import Expense
from .models import Income
from .models import Category
from .models import TempReceipt
from .models import RecurringExpense

from django.contrib import messages

# Forms to import
from .forms import ExpenseForm
from .forms import searchExpensesForm
# from .forms import ExpenseFilter
from .forms import DeleteExpenseForm
from .forms import RecurringExpenseForm
from .forms import DeleteRecurringExpenseForm

# For complex querying:
import operator
from functools import reduce
from django.db.models import Q


from django.shortcuts import redirect

from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

# //////////////////////////////////////////
from django.views import generic

# To read images
# import cloudmersive_ocr_api_client
# from cloudmersive_ocr_api_client.rest import ApiException
# from django.http import JsonResponse
# from .forms import TempReceiptForm

# Pagination
from django.core.paginator import Paginator

# Errors 
import logging

class IndexView(generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'latest_expenses_list'

    def get_queryset(self):
        return Expense.objects.order_by('-expense_date')[:5]

def expense_list(request):
    context = {}
    category_list = Category.objects.all()
    expenses_list = Expense.objects.order_by('-expense_date')
    highest_amount = Expense.objects.order_by('-amount')[0].amount
    # print(highest_amount)

    # If a search filter call has been made, we need to filter our expenses list and create a bounded form
    if 'keywords' in request.GET:
        form = searchExpensesForm(request.GET)
        if form.is_valid():
            # print("form is valid")
            keywords = form.cleaned_data["keywords"]
            all_dates = form.cleaned_data["all_dates"]
            use_range = form.cleaned_data["use_range"]  
            single_date = form.cleaned_data["single_date"]    # 04/22/2020
            date_range = form.cleaned_data["date_range"]     # 04/22/2020 - 04/22/2020
            min_amount = form.cleaned_data["min_amount"]
            max_amount = form.cleaned_data["max_amount"]
            categories = form.cleaned_data["categories"]
            has_receipt = form.cleaned_data["has_receipt"]

            context.update({'all_dates': all_dates,
                            'min_amount': min_amount,
                            'max_amount': max_amount,
                            'has_receipt': has_receipt})
            
            # Filter queryset for keywords
            if keywords:
                expenses_list = expenses_list.filter(
                    Q(expense_date__icontains=keywords) |
                    Q(amount__icontains=keywords) |
                    Q(description__icontains=keywords)
                )

            # Filter queryset for date range or single date
            if not all_dates and use_range: # if the user selected a date range
                print(type(date_range))
                # string
                # "05/03/2020 - 05/08/2020"
                print(date_range)
                # change "04/22/2020 - 04/22/2020"
                # into ["yyyy-mm-dd" - "yyyy-mm-dd"]
                fdl = date_range.split(" - ")[0].split('/')
                first_date = fdl[2] + "-" + fdl[0] + "-" + fdl[1]

                sdl = date_range.split(" - ")[1].split('/')
                second_date = sdl[2] + "-" + sdl[0] + "-" + sdl[1]

                expenses_list = expenses_list.filter(expense_date__range=[first_date, second_date])

                # expenses_list = Expense.objects.filter(date__range=["2011-01-01", "2011-01-31"])
            elif not all_dates and not use_range:
                expenses_list = expenses_list.filter(expense_date=single_date).order_by('-expense_date')

            # Filter query set for min amount
            if min_amount and min_amount != "0.00":
                expenses_list = expenses_list.filter(amount__gte=min_amount)

            # Filter query set for max amount
            if max_amount and max_amount != "1000.00":
                expenses_list = expenses_list.filter(amount__lte=max_amount)

            # Filter query set for categories
            if categories:
                list_foreignid = []

                # Get a list of category primary keys (foreign keys in expense table)
                for obj in category_list:
                    if obj.name in categories:
                        list_foreignid.append(obj.id)

                # Create a list of Q objects using the category foreign keys
                q_category_list = []
                for foreignid in list_foreignid:
                    q_category_list.append(Q(category__exact=foreignid))

                expenses_list = expenses_list.filter(reduce(operator.or_, q_category_list))

            # Filter query set based on whether it has a receipt or not
            if has_receipt == "has-receipt":
                expenses_list = expenses_list.exclude(receipt__exact='')
            elif has_receipt == "no-receipt":
                expenses_list = expenses_list.filter(receipt__exact='')

        
    else:
        form = searchExpensesForm(request.GET)
        # expenses_list = Expense.objects.order_by('-expense_date')

    limit = 10 # record limit per page
    paginator = Paginator(expenses_list, limit)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    # Get total number of expenses to be displayed on the current page
    page_total = 0
    page_count = 0
    for i in page_obj:
        page_total += i.amount
        page_count += 1

    # Get the starting and ending number of expenses for the current page
    start_num = (int(page_number) - 1) * limit +1
    end_num = start_num + page_count - 1

    context.update({
        'page_obj': page_obj,
        'page_number': page_number,
        'page_total': page_total,
        'num_records': paginator.count,
        'page_range': paginator.page_range,
        'start_num' : start_num,
        'end_num': end_num,
        'form': form,
        'highest_amount': highest_amount,
    })

    # logger.info(page_number)

    return render(request, 'budget/expenses/list.html', context)

def expense_list_recurring(request):
    recurring_expenses = RecurringExpense.objects.all()

    context = {
        'recurring_expenses': recurring_expenses,
    }

    return render(request, 'budget/expenses/recurring-list.html',context)

# View an existing expense
def expense_detail(request, pk):
    expense = Expense.objects.get(pk = pk)

    if request.method == "POST":
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            messages.success(request, "Expense #%s has been deleted." % expense.pk)
            expense.delete()
            return redirect('budget:expense_list')
        else:
            messages.error(request, "An error occurred and expense #%s was not deleted." % expense.pk)

    context = {
        'expense': expense,
    }

    return render(request, 'budget/expenses/detail.html', context)

# Edit an existing expense
def expense_edit(request, pk):
    expense = Expense.objects.get(pk = pk)

    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been saved.")
            return redirect('budget:expense_detail', pk=expense.pk)
        else:
            messages.error(request, "An error occurred and your changes have not been saved.")

    else:
        form = ExpenseForm(instance=expense)

    category_list = Category.objects.all()
    context = {
        'category_list' : category_list,
        'form' : form,
        'expense': expense,
    }

    return render(request, 'budget/expenses/edit-expense.html',context)

def recurring_edit(request, pk):
    expense = RecurringExpense.objects.get(pk = pk)

    if request.method == "POST" and 'day' in request.POST:
        recurring_form = RecurringExpenseForm(request.POST, instance=expense)
        if recurring_form.is_valid():
            recurring_form.save()
            messages.success(request, "Your changes have been saved.")
            return redirect('budget:expense_list_recurring')
        else:
            messages.error(request, "An error occurred and your changes have not been saved.")
    elif request.method == "POST":
        form = DeleteRecurringExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            messages.success(request, "A recurring expense for $%s has been successfully deleted." % expense.amount)
            expense.delete()
            return redirect('budget:expense_list_recurring')
        else:
            messages.error(request, "An error occurred and expense #%s was not deleted." % expense.pk)
    else:
        recurring_form = RecurringExpenseForm(instance=expense)

    category_list = Category.objects.all()
    context = {
        'category_list' : category_list,
        'recurring_form' : recurring_form,
        'expense': expense,
    }

    return render(request, 'budget/expenses/edit-recurring.html',context)

# Create a new expense page
def expense_form_page(request):
    if request.method == "POST" and 'expense_date' in request.POST:
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save()
            messages.success(request, "Expense #{} has been successfully created.".format(str(expense.pk)))
            return redirect('budget:expense_detail', pk=expense.pk)
        else:
            messages.error(request, "Your expense could not be submitted.")

    elif request.method == "POST" and 'day' in request.POST:
        recurring_form = RecurringExpenseForm(request.POST)
        if recurring_form.is_valid():
            recurring_expense = recurring_form.save()
            recurring_expense.save()
            messages.success(request, "A recurring expense for ${} has been successfully created.".format(str(recurring_expense.amount)))
            return redirect('budget:expense_list_recurring')
        else:
            messages.error(request, "Your expense could not be submitted.")
    else:
        form = ExpenseForm()
        recurring_form = RecurringExpenseForm()

    category_list = Category.objects.all()
    context = {
        'category_list' : category_list,
        'form' : form,
        'recurring_form': recurring_form,
    }

    return render(request, 'budget/expenses/new-expense.html',context)

# Code not working - attemt to read receipt
def read_receipt(request):
    # if request.method == "POST":
    #     response = {"test": "test"}
    #     return JsonResponse(response)
    test = {"test": "success"}
    # form = TempReceiptForm(request.POST, request.FILES)
    # if form.is_valid():
    #     img = form.save()
    #     image_file = img.image
        # return image_file
    if request.method == "POST":
        img = request.FILES.get('file')
        newTemp = TempReceipt(image = img)
        newTemp.save()
    # tempRe = TempReceipt()
    # tempRe.image = request.POST.get('file', None)
    # tempRe.image = request.FILES["file"]
    image_file = "C:/Users/sjbober/Documents/Projects/budget/budgetme" + newTemp.image.url
    path = {"path": image_file}
    return JsonResponse(path)
    # image_file = '..\/' + newTemp.image.url
    # pk = img.pk
    # api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
    # image_file = request.GET.get('file', None)
    # image_file = request.POST.get('file', None)
    # image_file = request.POST.get("file", None)
    # image_file = request.POST
    # image_name = request.FILES["file"].name
    # image_file = '../media/temp/' + image_name
        # return JsonResponse(test)
        # return JsonResponse(image_file)
    response = {"error": "File not found"}
                    # "image": image_file}
    # return image_file
    # image_file = tempRe.image
    if image_file == None:
    #     pass
        return JsonResponse(response)
    # image_file = request
    # print(image_file)
    # image_file = request
    # return JsonResponse(test)

    api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
    # return JsonResponse(test)
   ## image_file = 'C:\\temp\\input.jpg' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
    # configuration = cloudmersive_ocr_api_client.Configuration()
    api_instance.api_client.configuration.api_key = {}
    api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'
    # return JsonResponse(test)
    try:
        # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
        api_response = api_instance.image_ocr_post(image_file)
        # return JsonResponse(test)
        # return JsonResponse(api_response)
        return api_response
        # pprint(api_response)
    except ApiException as e:
        response = {"error": "Error calling the OCR API"}
        return JsonResponse(response)
        # print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)





# Income Views
# ///////////////////////////////////////


class IncomeDetailView(generic.DetailView):
    model = Income
    template_name = 'budget/income/detail.html'


def income_list(request):
    return HttpResponse("You are viewing your list of incomes")

# def income_detail(request, income_id):
#     return HttpResponse("You are viewing %s income detail page" % income_id)

def categories(request):
    return HttpResponse("You are viewing the categories page")

def category_detail(request, category_id):
    return HttpResponse("You are viewing %s category detail page" % category_id)