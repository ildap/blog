from django.shortcuts import render

from form import ContactForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/home.html', {'form': form, 'status': 'ok'})
        else:
            return render(request, 'home/home.html', {'form': form, 'status': 'error'})
    else:
        form = ContactForm

        return render(request, 'home/home.html', {'form': form, 'status': 'get'})
