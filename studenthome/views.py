# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teacherhome.models import File
from login.models import UserProfile

from django.db.models import Q

@login_required
def studentHome(request):
    try:
        profile = UserProfile.objects.get(email=request.user.email)
    except UserProfile.DoesNotExist:
        profile = None
        print('UserProfile not found for user:', request.user.email)

    search_query = request.GET.get('search', '')

    # Retrieve files with permission set to 1 and filter based on the search query
    files = File.objects.filter(permission=1)

    if search_query:
        # Filter files by file name or teacher name using Q objects for OR condition
        files = File.objects.filter(permission=1,file__icontains=search_query)


    context = {
        'profile': profile,
        'files_data': files,
        'search_query': search_query,
    }
    return render(request, 'studenthome.html', context)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.files import File as DjangoFile
from wsgiref.util import FileWrapper
from mimetypes import guess_type
from teacherhome.models import File

def download_file(request, file_id):
    file_instance = get_object_or_404(File, id=file_id)
    file_path = file_instance.file.path

    # Create a file wrapper for the response
    response = HttpResponse(FileWrapper(open(file_path, 'rb')), content_type=guess_type(file_path)[0])
    
    # Set the Content-Disposition header to force download
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
    
    return response