from django.core.management.base import BaseCommand
from tracker_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=30)
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=25)

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add users to teams
        team1.members.append(user1.email)
        team1.save()
        team2.members.append(user2.email)
        team2.save()

        # Create test activities
        Activity.objects.create(user_email=user1.email, type="Running", duration=45, date="2025-04-08")
        Activity.objects.create(user_email=user2.email, type="Cycling", duration=60, date="2025-04-07")

        # Create test leaderboard entries
        Leaderboard.objects.create(user_email=user1.email, score=150)
        Leaderboard.objects.create(user_email=user2.email, score=200)

        # Create test workouts
        Workout.objects.create(user_email=user1.email, description="Morning Yoga", date="2025-04-06")
        Workout.objects.create(user_email=user2.email, description="Evening Cardio", date="2025-04-05")

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
