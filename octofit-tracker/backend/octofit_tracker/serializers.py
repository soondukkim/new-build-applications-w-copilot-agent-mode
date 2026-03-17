from rest_framework import serializers

from .models import Activity, Leaderboard, Team, User, Workout


class ObjectIdStringField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data


class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'motto']
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team_name', 'total_points']
        read_only_fields = ['id']


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'activity_type', 'duration_minutes', 'calories_burned', 'recorded_at']
        read_only_fields = ['id', 'recorded_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user_email', 'team_name', 'score', 'rank']
        read_only_fields = ['id']


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user_email', 'title', 'difficulty', 'recommended_minutes']
        read_only_fields = ['id']
