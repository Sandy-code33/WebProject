from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, get_object_or_404
# from .models import Order

# def track_order(request, order_id):
#     order = get_object_or_404(Order, order_id=order_id)
#     return render(request, 'track_order.html', {'order': order})

from django.shortcuts import render
from .models import Order, OrderStatus

def track_order(request):
    context = {}
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(order_id=order_id)
            statuses = OrderStatus.objects.filter(order=order).order_by('timestamp')
            context['order'] = order
            context['statuses'] = statuses
        except Order.DoesNotExist:
            context['error'] = 'Order ID not found.'
    return render(request, 'track_order.html', context)
