
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home_page'),
    path('add/', views.addData, name='add_data'),
    path('update/<int:pk>/', views.updateData, name='add_data'),
    path('delete/<int:pk>/', views.deleteData, name='delete_data'),
]
