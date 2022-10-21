from faker import Faker

from employee.management.data_generator.interface_generator import IGenerator
import logging


class BankGenerator(IGenerator):
    """Генератор подразделений с помощью Faker"""

    def __init__(self, qual: int):
        self.logger = logging.getLogger(__class__.__name__)
        self.qual = qual  # Число подразделений
        self.fake = Faker()

    def get_data(self):
        data = []
        for _ in range(self.qual):
            data.append(self.fake.bban())
        self.logger.info(f"Bank data generated successfully")
        return data
