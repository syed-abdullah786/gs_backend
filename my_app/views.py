from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .models import Employee, TeamCollection, Team, Role, Comment, Task
from .serializers import EmployeeSerializer, TeamCollectionSerializer, TeamSerializer, TaskSerializer, RoleSerializer, \
    CommentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TeamCollectionViewSet(ModelViewSet):
    queryset = TeamCollection.objects.all()
    serializer_class = TeamCollectionSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

