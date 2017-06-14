from django.shortcuts import render
from .forms import DocumentForm, Document


def model_form_upload(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'hashes/model_form_upload.html', {
        'form': form,
        'documents': documents,
    })
