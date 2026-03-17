from django.contrib import admin

from .models import Activity, Leaderboard, Team, User, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_name', 'total_points')
    search_fields = ('name', 'email', 'team_name')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'motto')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'activity_type', 'duration_minutes', 'calories_burned', 'recorded_at')
    search_fields = ('user_email', 'activity_type')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'team_name', 'score', 'rank')
    search_fields = ('user_email', 'team_name')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'title', 'difficulty', 'recommended_minutes')
    search_fields = ('user_email', 'title', 'difficulty')
