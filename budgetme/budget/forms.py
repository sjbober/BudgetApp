from django import forms

# from django.db import models
from django.forms import ModelForm

from .models import Expense
from .models import TempReceipt

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

    # <input type="checkbox" class="custom-control-input" id="use-range" name="use-range">
    use_range = forms.BooleanField(required = False,widget=forms.CheckboxInput(attrs={  
                                                                'id': 'use-range',
                                                                'type': 'checkbox',
                                                                'class': 'custom-control-input',
                                                                'aria-describedby': 'useDateRange',  
                                                                    }))
    # If not checked --> None
    # If checked --> "on"

    # <input id="singledate" type="text" name="singledate" class="form-control w-50" aria-describedby="date"/>
    single_date = forms.CharField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'singledate',
                                                                'type': 'text',
                                                                'class': 'form-control w-50',
                                                                'aria-describedby': 'singleDate',  
                                                                    }))
    #  04/22/2020
    
    # <input id="daterange" type="text" name="daterange" class="form-control w-50 d-none" aria-describedby="dateRange"/>
    date_range = forms.CharField(required = False,widget=forms.TextInput(attrs={

                                                                'id': 'daterange',
                                                                'type': 'text',
                                                                'class': 'form-control w-50 d-none',
                                                                'aria-describedby': 'dateRange',  
                                                                    }))
    # 04/22/2020 - 04/22/2020
    # <input id="min-amount" type="number" name="min-amount" class="form-control" aria-describedby="minAmount" step="1" >
    min_amount = forms.DecimalField(required = False,widget=forms.NumberInput(attrs={  
                                                                'required': False,
                                                                'id': 'min-amount',
                                                                'type': 'number',
                                                                'class': 'form-control',
                                                                'aria-describedby': 'minAmount',
                                                                'step': "1"  
                                                                    }))
    # <input id="max-amount" type="number" name="max-amount" class="form-control" aria-describedby="maxAmount" step="1">
    max_amount = forms.DecimalField(required = False,widget=forms.NumberInput(attrs={  
                                                                'required': False,
                                                                'id': 'max-amount',
                                                                'type': 'number',
                                                                'class': 'form-control',
                                                                'aria-describedby': 'maxAmount',
                                                                'step': "1"  
                                                                    }))

    # <input class="form-check-input" type="radio" name="receipt-radio" id="has-receipt" value="has-receipt">
    CHOICES = [('All', 'All'),
               ('has-receipt', 'Has Receipt'),
               ('no-receipt', 'No Receipt')]
    has_receipt = forms.ChoiceField(
        required = False,choices=CHOICES,widget=forms.RadioSelect(attrs={  
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
                                                        'type': 'date',
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
                'category': forms.Select(attrs={'class': 'form-control w-50',
                                                'value': 'Select One'
                                                        })
        
        }
        # category = ChoiceField(widget=forms.Select(attrs={'class':'regDropDown'}))

class TempReceiptForm(ModelForm):
    class Meta:
        model = TempReceipt
        fields = '__all__'