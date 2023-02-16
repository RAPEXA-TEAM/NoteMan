from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
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
    
    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        username = json['username']
        password = json['password']

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

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        this_token = json['token']
        
        try:
            this_user = get_object_or_404(User, token__token=this_token)

            return JsonResponse({
                'data': this_user.username,
                'code' : 200,
            }, encoder=JSONEncoder)

        except Exception as e:

            return JsonResponse({
                'data': "token invalid!",
                'code' : 404,
            }, encoder=JSONEncoder)

    else:

        return JsonResponse({
            'data': 'request not valid!',
            'code': 401,
        }, encoder=JSONEncoder)

@csrf_exempt
def submit_note(request):
    '''this function handle the submit note request'''

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        this_token = json['token']
        this_title = json['title']
        this_text = json['text']
        
        try:
        
            this_user = User.objects.filter(token__token = this_token).get()
            
            now = datetime.now()
            
            Notes.objects.create(user = this_user, title = this_title , text = this_text , date = now)

            return JsonResponse({
                'data' : 'ok',
                'code' : 200,
            }, encoder=JSONEncoder)
    
        except Exception as e:

            return JsonResponse({
                'data': "token invalid!",
                'code' : 404,
            }, encoder=JSONEncoder)