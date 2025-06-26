from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, uuid, requests
from .models import Location

def send_tracking_link(request):
    user_id = str(uuid.uuid4())
    phone_number = "+919600794837"
    tracking_url =  f"http://127.0.0.1:8000/track-location/{user_id}/"
    message = f"Click here to share your location: {tracking_url}"

    payload = {
        "authorization": "DiXzMbqrOtE4sx2yNZuP8I1Q6ReLSdTgJoCFaUfc3vKV7BpYwloQPFC2KTS41gRGwHlLrbmv79ZfyhMV",
        "sender_id": "TXTIND",
        "message": message,
        "language": "english",
        "route": "v3",
        "numbers": phone_number,
    }

    headers = {'cache-control': "no-cache"}
    response = requests.post("https://www.fast2sms.com/dev/bulkV2", data=payload, headers=headers)
    print(response.text)
    return render(request, 'link_sent.html', {'link': tracking_url})

def track_location(request, uuid):
    return render(request, 'track_location.html', {'uuid': uuid})

@csrf_exempt
def save_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Location.objects.create(
            user_id=data['id'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        return JsonResponse({'status': 'Location saved'})
