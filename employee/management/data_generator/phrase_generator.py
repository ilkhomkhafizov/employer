from faker import Faker

from employee.management.data_generator.interface_generator import IGenerator
import logging


class PhraseGenerator(IGenerator):
    """Генератор подразделений с помощью Faker"""

    def __init__(self, qual: int):
        self.logger = logging.getLogger(__class__.__name__)
        self.qual = qual  # Число подразделений
        self.fake = Faker()

    def get_data(self):
        data = []
        for _ in range(self.qual):
            data.append(self.fake.catch_phrase())
        self.logger.info(f"Phrase data generated successfully")
        return data
