from django.shortcuts import redirect, render

# Create your views here.

def home_view(request):

    cookie_value = request.COOKIES.get('background', "white")


    response = render(request, "main/home.html", {"background": cookie_value})
    return response

def toggle_background(request):


    background = request.POST.get('button')

    response = render(request, "main/home.html", {"background": background})
    response.set_cookie("background", background)
    return response


def contact_view(request):
    
    
    return render(request, "main/contact.html", )

def home_dark_view(request):
    
    
    return render(request, "main/home_dark.html", )


def dark_base_view(request):
    
    
    return render(request, "main/dark_base.html", )

def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great Home for You in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 Bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    context = {
        'properties': properties 
    }
    return render(request, 'main/properties.html', context)


def base_view(request):
    
    
    return render(request, "main/base.html", )

