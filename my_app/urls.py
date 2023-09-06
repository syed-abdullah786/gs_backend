from django.contrib import admin
from django.urls import path
from rest_framework_nested.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register('employee', views.EmployeeViewSet, basename="employee")
router.register('team', views.TeamViewSet, basename="team")
router.register('teamcollection', views.TeamCollectionViewSet, basename="teamcollection")
router.register('role', views.RoleViewSet, basename="role")
router.register('task', views.TaskViewSet, basename="task")
router.register('comment', views.CommentViewSet, basename="comment")

urlpatterns = [

] + router.urls