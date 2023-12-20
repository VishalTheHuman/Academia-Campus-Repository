from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import UserProfile
from .forms import FileModelForm
from .models import File
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.files import File as DjangoFile
from wsgiref.util import FileWrapper
from mimetypes import guess_type
from django.contrib.auth.models import User
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from urllib.parse import unquote

@login_required
def teacherHome(request):
    try:
        profile = UserProfile.objects.get(email=request.user.email)
    except UserProfile.DoesNotExist:
        profile = None
        print('UserProfile not found for user:', request.user.email)
        return render(request, '404.html')

    # Retrieve files based on the search parameter if provided
    search_query = request.GET.get('search', '')
    if search_query:
        files = File.objects.filter(owner=request.user, file__icontains=search_query)
    else:
        files = File.objects.filter(owner=request.user)

    context = {
        'profile': profile,
        'files': files,
        'filtered_files': files,  # Used for displaying search results
    }
    return render(request, 'teacherhome.html', context)

@login_required
def upload_form(request):
    try:
        profile = UserProfile.objects.get(email=request.user.email)
        name = profile.name
        email = profile.email
    except UserProfile.DoesNotExist:
        profile = None
        print('UserProfile not found for user:', request.user.email)
        return render(request, '404.html')
    
    context = {
        'profile': profile,
    }

    if request.method == 'POST':
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.owner = request.user
            file_name = file_instance.file.name
            permission_status = file_instance.permission
            file_instance.save()
            if file_name and permission_status and name:
                notification(file_name,name,email)
                          

    else:
        form = FileModelForm()

    try:
        profile = UserProfile.objects.get(email=request.user.email)
    except UserProfile.DoesNotExist:
        profile = None
        print('UserProfile not found for user:', request.user.email)
        return render(request, '404.html')

    # Retrieve files based on the search parameter if provided
    search_query = request.GET.get('search', '')
    if search_query:
        files = File.objects.filter(owner=request.user, file__icontains=search_query)
    else:
        files = File.objects.filter(owner=request.user)

    context = {
        'profile': profile,
        'files': files,
        'filtered_files': files,  # Used for displaying search results
    }
    return render(request, 'teacherhome.html', context)

        

def download_file(request, file_id):
    file_instance = get_object_or_404(File, id=file_id)
    file_path = file_instance.file.path

    # Create a file wrapper for the response
    response = HttpResponse(FileWrapper(open(file_path, 'rb')), content_type=guess_type(file_path)[0])
    
    # Set the Content-Disposition header to force download
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
    
    return response

@login_required
def delete_file(request, file_id):
    file_instance = get_object_or_404(File, id=file_id, owner=request.user)
    
    if request.method == 'POST':
        file_instance.delete()

    return redirect('teacherhome')

def get_teacher_name_and_id(uploaded_by):
    try:
        teacher_profile = UserProfile.objects.get(user__username=uploaded_by)
        return teacher_profile.name, teacher_profile.teacher_id
    except UserProfile.DoesNotExist:
        return None, None

def notification(file_name,name,email):
    MAIL_ID = "ENTER_YOUR_GMAIL"
    # Refer this to create app password : https://support.google.com/accounts/answer/185833?hl=en
    PASSWORD = "xxxx xxxx xxxx xxxx"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 
    students = list(getStudents())
    try:
        subject = f"'{file_name}' was added by '{name}'- Academia Campus Repository"
        msg = MIMEMultipart()
        msg['From'] = MAIL_ID
        msg['To'] = ", ".join(students)
        msg['Subject'] = subject
        content = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Email Subject</title>
                    </head>
                    <body>
                        <p>Dear Student,</p>
                        <p>A File named 'FILE' has been uploaded by 'TEACHER'</p>
                        <br>
                        <p><b>With Regards,</b></p>
                        <br>
                        <img src="cid:image1" alt="Image" style="width: 250px;">
                    </body>
                    </html>
                    """.replace("FILE",file_name).replace("TEACHER",name)
        with open("D:\\Code\\Projects Individual Repository\\Academia-Campus-Repository\\test\\server\\login\\textLogo.png", 'rb') as image_file:
            img = MIMEImage(image_file.read(), name='image.png')
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)
        msg.attach(MIMEText(content, 'html'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(MAIL_ID, PASSWORD)
            server.sendmail(MAIL_ID, students, msg.as_string())
    except Exception as e:
        print(e)
        
def getStudents():
    students_emails = UserProfile.objects.filter(user_type='Student').values_list('email', flat=True)
    return students_emails