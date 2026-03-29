from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('reg',views.registration,name="registration"),
    path('log',views.user_login,name="user_login"),
    path('uhome',views.user_home,name="user_home"),
    path('adhome',views.adminHome,name="adminHome"),
    path('addmen',views.add_product,name="add_product"),
    # path('view_men',views.view_product,name="view_product"),
    path('usr',views.view_users,name="view_user"),
    path('edit/',views.edit_user,name="edit_user"),
    path('delete',views.delete_user,name="delete_user"),
    path('mens/', views.mens_product, name='mens'),
    path('womens/', views.womens_product, name='womens'),
    path('kids/', views.kids_product, name='kids'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove',views.remove_from_cart,name="remove_from_cart"),
    
]