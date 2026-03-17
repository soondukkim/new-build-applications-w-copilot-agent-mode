from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(name='marvel team', motto='Avengers Assemble')
        dc = Team.objects.create(name='dc team', motto='Justice League United')

        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team_name=marvel.name, total_points=980),
            User.objects.create(name='Captain America', email='captain@marvel.com', team_name=marvel.name, total_points=920),
            User.objects.create(name='Batman', email='batman@dc.com', team_name=dc.name, total_points=990),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_name=dc.name, total_points=940),
        ]

        Activity.objects.bulk_create(
            [
                Activity(user_email=users[0].email, activity_type='Running', duration_minutes=45, calories_burned=420),
                Activity(user_email=users[1].email, activity_type='Cycling', duration_minutes=60, calories_burned=510),
                Activity(user_email=users[2].email, activity_type='Weight Training', duration_minutes=50, calories_burned=480),
                Activity(user_email=users[3].email, activity_type='Yoga', duration_minutes=40, calories_burned=260),
            ]
        )

        Workout.objects.bulk_create(
            [
                Workout(user_email=users[0].email, title='Repulsor Core HIIT', difficulty='Hard', recommended_minutes=35),
                Workout(user_email=users[1].email, title='Shield Endurance Circuit', difficulty='Medium', recommended_minutes=40),
                Workout(user_email=users[2].email, title='Gotham Strength Set', difficulty='Hard', recommended_minutes=45),
                Workout(user_email=users[3].email, title='Amazon Agility Flow', difficulty='Medium', recommended_minutes=30),
            ]
        )

        leaderboard_rows = [
            (users[2].email, dc.name, 990, 1),
            (users[0].email, marvel.name, 980, 2),
            (users[3].email, dc.name, 940, 3),
            (users[1].email, marvel.name, 920, 4),
        ]
        for user_email, team_name, score, rank in leaderboard_rows:
            Leaderboard.objects.create(user_email=user_email, team_name=team_name, score=score, rank=rank)

        self.stdout.write(self.style.SUCCESS('octofit_db 테스트 데이터 적재 완료'))
