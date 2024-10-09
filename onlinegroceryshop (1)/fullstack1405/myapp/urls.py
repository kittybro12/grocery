from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout,name='logout'),
    path('main/',views.main,name='main'),
    path("cart/<int:id>",views.cart,name="cart"),
    path("view_cart/",views.view_cart,name="view_cart"),
    path("billing/",views.billing,name='billing'),
    path("payment/",views.payment,name='payment'),



]