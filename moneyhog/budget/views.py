from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect

# For working with fetch calls
from django.http import JsonResponse
import json

# Models
from django.contrib.auth.models import User
from .models import Expense
from .models import Income
from .models import Category
from .models import RecurringExpense

# Displaying success/error/etc messages
from django.contrib import messages

# Login authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms to import
from .forms import LoginForm
from .forms import AuthenticationForm
from .forms import ExpenseForm
from .forms import SearchExpensesForm
from .forms import DeleteExpenseForm
from .forms import RecurringExpenseForm
from .forms import DeleteRecurringExpenseForm
from .forms import CreateCategoryForm
from .forms import SignupForm

# For complex querying:
import operator
from functools import reduce
from django.db.models import Q

# Pagination
from django.core.paginator import Paginator

# Errors 
# import logging

def signup(request):
    # expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        userForm = SignupForm(request.POST)
        if userForm.is_valid():
            # user = userForm.save()
            username = userForm.cleaned_data["username"]
            password = userForm.cleaned_data["password1"]
            email = userForm.cleaned_data["email"]   
            user = User.objects.create_user(username, email, password)
            messages.success(request, "Your account was successfully created, %s! Try logging in now." % user.username)
            return redirect('budget:index')
        else:
            messages.error(request, "An error occurred and your account could not be created.")
    # else:
    form = SignupForm()
    context = {
        'form': form,
    }

    return render(request, 'budget/signup.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('budget:expense_list')
        else:
            print("user does not exist")
            messages.error(request, "Your username and/or password is incorrect.")
    # else:
    #     pass
        # Return an 'invalid login' error message.

    form = LoginForm()
    context = {
        'form': form,
    }

    return render(request, 'budget/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    form = LoginForm()
    context = {
        'form': form,
    }

    return render(request, 'budget/login.html', context)


# View spending history
@login_required
def expense_list(request):
    context = {}

    expenses_list = Expense.objects.filter(user__exact=request.user.id).order_by('-expense_date')
    if expenses_list:
        highest_amount = Expense.objects.order_by('-amount')[0].amount
    else:
        highest_amount = 1000

    # If a search filter call has been made, we need to filter our expenses list and create a bounded form
    if 'keywords' in request.GET:
        form = SearchExpensesForm(request.GET)
        if form.is_valid():
            keywords = form.cleaned_data["keywords"]
            date_choice = form.cleaned_data["date_choice"] 
            single_date = form.cleaned_data["single_date"]    # 04/22/2020
            date_range = form.cleaned_data["date_range"]     # 04/22/2020 - 04/22/2020
            min_amount = form.cleaned_data["min_amount"]
            max_amount = form.cleaned_data["max_amount"]
            categories = form.cleaned_data["categories"]
            has_receipt = form.cleaned_data["has_receipt"]

            context.update({'date_choice': date_choice,
                            'min_amount': min_amount,
                            'max_amount': max_amount,
                            'has_receipt': has_receipt,
                            })
            
            # Filter queryset for keywords
            if keywords:
                expenses_list = expenses_list.filter(
                    Q(expense_date__icontains=keywords) |
                    Q(amount__icontains=keywords) |
                    Q(description__icontains=keywords)
                )

            # Filter queryset for date range or single date
            # if not all_dates and use_range: # if the user selected a date range
            if date_choice == "date-range":
                # change "mm/dd/yyyy - mm/dd/yyyy"
                # into ["yyyy-mm-dd" - "yyyy-mm-dd"]
                fdl = date_range.split(" - ")[0].split('/')
                first_date = fdl[2] + "-" + fdl[0] + "-" + fdl[1]

                sdl = date_range.split(" - ")[1].split('/')
                second_date = sdl[2] + "-" + sdl[0] + "-" + sdl[1]

                expenses_list = expenses_list.filter(expense_date__range=[first_date, second_date])

            elif date_choice == "single-date":
                expenses_list = expenses_list.filter(expense_date=single_date).order_by('-expense_date')

            # Filter query set for min amount
            if min_amount and min_amount != "0.00":
                expenses_list = expenses_list.filter(amount__gte=min_amount)

            # Filter query set for max amount
            if max_amount and max_amount != "1000.00":
                expenses_list = expenses_list.filter(amount__lte=max_amount)

            # Filter query set for categories
            if categories:
                category_list = Category.objects.filter(user__exact=request.user.id)
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
            pass
            '''Need to put something here...'''
        
    else:
        form = SearchExpensesForm(request.GET,request.user)

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

# View list of monthly bills
@login_required
def expense_list_recurring(request):
    recurring_expenses = RecurringExpense.objects.filter(user__exact=request.user.id)

    context = {
        'recurring_expenses': recurring_expenses,
    }

    return render(request, 'budget/expenses/recurring-list.html',context)

# View or delete an existing expense
@login_required
def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

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
@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

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

    category_list = Category.objects.filter(user__exact=request.user.id)
    context = {
        'category_list' : category_list,
        'form' : form,
        'expense': expense,
    }

    return render(request, 'budget/expenses/edit-expense.html',context)

# Edit a monthly bill
@login_required
def recurring_edit(request, pk):
    expense = get_object_or_404(RecurringExpense, pk=pk)

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
            messages.success(request, "A monthly bill for $%s has been successfully deleted." % expense.amount)
            expense.delete()
            return redirect('budget:expense_list_recurring')
        else:
            messages.error(request, "An error occurred and expense #%s was not deleted." % expense.pk)
    else:
        recurring_form = RecurringExpenseForm(instance=expense)

    category_list = Category.objects.filter(user__exact=request.user.id)
    context = {
        'category_list' : category_list,
        'recurring_form' : recurring_form,
        'expense': expense,
    }

    return render(request, 'budget/expenses/edit-recurring.html',context)

# Create a new expense page
@login_required
def expense_form_page(request):
    if request.method == "POST" and 'expense_date' in request.POST:
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense #{} has been successfully created.".format(str(expense.pk)))
            return redirect('budget:expense_detail', pk=expense.pk)
        else:
            messages.error(request, "Your expense could not be submitted.")

    elif request.method == "POST" and 'day' in request.POST:
        recurring_form = RecurringExpenseForm(request.POST)
        if recurring_form.is_valid():
            recurring_expense = recurring_form.save(commit=False)
            recurring_expense.user = request.user
            recurring_expense.save()
            messages.success(request, "A monthly bill for ${} has been successfully created.".format(str(recurring_expense.amount)))
            return redirect('budget:expense_list_recurring')
        else:
            messages.error(request, "Your expense could not be submitted.")
    else:
        form = ExpenseForm()
        recurring_form = RecurringExpenseForm()

    category_list = Category.objects.filter(user__exact=request.user.id)
    context = {
        'category_list' : category_list,
        'form' : form,
        'recurring_form': recurring_form,
    }

    return render(request, 'budget/expenses/new-expense.html',context)



# Category List View
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
@login_required
def category_list(request):
    category_names = [cat.name for cat in Category.objects.filter(user__exact=request.user.id)]

    if request.method == "GET":
        form = CreateCategoryForm()
        context = {
            'category_names': category_names,
            'form': form,
        }

        return render(request, 'budget/category/list.html',context)

    elif request.method == "POST": # create, edit or delete a category!
        post_data = json.loads(request.body)
        response_data = {}
        cat_name = post_data['name']

        if post_data['purpose'] == 'create': #create category
            print(post_data['tok1'], post_data['tok2'])

            if cat_name.strip() == "": # check if blank was sent
                response_data['error'] = "You can't create a blank category."
            else:
                cat_name = cat_name.strip()
                cat_name = cat_name[0].upper() + cat_name[1:].lower()

                if cat_name in category_names:
                    response_data['error'] = "This category already exists."

                else:   # category is valid
                    category = Category(name=cat_name,user=request.user)
                    category.save()
                    response_data['result'] = 'success'
                    response_data['category_name'] = category.name
                    response_data['tok1'] = post_data['tok1']
                    response_data['tok2'] = post_data['tok2']

                return JsonResponse(response_data)

        elif post_data['purpose'] == 'delete': # delete category
            category = Category.objects.filter(name__exact=cat_name)
            if category:
                category.delete()
                response_data['result'] = 'success'
            else:
                response_data['result'] = 'error'
            print('got this far')
            return JsonResponse(response_data)


# Delete a category
# @login_required
# def categ_delete_edit(request):
#     if request.method == "POST": # delete
#         print("this far")
#         post_data = json.loads(request.body)
#         cat_name = post_data['name']
#         # queryset = Category.objects.filter(name__exact=cat_name)
#         category = get_object_or_404(Category, name__exact=cat_name)

#     elif request.method == "PUT":
#         pass
