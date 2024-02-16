"""
URL configuration for helloworld project.
"""

from django.urls import path

from first import views


urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.main),
    # http://127.0.0.1:8000/page
    path('page', views.next_page),
]
