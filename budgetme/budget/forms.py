
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm # Login form

# Import model classes
from django.contrib.auth.models import User
from .models import Expense
from .models import Category
from .models import RecurringExpense

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control', 
        'id': 'username',
        'aria-describedby': 'username',
        'placeholder': 'Username', 
        'required': 'true'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'aria-describedby': 'password',
            'placeholder': 'Password',
            'required': 'true'
        }))

class searchExpensesForm(forms.Form):
    keywords = forms.CharField(required = False,widget=forms.TextInput(attrs={   
                                                                'id': 'keywords',
                                                                'type': 'text',
                                                                'class': 'form-control',
                                                                'aria-describedby': 'searchKeywords',  
                                                                    }))

    all_dates = forms.BooleanField(required = False,widget=forms.CheckboxInput(attrs={  
                                                                'id': 'all-dates',
                                                                'type': 'checkbox',
                                                                'class': 'custom-control-input',
                                                                'aria-describedby': 'searchAllDates',  
                                                                    }))

    use_range = forms.BooleanField(required = False,widget=forms.CheckboxInput(attrs={  
                                                                'id': 'use-range',
                                                                'type': 'checkbox',
                                                                'class': 'custom-control-input',
                                                                'aria-describedby': 'useDateRange',  
                                                                    }))

    single_date = forms.DateField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'singledate',
                                                                'type': 'text',
                                                                'class': 'form-control w-50',
                                                                'aria-describedby': 'singleDate',  
                                                                    }))

    date_range = forms.CharField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'daterange',
                                                                'type': 'text',
                                                                'class': 'form-control w-50 d-none',
                                                                'aria-describedby': 'dateRange',  
                                                                    }))

    min_amount = forms.DecimalField(required = False,widget=forms.NumberInput(attrs={  
                                                                'required': False,
                                                                'id': 'min-amount',
                                                                'type': 'number',
                                                                'class': 'form-control',
                                                                'aria-describedby': 'minAmount',
                                                                'step': "1"  
                                                                    }))

    max_amount = forms.DecimalField(required = False,widget=forms.NumberInput(attrs={  
                                                                'required': False,
                                                                'id': 'max-amount',
                                                                'type': 'number',
                                                                'class': 'form-control',
                                                                'aria-describedby': 'maxAmount',
                                                                'step': "1"  
                                                                    }))
    

    CATEG_CHOICES = []
    category_list = Category.objects.all()
    for category in category_list:
        CATEG_CHOICES.append((category.name, category.name))

    categories = forms.MultipleChoiceField(
        required = False,choices=CATEG_CHOICES,widget=forms.CheckboxSelectMultiple(attrs={  
                                                                'type': 'checkbox',
                                                                'class': 'custom-control-input',
                                                                'aria-describedby': 'category',
                                                                    }))

    RECEIPT_CHOICES = [('All', 'All'),
               ('has-receipt', 'Has Receipt'),
               ('no-receipt', 'No Receipt')]
    has_receipt = forms.ChoiceField(
        required = False,choices=RECEIPT_CHOICES,widget=forms.RadioSelect(attrs={  
                                                                'type': 'radio',
                                                                'class': 'form-check-input',
                                                                'aria-describedby': 'hasReceipt',
                                                                    }))

class DeleteExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = []

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
                'expense_date': forms.TextInput(attrs={
                                                        'id': 'datepicker',
                                                        'type': 'text',
                                                        'class': 'form-control w-50',
                                                        'aria-describedby': 'dateofExpense',
                                                        'required': 'true'  
                                                        }),
                                                        
                'amount': forms.TextInput(attrs={
                                                'type': 'number',
                                                'class': 'form-control w-50',
                                                'aria-describedby': 'amount',
                                                'min': '0',
                                                'step': '0.01',
                                                'required': 'true'
                                                }),
                'vendor': forms.TextInput(attrs={
                                                'type': 'text',
                                                'class': 'form-control w-50',
                                                'aria-describedby': 'vendor'
                                                }),
                'description': forms.TextInput(attrs={
                                                        'type': 'text',
                                                        'class': 'form-control',
                                                        'aria-describedby': 'description'

                                                        }),
                'category': forms.Select(attrs={'class': 'form-control w-50 mr-2',
                                                'value': 'Select One'
                                                        })
        
        }

class RecurringExpenseForm(ModelForm):
    class Meta:
        model = RecurringExpense
        fields = '__all__'
        widgets = {
                'day': forms.NumberInput(attrs={
                                                'type': 'number',
                                                'class': 'form-control w-50 mr-2',
                                                'aria-describedby': 'dayOfMonth' 
                                                }),
                'amount': forms.TextInput(attrs={
                                                'type': 'number',
                                                'class': 'form-control w-50',
                                                'aria-describedby': 'amount',
                                                'min': '0',
                                                'step': '0.01',
                                                'required': 'true'
                                                }),
                'vendor': forms.TextInput(attrs={
                                                'type': 'text',
                                                'class': 'form-control w-50',
                                                'aria-describedby': 'vendor'
                                                }),
                'description': forms.TextInput(attrs={
                                                        'type': 'text',
                                                        'class': 'form-control',
                                                        'aria-describedby': 'description'

                                                        }),
                'category': forms.Select(attrs={'class': 'form-control w-50 mr-2',
                                                'value': 'Select One'
                                                        })
        
        }

class DeleteRecurringExpenseForm(ModelForm):
    class Meta:
        model = RecurringExpense
        fields = []