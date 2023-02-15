from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST
from json import JSONEncoder,loads
from web.models import User, Notes, Token
from datetime import datetime

# Create your views here.

@csrf_exempt
def register(request):
    "register a new user"
    pass

@csrf_exempt
def edit_note(request):
    "user edit a note"
    pass

@csrf_exempt
def forget(request):
    "user forget password"
    pass

@csrf_exempt
def login(request):
    "login a user"
    pass

@csrf_exempt
@require_POST
def whoami(request):
    "whoami from request"
    pass

@csrf_exempt
def submit_note(request):
    """user submit a note"""
 
    pass