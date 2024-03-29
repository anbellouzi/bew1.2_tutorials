from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
]
