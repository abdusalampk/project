from django.urls import path
from . import views
app_name='shopapp'

urlpatterns = [
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.proDetails,name='prodCatDetail'),
]
