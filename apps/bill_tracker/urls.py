from django.urls import path
from . import views

app_name = 'bill_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_bill', views.add_bill, name='add_bill'),
    path('edit_bill/<int:bill_id>', views.edit_bill, name='edit_bill'),
    path('update_bill', views.update_bill, name='update_bill'),
    path('del_bill/<int:bill_id>', views.del_bill, name='del_bill'),
]

