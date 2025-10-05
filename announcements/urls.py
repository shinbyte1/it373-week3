from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("announcements/", views.announcement_list, name="announcements"),
    path("announcements/<int:id>/", views.detail, name="detail"),  # <-- name matches template
]

