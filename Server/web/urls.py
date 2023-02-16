from django.urls import path
from web.views import submit_note, register, edit_note, forget, login, whoami

urlpatterns = [
    path('submit/Note/', submit_note , name='submit_note'),
    path('register/' , register, name='register'),  
    path('edit/Note/', edit_note, name='edit_note'),
    path('accounts/register/', register, name='register'),
    path('accounts/forget/', forget, name='forget'),
    path('accounts/login/', login, name='login'),
    path('accounts/whoami/', whoami, name='whoami'),
]