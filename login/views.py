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
        forgot = request.POST.get('password')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        user_profile = UserProfile.objects.create(
            name=name,
            user_type=user_type,
            roll_number=roll_number,
            teacher_id=teacher_id,
            email=email,
            password=password,
            forgot= forgot
        )

        print(f"Email: {email}; Password: {password}; Name: {name}; Roll Number: {roll_number}; Teacher ID: {teacher_id}")
        return redirect('login')

    return render(request, 'not_access.html')

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

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from urllib.parse import unquote
def forgot_password(request):
    login_email = request.GET.get('email')
    print("Login Email:", login_email)
    email = login_email
    try:
        user_profile = UserProfile.objects.get(email=email)
    except UserProfile.DoesNotExist:
        print("No User")
        return render(request, 'index.html', {'error_message': 'No account found with this email address'})
    forgot_value = user_profile.forgot
    name = user_profile.name
    
    forgotPasswordMail(email, forgot_value,name)
    print("Mail Sent")
    return render(request, 'index.html')

def forgotPasswordMail(to_email,password,name = "User"):
    MAIL_ID = "ENTER_YOUR_GMAIL"
    # Refer this to create app password : https://support.google.com/accounts/answer/185833?hl=en
    PASSWORD = "xxxx xxxx xxxx xxxx"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 
    subject = "Password Recovery - Academia Campus Repository"
    msg = MIMEMultipart()
    msg['From'] = MAIL_ID
    msg['To'] = to_email
    msg['Subject'] = subject
    
    content = """
                <p>Dear NAME,</p>
                <p>Your Password is : <b> PASSWORD </b></p>
                <br>
                <p><b>With Regards,</b></p>
                <br>
                <img src="cid:image1" alt="Image" style="width: 250px;">
                """.replace("PASSWORD",password).replace("NAME",name)
    msg.attach(MIMEText(content, 'html'))
    
    with open("textLogo.png", 'rb') as image_file:
        img = MIMEImage(image_file.read(), name='image.png')
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(MAIL_ID, PASSWORD)
        server.sendmail(MAIL_ID, to_email, msg.as_string())