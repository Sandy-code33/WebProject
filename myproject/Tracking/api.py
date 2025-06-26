from django.http import JsonResponse
from .models import Order

def track_order_api(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        data = {
            "order_id": order.order_id,
            "customer": order.customer_name,
            "status": order.status,
            "last_updated": order.last_updated.strftime('%Y-%m-%d %H:%M:%S')
        }
        return JsonResponse({"success": True, "data": data})
    except Order.DoesNotExist:
        return JsonResponse({"success": False, "error": "Order not found"})
