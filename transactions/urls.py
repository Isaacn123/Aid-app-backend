from django.urls import path
from .views import *

app_name = 'transactions'
urlpatterns = [
    path('all_transactions/', get_all_transactions),
    path('create_transactions/', create_transaction),
    path('get_transaction_event/<str:event_uid>/', get_all_transactions_event),
    
]
