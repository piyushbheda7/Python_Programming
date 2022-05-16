# Create a class Employee and add salary and increment properties to it.
# Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 10000

    @property
    def SalaryAfterIncrement(self):
        return self.salary

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self , increment):
        self.salary += increment

emp = Employee()

print(emp.salary)

emp.SalaryAfterIncrement = 100000

print(emp.SalaryAfterIncrement)