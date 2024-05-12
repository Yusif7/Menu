from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>', views.MenuItemDetail.as_view(), name='item_detail'),
    path('create/', views.CreateItem.as_view(), name='create_item'),
    path('item/<int:pk>/update/', views.UpdateItem.as_view(), name='update_item'),
    path('item/<int:pk>/delete/', views.DeleteItem.as_view(), name='delete_item'),
]
