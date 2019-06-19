"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from experts import views as experts_views
from experts import views_update as update_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_rest/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('password_rest/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('addexpert/', experts_views.addExpert, name='addexpert'),
    path('addecomment/', experts_views.addComment, name='addcomment'),
    path('addeworkexp/', experts_views.addWorkexp, name='addworkexp'),

    path('addexperttodatabase/', experts_views.addExpertToDatabase, name='addexperttodatabase'),
    path('addcommenttodatabase/', experts_views.addCommentToDatabase, name='addcommenttodatabase'),
    path('addworkexptodatabase/', experts_views.addWorkexpToDatabase, name='addworkexptodatabase'),

    path('addcomplete/', experts_views.addok, name='addcomplete'),
    path('expertalreadyexist/', experts_views.addExpertToDatabase, name='expertalreadyexist'),

    path('updateexpert/', update_views.expertInfoUpdate, name='updateexpert'),
    path('expertinfolist/', experts_views.expertInfo_list, name='expertinfolist'),
    path('<str:ename>/<str:emobile>/', experts_views.expert_detail, name='expert_detail'),
    path('update/<str:ename>/<str:emobile>/', experts_views.expert_detail_update, name='expert_detail_update'),
    path('expertinfoupdatetodatabase/', update_views.expertInfoUpdateToDatabase, name='expertinfoupdatetodatabase'),

    path('<int:eid>/<str:ename>/commentdetail/', experts_views.comment_detail, name='comment_detail'),

    path('', include('experts.urls')),
    path('', include('users.urls')),

]

"""
path('update/<str:ename>/<str:emobile>/', experts_views.expert_detail_update, name='expert_detail_update'),
path('updateexpert/', update_views.expertInfoUpdate, name='updateexpert'),
path('expertinfoupdatetodatabase/', update_views.expertInfoUpdateToDatabase, name='expertinfoupdatetodatabase'),

"""
