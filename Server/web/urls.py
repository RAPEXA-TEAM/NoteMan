from django.urls import path
from web.views import submit_note, register, edit_note_text, edit_note_title, forget, login, whoami, delete_note

urlpatterns = [
    path('Note/submit', submit_note , name='submit_note'),
    path('Note/delete', delete_note , name='delete_note'),
    path('Note/edit/title', edit_note_title, name='edit_note_title'),
    path('Note/edit/text', edit_note_text, name='edit_note_text'),
    path('accounts/register', register, name='register'),
    path('accounts/forget', forget, name='forget'),
    path('accounts/login', login, name='login'),
    path('accounts/whoami', whoami, name='whoami'),
]