from random import randint
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from employee.management.data_generator.generator_factory import GeneratorFactory
from employee.models import Department, Employee

DEPARTMENTS = GeneratorFactory.generate('department', 20).get_data()
SUBDIVISIONS = GeneratorFactory.generate('department', 40).get_data()
SUBDIVISIONS_2 = GeneratorFactory.generate('department', 40).get_data()
SUBDIVISIONS_3 = GeneratorFactory.generate('department', 40).get_data()
SUBDIVISIONS_4 = GeneratorFactory.generate('department', 40).get_data()
SUBDIVISIONS_5 = GeneratorFactory.generate('department', 40).get_data()


class Provider(faker.providers.BaseProvider):

    def departments(self):
        return self.random_element(DEPARTMENTS)

    def subdivisions(self):
        return self.random_element(SUBDIVISIONS)

    def subdivisions_2(self):
        return self.random_element(SUBDIVISIONS_2)

    def subdivisions_3(self):
        return self.random_element(SUBDIVISIONS_3)

    def subdivisions_4(self):
        return self.random_element(SUBDIVISIONS_4)

    def subdivisions_5(self):
        return self.random_element(SUBDIVISIONS_5)


class Command(BaseCommand):
    help = "Create fake Department, subdivision and personal data"

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(Provider)

        # Save Department first level
        for _ in range(20):
            department_name = fake.unique.departments()
            department = Department.objects.create(name=department_name)

            for i in range(2):
                sub_1_text = fake.unique.subdivisions()
                sub_2_text = fake.unique.subdivisions_2()
                sub_3_text = fake.unique.subdivisions_3()
                sub_4_text = fake.unique.subdivisions_4()
                sub_5_text = fake.unique.subdivisions_5()
                sub_1 = Department.objects.create(name=sub_1_text, parent=department)
                sub_2 = Department.objects.create(name=sub_2_text, parent=sub_1)
                sub_3 = Department.objects.create(name=sub_3_text, parent=sub_2)
                sub_4 = Department.objects.create(name=sub_4_text, parent=sub_3)
                Department.objects.create(name=sub_5_text, parent=sub_4)
        employee_obj = [
            Employee(
                name=fake.name(),
                employment_position=fake.job(),
                employment_start_date=fake.date(),
                salary=randint(50000, 150000),
                department_id=randint(1, 220)
            )
            for _ in range(1, 51000)
        ]
        employee = Employee.objects.bulk_create(employee_obj)
        check_dep = Department.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number dep: {check_dep}"))
