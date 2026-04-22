from django.urls import path
from .  import views
urlpatterns = [
  path('home/',views.home,name="shop_home"),
  path('product/',views.product,name="shop_product"),
]