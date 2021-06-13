class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def get_name(self):
        return self._name


class EmployeeManager(Employee):
    def __init__(self, name="", age=0, salary=0):
        super().__init__(name, age, salary)
        self._employee_lst = []
        self.eml_index = -1

    def add_employee(self, new_empl):
        self._employee_lst.append(new_empl)

    def __iter__(self):
        return self

    def __next__(self):
        if self.eml_index >= len(self._employee_lst) - 1:
            raise StopIteration()
        self.eml_index += 1
        return self._employee_lst[self.eml_index].get_name()


manager = EmployeeManager()
manager.add_employee(Employee("Lia Levi", 30, 5000))
manager.add_employee(Employee("Yosef Cohen", 32, 4800))
manager.add_employee(Employee("Oded Haim", 47, 5100))
manager.add_employee(Employee("y",78,9))
yair = EmployeeManager("Yair", 5, 7)
print(yair.get_name())
yair.add_employee(Employee("Haim", 47, 5100))
for emp_name in manager:
    print(emp_name)