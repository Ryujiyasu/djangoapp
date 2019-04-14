from django.urls import path
from . import views

urlpatterns = [
    path('<str:artist>/<int:yearmonth>/', views.sum),
    path('<str:artist>/', views.sum),
    path('artist',views.MyListView.as_view()),

]