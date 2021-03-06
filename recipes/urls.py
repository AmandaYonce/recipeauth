from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="homepage"),
    path('recipes/<int:recipe_id>/', views.recipes),
    path('authors/<int:author_id>/', views.authors),
    path('newrecipe/', views.recipe_form_view),
    path('newauthor/', views.author_form_view),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('signup/', views.signup_view, name='signupview')
]