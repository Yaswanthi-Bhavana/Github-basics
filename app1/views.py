import requests
from django.shortcuts import render

# def ut(request):
#     response = requests.get("https://jsonplaceholder.typicode.com/users")
    
#     if response.status_code == 200:
#         users = response.json()
#     else:
#         users = []

#     return render(request, "app1/at.html", {"users": users})




# def index(request):

#     weather_data = {}
#     error = None

#     if request.method == "POST":
#         city = request.POST.get("city")

#         api_key = "49c7f70b13d62b2e48729872980932d6"

#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()

#             weather_data = {
#                 "city": city,
#                 "temperature": data["main"]["temp"],
#                 "humidity": data["main"]["humidity"],
#                 "wind": data["wind"]["speed"],
#                 "description": data["weather"][0]["description"]
#             }

#         else:
#             error = "City not found or API error."

#     return render(request, "app1/index.html", {"weather": weather_data, "error": error})



# def index(request):

#     temperature = None
#     error = None

#     if request.method == "POST":

#         city = request.POST.get("city")
#         api_key = "49c7f70b13d62b2e48729872980932d6"

#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#         response = requests.get(url)
#         data = response.json()

#         if data["cod"] != 200:
#             error = "City not found"
#         else:
#             temperature = data["main"]["temp"]

#     return render(request, "app1/index.html", {"temperature": temperature, "error": error})




# def index(request):

#     temperature = None
#     error = None
#     city = ""

#     if request.method == "POST":

#         city = request.POST.get("city")
#         api_key = "49c7f70b13d62b2e48729872980932d6"

#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#         response = requests.get(url)
#         data = response.json()

#         if data["cod"] != 200:
#             error = "City not found"
#         else:
#             temperature = data["main"]["temp"]

#     return render(request,"app1/index.html",{
#         "temperature": temperature,
#         "error": error,
#         "city": city
#     })

# def index(request):

#     weather_data = {}
#     error = None

#     if request.method == "POST":
#         city = request.POST.get("city")

#         api_key = "49c7f70b13d62b2e48729872980932d6"

#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()

#             weather_data = {
#                 "city": city,
#                 "temperature": data["main"]["temp"],
#                 "humidity": data["main"]["humidity"],
#                 "wind": data["wind"]["speed"],
#                 "description": data["weather"][0]["description"]
#             }

#         else:
#             error = "City not found or API error."

#     return render(request, "app1/index.html", {"weather": weather_data, "error": error})


from django.shortcuts import render
import requests

def index(request):

    users = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        API_KEY = "49c7f70b13d62b2e48729872980932d6"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            error = "City not found. Please enter a valid city name."
        else:
            users = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }

    return render(request, "app1/index.html", {"users": users, "error": error})