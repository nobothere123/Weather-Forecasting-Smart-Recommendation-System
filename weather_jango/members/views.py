from django.shortcuts import render
from django.http import HttpResponse
from weather_files.location import get_location 
from weather_files.geo_zipcode import geo_location

# Create your views here.

def weather_home(requests):
    return render(requests,"prediction_page.html")

def run_weather(request):

    if request.method == "POST":
        # print("POST DATA:", request.POST)
        form_type = request.POST.get("form_type")
        # print("Form type:", form_type)
        
        if form_type == "current":

            result_data = get_location()
            return render(
                request,
                "weather_result.html",
                {"data": result_data}
            )
            
        elif form_type == "location":
            postal_code = request.POST.get("zipcode")
            country_name = request.POST.get("country")
            # print(postal_code,country_name)
            result_data = geo_location(postal_code,country_name)
            
            return render(
                request,
                "weather_result.html",
                {"data": result_data}
            )