from django.shortcuts import render
from .forms import DocumentForm, Document
import hashlib


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            file_path = doc.filepath()
            sha_256 = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
            doc.sha256 = sha_256
            doc.save()
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'hashes/model_form_upload.html', {
        'form': form,
        'documents': documents,
    })
