from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Tasks
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import TasksPagination
from .filters import TaskFilter
# Create your views here.

class TasksView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()
    pagination_class = TasksPagination
    filterset_class = TaskFilter
    

    
