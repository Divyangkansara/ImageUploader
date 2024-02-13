from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
import os
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    
    return render(request, 'myapp/home.html', {'form':form, 'image':img})

def delete_image(request, image_id):
    try:
        # image = get_object_or_404(Image, pk=image_id)
        image = Image.objects.get(id=image_id)

        if image.photo and os.path.exists(image.photo.path):
            image.photo.delete()
        else:
            return HttpResponse("Image file not found", status=404)
            
        image.delete()
        return HttpResponseRedirect("/")

    except Image.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Images does not exists.')
        return HttpResponseRedirect("/")
        