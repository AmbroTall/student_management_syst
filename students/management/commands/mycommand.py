from django.core.management.base import BaseCommand
from faker import Faker
from students.models import Student

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(10):
            student = Student(
                student_number=fake.random_number(digits=8),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                field_of_study=fake.random_element(elements=("Computer Science", "Mathematics", "Biology", "Psychology")),
                gpa=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            )
            student.save()
