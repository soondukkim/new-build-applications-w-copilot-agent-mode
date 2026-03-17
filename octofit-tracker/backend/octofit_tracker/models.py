from bson import ObjectId
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    motto = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'teams'
        ordering = ['name']

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, default='')
    total_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
        ordering = ['name']

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField(default='')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-recorded_at']


class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField(default='')
    team_name = models.CharField(max_length=100, default='')
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField(default='')
    title = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=50)
    recommended_minutes = models.IntegerField()

    class Meta:
        db_table = 'workouts'
        ordering = ['title']
