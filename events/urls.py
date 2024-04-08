from django.urls import path

from .views import *

app_name = 'events'
urlpatterns = [
    path('events/', CreateEventsAPIView.as_view()),
    path('get_event/<str:event_name>/', get_events_view),
    path('all_events/', all_events),
    path('update_event/<int:pk>/', update_event),
    path('delete_event/<int:pk>/', delete_event),
    path('get_events_organization/<int:organization_id>/', get_events_organization),
    path('get_events_category/<int:category_id>/', get_events_category),

    path('create_category/', create_category),
    path('update_category/<str:uid>/', update_category),
    path('get_category/<str:uid>/', get_category),
    path('all_categories/', all_category),
    path('delete_category/<str:uid>/', delete_category),


]
