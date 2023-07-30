from django.shortcuts import render
from .models import chat

# Create your views here.
def index(request):
  msg = chat.objects.all()
  chat_data = {'messages': msg}

  if request.method ==  "POST":
    m = request.POST.get("m")
    send_msg = chat.objects.create(
      message = m
    )

    send_msg.save()



  return render(request, 'index.html', chat_data)

  
     