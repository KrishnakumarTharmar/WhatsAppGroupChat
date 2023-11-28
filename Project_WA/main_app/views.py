from django.shortcuts import render, get_object_or_404
from .models import Group, Person, ChatMessage
from django.utils import timezone

def group_list(request):
    groups = Group.objects.all()

    common_members = {}
    
    for group in groups:
        for person in group.person_set.all():
            person_name = person.name.strip().lower()
            common_members.setdefault(person_name, {'groups': set()})
            common_members[person_name]['groups'].add(group.name)

    common_members_list = []
    
    for person_name, info in common_members.items():
        common_members_list.append({
            'person_name': person_name,
            'group_names': ', '.join(info['groups']),
        })

    return render(request, 'group_list.html', {'groups': groups, 'common_members': common_members_list})
def member_detail(request, person_id, group_id):
    person = get_object_or_404(Person, pk=person_id)
    group = get_object_or_404(Group, pk=group_id)
    messages = ChatMessage.objects.filter(person=person, group=group)

    if request.method == 'POST':
        entered_text = request.POST.get('entered_text')

        if entered_text:
            ChatMessage.objects.create(person=person, group=group, message=entered_text, timestamp=timezone.now())

    return render(request, 'member_detail.html', {'person': person, 'group': group, 'messages': messages})
def group_chat(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    members = group.person_set.all()
    messages = ChatMessage.objects.filter(group=group)

    if request.method == 'POST':
        entered_text = request.POST.get('entered_text')

        if entered_text:
            person = get_object_or_404(Person, pk=request.user.id)
            ChatMessage.objects.create(person=person, group=group, message=entered_text, timestamp=timezone.now())

    return render(request, 'group_chat.html', {'group': group, 'members': members, 'messages': messages})