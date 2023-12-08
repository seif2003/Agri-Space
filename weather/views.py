from dotenv import load_dotenv
import os
from django.http import JsonResponse
import requests

url = "http://api.weatherapi.com/v1/current.json"


def weather_api(request):
    if request.method == 'POST':
        loc = request.POST.get('location')
        res = requests.get(url, headers={"Accept": "application/json"}, params={"key":os.getenv("WEATHER_KEY"),"q":loc})
        return JsonResponse(res.json())
