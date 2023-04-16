from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview,name='home'),
    path('create/', views.add_items,name='add-items'),
    # path('pets/', views.pets,name='view-all-pets'),
    # path('update/<int:pk>', views.update_items,name='update-items'),
    # path('item/<int:pk>/delete/', views.delete_items,name='delete-items'),
    # path('pets/<int:pet_id>/', views.view_pet,name='view_pet'),
    
]