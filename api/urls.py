from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('core/products/', views.ProductListView.as_view()),
    path('core/products/<int:pk>/', views.ProductDetailView.as_view()),
    path('core/categories/', views.CategoryListView.as_view()),
    path('core/categories/<int:pk>/', views.CategoryDetailView.as_view()),
    path('core/feedbacks/', views.FeedbackListView.as_view()),
    path('core/feedbacks/<int:pk>/', views.FeedbackDetailView.as_view()),
    path('core/feedbacks/create/', views.FeedbackCreateView.as_view()),
    path('accounts/users/', views.UserListView.as_view()),
    path('accounts/users/<int:pk>/', views.UserDetailView.as_view()),
    path('accounts/users/signup/', views.UserCreateView.as_view()),
    path('accounts/users/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]