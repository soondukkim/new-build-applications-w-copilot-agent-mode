from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, Leaderboard, Team, User, Workout


class CollectionSupportTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        Team.objects.create(name='marvel team', motto='Avengers Assemble')
        Team.objects.create(name='dc team', motto='Justice League United')

        User.objects.create(
            name='Iron Man',
            email='ironman@marvel.com',
            team_name='marvel team',
            total_points=980,
        )

        Activity.objects.create(
            user_email='ironman@marvel.com',
            activity_type='Running',
            duration_minutes=45,
            calories_burned=420,
        )

        Leaderboard.objects.create(
            user_email='ironman@marvel.com',
            team_name='marvel team',
            score=980,
            rank=1,
        )

        Workout.objects.create(
            user_email='ironman@marvel.com',
            title='Repulsor Core HIIT',
            difficulty='Hard',
            recommended_minutes=35,
        )

    def test_collections_have_data(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(Workout.objects.count(), 1)

    def test_api_endpoints_for_all_collections(self):
        endpoints = [
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]

        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200, msg=f'failed endpoint: {endpoint}')
            self.assertIsInstance(response.json(), list)

    def test_user_serializer_objectid_is_string(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload)
        self.assertIsInstance(payload[0]['id'], str)
