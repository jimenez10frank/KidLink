from django.core.management.base import BaseCommand
from administration.models import Youth, Activity, YouthActivity, Institute, YouthInstitute
from faker import Faker
import random
from datetime import datetime, timedelta

# THIS IS A SEEDER, YOU CAN RUN IT USING THE COMMAND:
# python manage.py seed_data
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Clear old data (optional)
        YouthActivity.objects.all().delete()
        YouthInstitute.objects.all().delete()
        Youth.objects.all().delete()
        Activity.objects.all().delete()
        Institute.objects.all().delete()

        # Create Institutes
        institutes = []
        for _ in range(5):
            institute = Institute.objects.create(
                institute_name=fake.company(),
                type=random.choice(['School', 'College', 'Training Center']),
                address=fake.address(),
                contact_person=fake.name(),
                phone=fake.random_number(digits=10, fix_len=True),
                email=fake.email()
            )
            institutes.append(institute)

        # Create Activities
        activities = []
        for _ in range(10):
            activity = Activity.objects.create(
                activity_name=fake.word().capitalize() + " Program",
                description=fake.text(),
                start_date=fake.date_between(start_date='-1y', end_date='today'),
                end_date=fake.date_between(start_date='today', end_date='+1y'),
                location=fake.city()
            )
            activities.append(activity)

        # Create Youth
        youths = []
        for _ in range(20):
            youth = Youth.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=18),
                gender=random.choice(['Male', 'Female']),
                status=random.choice(['Active', 'Inactive']),
                registration_due=fake.date_between(start_date='-1y', end_date='+1y')
            )
            youths.append(youth)

            # Assign Institute to Youth
            YouthInstitute.objects.create(
                youth=youth,
                institute=random.choice(institutes),
                status=random.choice(['active', 'inactive', 'pending'])
            )

            # Assign Activities to Youth
            selected_activities = random.sample(activities, k=random.randint(1, 5))
            for act in selected_activities:
                YouthActivity.objects.create(
                    youth=youth,
                    activity=act,
                    notes=fake.sentence(),
                    result=random.choice(['Passed', 'Pending', 'Failed'])
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
