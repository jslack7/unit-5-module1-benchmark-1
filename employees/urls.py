from django.urls import path

from . import views 

urlpatterns = [
    path("id/", views.filter_by_id),
    path("firstname/", views.filter_by_first_name),
    path("money-ceiling/", views.filter_by_greater_than_salary)
]