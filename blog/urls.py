from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    
    path('post/new/', views.post_new, name='post_new'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('', views.post_list, name='post_list'),    
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post-edit/<str:slug>/', views.post_edit, name='post_edit'),
    path('post_Category/<int:id>/', views.post_Category, name='post_Category'),
    path('post_Tag/<int:id>/', views.post_Tag, name='post_Tag'),
    path('post_author/<int:id>/', views.post_author, name='post_author'),
    # path('post_Published_date/<int:id>/', views.post_published_date, name='post_published_date'),


]
