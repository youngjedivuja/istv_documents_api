from django.core.files.storage import FileSystemStorage


def upload(request):
    uploaded_file = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)
