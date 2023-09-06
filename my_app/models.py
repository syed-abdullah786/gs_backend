from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=GENDER)
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    joining_date = models.DateField()
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=20)
    field = models.CharField(max_length=20)


class Team(models.Model):
    name = models.CharField(max_length=50)


class Role(models.Model):
    name = models.CharField(max_length=50,default="employee")
    permission = models.JSONField(default="{access:all}")


class TeamCollection(models.Model):
    employee = models.ManyToManyField(Employee,related_name='team_collections')
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    role = models.ManyToManyField(Role)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(Employee, on_delete=models.RESTRICT, related_name='created_team_collection')


class Task(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('progress', 'progress'),
        ('complete', 'complete')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS)
    client_name = models.CharField(max_length=50)
    communicator = models.OneToOneField(Employee, on_delete=models.RESTRICT,related_name="communicator")
    main_developer = models.OneToOneField(Employee, on_delete=models.RESTRICT,related_name="developer")
    helper_developer = models.OneToOneField(Employee, on_delete=models.RESTRICT,related_name="helper")
    estimated_hours = models.IntegerField()
    platform = models.CharField(max_length=70)
    started_date = models.DateField()
    completed_date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    # code = models.FileField(upload_to='specs', null=True)


class Comment(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    started_date = models.DateField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
