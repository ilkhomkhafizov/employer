from abc import ABC, abstractmethod


class IGenerator(ABC):

    @staticmethod
    @abstractmethod
    def get_data(self):
        """Get Generated Data with Faker"""
