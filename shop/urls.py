from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("",views.home,name='home'),
    path('women/',views.women,name='women'),
    path('women/product/<int:pk>/', views.women_product, name='women_product'),
    path('men/',views.men,name='men'),
    path('men/product/<int:pk>/', views.men_product, name='men_product'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),  # we’ll create this view next
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='cart'), 
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.view_cart, name='cart'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
