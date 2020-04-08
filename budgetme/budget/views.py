from django.shortcuts import get_object_or_404, render


# will remove HttpResponse once we convert all of the stubs
from django.http import Http404
from django.http import HttpResponse
from django.template import loader


from .models import Expense
from .models import Income
from .models import Category

from datetime import date
from django.contrib import messages

from .forms import ExpenseForm

# from .forms import DeleteExpenseForm
from django.shortcuts import redirect

from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

# //////////////////////////////////////////
from django.views import generic
# from .models import Expense 

# from budget.forms import ExpenseForm 
from django.views.generic.edit import FormView

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
    today = date.today()
    latest_expenses_list = Expense.objects.filter(expense_date__year=today.year, expense_date__month=today.month).order_by('-expense_date')

    monthly_total = 0
    for i in latest_expenses_list:
        monthly_total += i.amount

    month = today.strftime('%B')
    # month = today.strftime
    context = {
        'latest_expenses_list': latest_expenses_list,
        'monthly_total' : monthly_total,
        'month': month,
    }

    return render(request, 'budget/expenses/list.html', context)


# class ExpenseDetailView(generic.DetailView):
#     model = Expense
#     template_name = 'budget/expenses/detail.html'

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
        category_list = Category.objects
        

        context = {
            'category_list' : category_list,
            'form' : form,
            'expense': expense,
        }

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