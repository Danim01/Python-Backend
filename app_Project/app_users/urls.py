from django.urls import path
from . import views 

urlpatterns = [
  path('get_user_request/<int:pk>/', views.get_user_request, name="get_user_request"),
  path('get_all_request/', views.get_all_request, name="get_all_request"),
  path('delete_user_request/<int:pk>/', views.delete_user_request, name="delete_user_request"),
  path('put_user_request/<int:pk>/', views.put_user_request, name="put_user_request"),
  path('post_user_request/', views.post_user_request, name="post_user_request"),
]