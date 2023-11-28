from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person.name} - {self.group.name} - {self.timestamp}'