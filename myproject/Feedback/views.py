from django.shortcuts import render,redirect
from .models import Feedback
from django.http import JsonResponse
# Create your views here.

def feedback_form(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        remark = request.POST.get('remark')
        Feedback.objects.create(rating=rating, remark=remark)
        return JsonResponse({'message': 'Feedback submitted successfully!'})
    return render(request,'feedback.html')