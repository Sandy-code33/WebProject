from django.shortcuts import render

def track_order_page(request):
    return render(request, 'track/index.html')
