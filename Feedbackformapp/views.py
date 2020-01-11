from django.shortcuts import render
from Feedbackformapp.models import Feedback
from Feedbackformapp.forms import Feedbackform
from django.http.response import HttpResponse
import datetime as dt
date1 = dt.datetime.now()

# Create your views here.
def Feedbackview(request):
    if request.method=='POST':
        ffrom = Feedbackform(request.POST)
        if ffrom.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            data = Feedback(
                name=name1,
                rating=rating1,
                feedback=feedback1,
                date = date1
            )
            data.save()
            ffrom = Feedbackform()
            feedbacks = Feedback.objects.all()
            return render(request,'feedback.html',{'ffrom':ffrom,'feedbacks':feedbacks})
        else:
            return HttpResponse('User Missing Values')
    else:
        ffrom = Feedbackform()
        feedbacks = Feedback.objects.all()
        return render(request,'feedback.html',{'ffrom':ffrom,'feedbacks':feedbacks})
