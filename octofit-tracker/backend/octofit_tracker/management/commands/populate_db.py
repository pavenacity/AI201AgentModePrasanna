from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc.name),
        ]

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout', suggested_for='Marvel'),
            Workout.objects.create(name='Agility Training', description='Agility workout', suggested_for='DC'),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Boxing', duration=50, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=95, rank=1)
        Leaderboard.objects.create(user=users[3], score=85, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
