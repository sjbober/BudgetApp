from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.login_view, name='index'),

    path('logout/', views.logout_view, name='logout'),

    path('expenses/', views.expense_list, name='expense_list'),

    path('expenses/recurring', views.expense_list_recurring, name='expense_list_recurring'),

    path('expenses/expense-form-page/', views.expense_form_page, name='expense_form_page'),

    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),

    path('expenses/recurring/<int:pk>/', views.recurring_edit, name='recurring_edit'),

    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),

    path('categories/', views.category_list, name='category_list'),

    path('categories/create-category/', views.create_category, name='create_category'),


]