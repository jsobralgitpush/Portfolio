from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    CARGA_TRABALHO = 8

    def __init__(self):
        print("Profissional criado com sucesso")

    @classmethod
    def set_employee(cls, code, name, salary):
        cls.code = code
        cls.name = name
        cls.salary = salary

    @staticmethod
    def get_hours():
        return Employee.CARGA_TRABALHO

    def calc_bonus(self):
        return self.salary * 0.15



class Manager(Employee):
    def __init__(self, code, name, salary):
        Employee.set_employee(code,name,salary)
        self.__departament = Department("managers", 1)

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, new_dep):
        self.__departament = new_dep
        return self.__departament



class Seller(Manager):
    def __init__(self, code, name, salary):
        Employee.set_employee(code,name,salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, soma):
        self.__sales = self.__sales + soma
        return self.__sales

    def get_departament(self):
        return self.__departament.name

