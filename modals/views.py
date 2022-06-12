from django.shortcuts import render

from modals.models import Feedback
from modals.forms import FeedbackForm

# Create your views here.
def index(request):
    form = FeedbackForm()
    context = {'form': form}
    
    return render(request, 'modals/index.html', context)