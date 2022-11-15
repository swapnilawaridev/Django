from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to Great learning")
def contactUs(request):
    return HttpResponse("Thank you for contact us")