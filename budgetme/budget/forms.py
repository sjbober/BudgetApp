from django import forms

# from django.db import models
from django.forms import ModelForm

from .models import Expense

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
