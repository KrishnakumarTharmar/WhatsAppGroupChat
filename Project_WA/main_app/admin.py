from django.contrib import admin
from .models import Group, Person, ChatMessage

admin.site.register(Group)
admin.site.register(Person)
admin.site.register(ChatMessage)
