from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import UserProfile
from .forms import FileModelForm
from .models import File
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import File
from .forms import FileModelForm
from login.models import UserProfile

@login_required
def upload_form(request):
    try:
        profile = UserProfile.objects.get(email=request.user.email)
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
            file_instance.save()

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

        
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.files import File as DjangoFile
from wsgiref.util import FileWrapper
from mimetypes import guess_type
from .models import File

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

# teacherhome/views.py

from django.contrib.auth.models import User
from .models import File
from login.models import UserProfile

def get_teacher_name_and_id(uploaded_by):
    try:
        teacher_profile = UserProfile.objects.get(user__username=uploaded_by)
        return teacher_profile.name, teacher_profile.teacher_id
    except UserProfile.DoesNotExist:
        return None, None