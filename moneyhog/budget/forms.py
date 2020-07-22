
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm # Login form
from django.contrib.auth.forms import UserCreationForm

# Import model classes
from django.contrib.auth.models import User
from .models import Expense
from .models import Category
from .models import RecurringExpense

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control', 
        'id': 'username',
        'aria-describedby': 'username',
        'placeholder': 'Username', 
        'required': 'true'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password1',
            'aria-describedby': 'password',
            'placeholder': 'Password',
            'required': 'true'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={
        'class': 'form-control',
        'id': 'password2',
        'aria-describedby': 'password',
        'placeholder': 'Password Confirmation',
        'required': 'true'
    }))
    email = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'id': 'email',
        'aria-describedby': 'email',
        'placeholder': 'Email Address',
    }),required=False)

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

class SearchExpensesForm(forms.Form):

    def __init__(self,*args,user,**kwargs):
        self.user = user
        super().__init__(*args,**kwargs)
        self.fields['categories'].choices = [(category.name,category.name) for category in Category.objects.filter(user__exact=self.user)]

    keywords = forms.CharField(required = False,widget=forms.TextInput(attrs={   
                                                                    'id': 'keywords',
                                                                    'type': 'text',
                                                                    'class': 'form-control',
                                                                    'aria-describedby': 'searchKeywords',  
                                                                        }))

    DATE_CHOICES = [('All', 'All'),
               ('single-date', 'Single'),
               ('date-range', 'Range')]
    date_choice = forms.ChoiceField(required = False,choices=DATE_CHOICES,widget=forms.RadioSelect(attrs={  
                                                                'type': 'radio',
                                                                'class': 'form-check-input',
                                                                'aria-describedby': 'date',
                                                                    }))

    single_date = forms.DateField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'singledate',
                                                                'type': 'text',
                                                                'class': 'form-control w-75',
                                                                'aria-describedby': 'singleDate',  
                                                                    }))

    date_range = forms.CharField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'daterange',
                                                                'type': 'text',
                                                                'class': 'form-control w-75 d-none',
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
    

    categories = forms.MultipleChoiceField(
        required = False,widget=forms.CheckboxSelectMultiple(attrs={  
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
        # fields = '__all__'
        fields = ['expense_date','amount','description','category']
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
        # fields = '__all__'
        fields = ['day','amount','description','category']
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

class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ['user']
        widgets = {
                'name': forms.TextInput(attrs={
                                            'id': 'categoryName',
                                            'type': 'text',
                                            'class': 'form-control',
                                            'aria-describedby': 'categoryName',
                                            'placeholder': 'Enter a category' 
                                            })
        }

