from django.contrib import admin
from .models import chat
# Register your models here.


class chat_admin(admin.ModelAdmin):
  list_display = ('message', 'created_at')
    

admin.site.register(chat, chat_admin)
  

