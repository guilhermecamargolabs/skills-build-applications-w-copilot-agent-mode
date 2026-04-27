from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Team A")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=team)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.team.name, "Team A")

class TeamTests(APITestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team B")
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(team.name, "Team B")

class ActivityTests(APITestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team C")
        user = User.objects.create_user(username="user2", email="user2@example.com", password="pass", team=team)
        activity = Activity.objects.create(user=user, type="run", duration=30, distance=5.0)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(activity.type, "run")

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        team = Team.objects.create(name="Team D")
        user = User.objects.create_user(username="user3", email="user3@example.com", password="pass", team=team)
        workout = Workout.objects.create(user=user, description="Pushups")
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(workout.description, "Pushups")

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team E")
        user = User.objects.create_user(username="user4", email="user4@example.com", password="pass", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(leaderboard.points, 100)
