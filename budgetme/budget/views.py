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

from datetime import date

from django.contrib import messages

from .forms import ExpenseForm

# from .forms import DeleteExpenseForm
from django.shortcuts import redirect

from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

# //////////////////////////////////////////
from django.views import generic

# from budget.forms import ExpenseForm 
from django.views.generic.edit import FormView

# To read images
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from django.http import JsonResponse
from .forms import TempReceiptForm

# Pagination
from django.core.paginator import Paginator

# Errors 
import logging

class IndexView(generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'latest_expenses_list'

    def get_queryset(self):
        return Expense.objects.order_by('-expense_date')[:5]

# Expense Views
# ///////////////////////////////////////

# class ExpenseUpdate(UpdateView):
#     model = Expense
#     # template_name = 'budget/expenses/new-expense.html'

# class ExpenseDelete(DeleteView):
#     model = Expense
#     success_url = reverse_lazy('author-list')
    

# Old Expense List view
# def expense_list(request):
#     latest_expenses_list = Expense.objects.order_by('-expense_date')[:5]
#     context = {
#         'latest_expenses_list': latest_expenses_list,
#     }
#     return render(request, 'budget/expenses/list.html',context)

# class ExpenseListView(generic.ListView):
#     template_name = 'budget/expenses/list.html'
#     context_object_name = 'latest_expenses_list'

#     def get_queryset(self):
#         today = date.today()
#         return Expense.objects.filter(expense_date__year=today.year,
#         expense_date__month=today.month).order_by('-expense_date')

def expense_list(request):
    # today = date.today()
    # expenses_list = Expense.objects.filter(expense_date__year=today.year, expense_date__month=today.month).order_by('-expense_date')

    expenses_list = Expense.objects.order_by('-expense_date')

    limit = 10
    paginator = Paginator(expenses_list, limit)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    # monthly_total = 0
    # for i in latest_expenses_list:
    #     monthly_total += i.amount

    # List of all categories:
    category_list = Category.objects.all()

    page_total = 0
    page_count = 0
    for i in page_obj:
        page_total += i.amount
        page_count += 1

    start_num = (int(page_number) - 1) * limit +1
    end_num = start_num + page_count - 1

    # month = today.strftime('%B')
    # month = today.strftime
    context = {
        'page_obj': page_obj,
        'page_number': page_number,
        'page_total': page_total,
        'num_records': paginator.count,
        'page_range': paginator.page_range,
        'start_num' : start_num,
        'end_num': end_num,
        'category_list': category_list,
    }

    # logger.info(page_number)

    return render(request, 'budget/expenses/list.html', context)

def expense_list_filter(request):
    if request.method == "POST":
        # for i in request.POST:
        #     print(i)
        #     print(request.POST.get(i))
        print("newline")
        keywords = request.POST.get("expense-search")
        single_date = request.POST.get("singledate")
        date_range = request.POST.get("daterange")
        print("single date is: ",single_date)
        print("date range is: ",date_range)
        print("search keywords are: ",keywords)
        # print(request.POST.get("singledate"))

        # categories:
        # {{ category }}
        # have to loop through ..how to know the id of each category?
        
        if single_date:
            print(single_date)
            # print(type(single_date))
            # print("single date")
            # 04/10/2020
            # Create list composed of the year, month, and day
            date_list = single_date.split('/')
            print("the date list is: ", date_list)

            # Get a filtered expense list based on the date
            expenses_list = Expense.objects.filter(expense_date__year=date_list[2],    expense_date__month=date_list[0],expense_date__day=date_list[1]).order_by('-expense_date')

            # for i in expenses_list:
                # print(expenses_list[i])
            if not expenses_list:
                print("no expenses?")


# YourModel.objects.filter(datetime_published__year='2008', 
#                          datetime_published__month='03', 
#                          datetime_published__day='27')

            # expenses_list = Expense.objects.filter(expense_date__year=date_list[2],    expense_date__month=date_list[1],expense_date__date=date_list[0]).order_by('-expense_date')
            #     expenses_list = Expenses.objects.filter(date__range=["2011-01-01", "2011-01-31"])
            

        elif date_range:
            print("date range")

        else:
            print("no date entered")
            expenses_list = Expense.objects.order_by('-expense_date')
            
        
    # else: 
    # print("made it this far")

    limit = 10
    paginator = Paginator(expenses_list, limit)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    # List of all categories:
    category_list = Category.objects.all()

    # monthly_total = 0
    # for i in latest_expenses_list:
    #     monthly_total += i.amount

    page_total = 0
    page_count = 0
    for i in page_obj:
        page_total += i.amount
        page_count += 1

    start_num = (int(page_number) - 1) * limit +1
    end_num = start_num + page_count - 1
    # print("made it this far 2")
    # month = today.strftime('%B')
    # month = today.strftime
    context = {
        'page_obj': page_obj,
        'page_number': page_number,
        'page_total': page_total,
        'num_records': paginator.count,
        'page_range': paginator.page_range,
        'start_num' : start_num,
        'end_num': end_num,
        'category_list': category_list,
    }

    # logger.info(page_number)

    return render(request, 'budget/expenses/list.html', context)


# View an existing expense
def expense_detail(request, pk):
    expense = Expense.objects.get(pk = pk)

    if request.method == "POST":
        expense.delete()
        return redirect('budget:expense_list')
    else:
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
            pass
        # come back here and finish error handling
    else:
        form = ExpenseForm(instance=expense)
        category_list = Category.objects.all()
        

        context = {
            'category_list' : category_list,
            'form' : form,
            'expense': expense,
        }

        # return render(request, 'budget/expenses/edit-expense.html',context)
        return render(request, 'budget/expenses/edit-expense.html',context)

# Create a new expense page
def expense_form_page(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save()
            return redirect('budget:expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm()
        category_list = Category.objects

        context = {
            'category_list' : category_list,
            'form' : form,
        }

        return render(request, 'budget/expenses/new-expense.html',context)
        # return render(request, 'budget/expenses/edit-expense.html',context)

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



# Old views


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