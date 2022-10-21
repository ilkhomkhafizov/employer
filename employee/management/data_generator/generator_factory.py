from employee.management.data_generator.department_generator import DepartmentGenerator


class GeneratorFactory:
    @staticmethod
    def generate(file_type: str, quality: int):
        """A static method to get a data"""
        if file_type == 'department':
            return DepartmentGenerator(quality)
        return False
