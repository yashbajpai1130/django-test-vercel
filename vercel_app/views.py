from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    return HttpResponse("Hello, world! This is my Django app.")
@csrf_exempt
def write(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data['name']
        with open("names.txt", "w+") as f:
            f.write(name)

        return JsonResponse({"message" : "name written"})
@csrf_exempt
def get_last_name(request):
    if request.method == "GET":
        with open("names.txt", "r") as f:
            name = f.read()
        return JsonResponse({"Last entered name" : name})