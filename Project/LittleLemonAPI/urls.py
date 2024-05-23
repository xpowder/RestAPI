from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    
   
    path('', views.ProductList.as_view()),
    path('product-list/', views.ProductList.as_view()),
    path('product-list/<int:pk>', views.ProductList.as_view()),
    path('product-list/<int:pk>', views.UpdateProduct.as_view(), name='product-detail-update-delete'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('order-item/', views.OrdersViews.as_view()),
    path('order-item/<int:pk>', views.OrdersViews.as_view()),
    path('customer', views.CustomerName.as_view(), name='customer-list'),
    path('category', views.CategoryView.as_view()),
    path('user/orders/', views.UserOrders.as_view()),
    path('user/orders/<int:pk>', views.UserOrders.as_view()),
    
]




