from employee.management.data_generator.department_generator import DepartmentGenerator
from employee.management.data_generator.automotive_generator import AutomotiveGenerator
from employee.management.data_generator.city_generator import CityGenerator
from employee.management.data_generator.address_generator import AddressGenerator
from employee.management.data_generator.bank_generator import BankGenerator
from employee.management.data_generator.phrase_generator import PhraseGenerator


class GeneratorFactory:
    @staticmethod
    def generate(file_type: str, quality: int):
        """A static method to get a data"""
        if file_type == 'department':
            return DepartmentGenerator(quality)
        if file_type == 'city':
            return CityGenerator(quality)
        if file_type == 'address':
            return AddressGenerator(quality)
        if file_type == 'bank':
            return BankGenerator(quality)
        if file_type == 'phrase':
            return PhraseGenerator(quality)
        if file_type == 'automotive':
            return AutomotiveGenerator(quality)
        return False
