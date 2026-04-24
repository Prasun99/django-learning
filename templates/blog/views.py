from django.shortcuts import render
from datetime import datetime

class User :
  def __init__(self , name ,age):
   self.name= name
   self.age = age
def context(request):
  content={
  'name':'Prasun',
  'age':22,
  'skills': ['python','django','react'],
  'user':User('Prasun',44),
  'blog': {
    'title': 'Django Template Intro',
    'content': '<b> This is Bold</b>',
    'created_at': datetime(2026,4,10,10,45),
  },
  'empty value' : None,
  }
  return render (request, 'blog/home.html',content)