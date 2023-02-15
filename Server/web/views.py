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
    # check if POST objects has username and password
    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        username = json['username']
        password = json['password']

        print(username, password)
        this_user = get_object_or_404(User, username=username)

        if (check_password(password, this_user.password)):  # authentication

            this_token = get_object_or_404(Token, user=this_user)
            token = this_token.token
            
            context = {}
            context['code'] = 200
            context['token'] = token
            return JsonResponse(context, encoder=JSONEncoder)

        else:
            
            context = {}
            context['code'] = 404
            context['data'] = 'error password incorrect'
            return JsonResponse(context, encoder=JSONEncoder)
        
    context = {}
    context['code'] = 401
    context['data'] = "request not valid!"
    return JsonResponse(context, encoder=JSONEncoder)

@csrf_exempt
@require_POST
def whoami(request):
    "whoami from request"
    pass

@csrf_exempt
def submit_note(request):
    """user submit a note"""
 
    pass