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
            doc.uploaded_count = 1
            for saved_doc in Document.objects.all():
                if saved_doc.sha256 == sha_256:
                    saved_doc.uploaded_count += 1
                    doc.uploaded_count += 1
                    saved_doc.save()
            doc.save()
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'hashes/model_form_upload.html', {
        'form': form,
        'documents': documents,
    })
