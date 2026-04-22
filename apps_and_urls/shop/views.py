from django.http import HttpResponse

def home(request):
  return HttpResponse("This is shop home page")
def product(request):
  return HttpResponse("This is shop product page")