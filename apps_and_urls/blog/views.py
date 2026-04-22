from django.http import HttpResponse

def home(request):
  return HttpResponse("this is the blog home page")
def about(request):
  return HttpResponse("this is the blog about page")