from django.shortcuts import render

from modals.models import Feedback
from modals.forms import FeedbackForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'modals/partials/success.html')
        return render(request, 'modals/partials/failure.html')
     
    form = FeedbackForm()
    context = {'form': form}   
    return render(request, 'modals/index.html', context)