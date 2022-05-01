from django.shortcuts import render
from rest_framework import viewsets
from task.serializer import TaskSerializer
from task.models import Task
from rest_framework import mixins
from rest_framework.decorators import action


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()




