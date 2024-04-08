from django.urls import path

from .views import create_organization, all_organizations, get_organization, delete_organization, update_organization, get_organization_user

app_name = 'organization'
urlpatterns = [
    path("create_organization/", create_organization),
    path("organizations/", all_organizations),
    path("get_organization/<int:pk>/", get_organization),
    path("update_organization/<int:pk>/", update_organization),
    path("delete_organization/<int:pk>/", delete_organization),
    path("get_organization_user/<int:user_id>/", get_organization_user),

]