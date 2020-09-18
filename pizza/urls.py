from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', views.index, name="pizza-index"),
    path('pizzas/<int:pizza_id>', views.show2, name='pizza-show'),
    path('pizzas/new/', views.create, name='create-pizza')
]