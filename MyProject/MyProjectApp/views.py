from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def login_url(request):
    return render(request, 'login.html')


@csrf_exempt
def login_api(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username.upper() == "SAHIL" and password == "1234":
                data = {
                    "username": "sahil",
                    "age": 23,
                    "gender": "Male",
                    "Designation": "Software Developer"
                }
                response = {}
                response["status"] = True
                response["message"] = "Success"
                response["data"] = data
                return JsonResponse(response)
            else:
                response = {}
                response["status"] = False
                response["message"] = "Invalid username or password"
                response["data"] = []
                return JsonResponse(response)
        response = {}
        response["status"] = False
        response["message"] = "Get Request not allowed"
        response["data"] = []
        return JsonResponse(response)
    except Exception as e:
        print("Error--------->", e)
        response = {}
        response["status"] = False
        response["message"] = "Internal server error!"
        response["data"] = []
        return JsonResponse(response)


def home_url(request):
    return render(request, "home.html")
