from django.urls import path
from .views import Home, Add_job,Delete_job,EditJob

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-job/', Add_job.as_view(), name='add-job'),
    path('delete-job/', Delete_job.as_view(), name='delete-job'),
    path('edit-job/<int:id>/', EditJob.as_view(), name='edit-job'),
]
