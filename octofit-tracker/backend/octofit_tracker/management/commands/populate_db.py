from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpa dados existentes
        User = get_user_model()
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Cria times
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Cria usuários (heróis)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        # Cria atividades
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=hulk, type='swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=superman, type='fly', duration=15, distance=100)

        # Cria workouts
        octo_models.Workout.objects.create(user=ironman, description='Treino de resistência')
        octo_models.Workout.objects.create(user=batman, description='Treino de força')

        # Cria leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=batman, points=90)
        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
