from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

def login(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_type = request.POST.get('userType')
        roll_number = request.POST.get('roll_number', '')
        teacher_id = request.POST.get('teacher_id', '')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        user_profile = UserProfile.objects.create(
            name=name,
            user_type=user_type,
            roll_number=roll_number,
            teacher_id=teacher_id,
            email=email,
            password=password 
        )

        print(f"Email: {email}; Password: {password}; Name: {name}; Roll Number: {roll_number}; Teacher ID: {teacher_id}")
        return redirect('not_found')

    return render(request, 'index.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user_profile = UserProfile.objects.get(email=username)
        except UserProfile.DoesNotExist:
            user_profile = None

        user = authenticate(request, username=username, password=password)

        if user_profile is not None and user is not None:
            auth_login(request, user)
            
            if user_profile.user_type == 'Student':
                return redirect('studenthome')
            elif user_profile.user_type == 'Teacher':
                return redirect('teacherhome')
            else:
                return redirect('not_found')
        else:
            return redirect('no_access')

    return render(request, 'index.html')
