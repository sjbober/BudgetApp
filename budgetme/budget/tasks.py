# Models
from .models import Expense
from .models import RecurringExpense


active_recexp = RecurringExpense.objects.filter(active__exact=True)