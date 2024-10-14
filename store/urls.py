from . import views
from django.urls import path


urlpatterns = [
    
    path('',views.store, name="store"),
    path('search/',views.search, name="search"),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('<slug:category_slug>/',views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_detail, name='product_detail'),
    
] 