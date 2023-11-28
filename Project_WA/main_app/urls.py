from django.urls import path
from .views import group_list, member_detail, group_chat

urlpatterns = [
    path('groups/', group_list, name='group_list'),
    path('member_detail/<int:person_id>/<int:group_id>/', member_detail, name='member_detail'),
    path('group_chat/<int:group_id>/', group_chat, name='group_chat'),
]

