from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('', views.summary, name='summary'),

    path('signup/', views.signup, name='signup'),

    path('logout/', views.logout_view, name='logout'),

    path('expenses/', views.expense_list, name='expense_list'),

    path('expenses/recurring/', views.expense_list_recurring, name='expense_list_recurring'),

    path('expenses/record-spending/', views.record_spending, name='record_spending'),

    path('expenses/create-repeat-bill/', views.create_repeat_bill, name='create_repeat_bill'),

    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),

    path('expenses/recurring/<int:pk>/', views.recurring_edit, name='recurring_edit'),

    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),

    path('expenses/categories/', views.category_list, name='category_list'),

]