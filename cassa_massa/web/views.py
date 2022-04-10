from django.shortcuts import render

from cassa_massa.web.forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contacts.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contacts.html', context)
