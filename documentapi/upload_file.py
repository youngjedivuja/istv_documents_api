from django.core.files.storage import FileSystemStorage
import mimetypes

from django.http import HttpResponse

fs = FileSystemStorage()


def upload(request, data):
    uploaded_file = request.FILES['file']
    data['file_name'] = uploaded_file.name
    fs.save(uploaded_file.name, uploaded_file)
    return data


def download(file_name):
    with open(fs.path(file_name), 'rb') as f:
        content = f.read()
    # fl = open(fs.path(file_name), errors=ignore).read()
    mime_type, _ = mimetypes.guess_type(fs.path(file_name))
    response = HttpResponse(content, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response
