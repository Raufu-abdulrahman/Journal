from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('journal/', views.journal, name='journal'),
    path('journal/new/', views.new_journal, name='new_journal'),
    path('journal/<int:journal_id>/', views.journal_detail, name='journal_detail'),
    path('journal/<int:journal_id>/edit/', views.update_journal, name='update'),
    path('journal/<int:journal_id>/del/', views.del_journal, name='delete'),
]