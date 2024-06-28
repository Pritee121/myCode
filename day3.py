# class Animal:
#     def __init__(self, name):
#         print("Constructor invoked")
#         self.name = name

#     def eat(self):
#         print(self.name)
#         print("I can eat")

#     def sleep(self):
#         print("I can sleep")
    
# class Dog(Animal):
#         def bark(self):
#             print("Woof")

# dog1 = Dog('German Shepherd')
# print(dog1.name)
# dog1.eat()
# dog1.sleep()

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_number = account_number
#         self._balance = balance

#     def _deposit(self,amount):
#         self._balance += amount
#         print(f"Deposit successful. New Balance : ${self._balance}")

#     def check_balance(self):
#         print(f"Current Balance:{self._balance}")

#     def withdraw(self,amount):
#         self._balance -= amount
#         print(f"withdraw successful. New Balance : ${self._balance}")

# account = BankAccount('1234', 1000)
# account._deposit(-100)
# account.withdraw(1500)
# account.check_balance()
# print(account._account_number)


# class Employee:
#     def __init__(self,name,emp_id,salary):
#         self._name = name
#         self._emp_id = emp_id
#         self._salary = salary
    
#     def calculate_bonus(self):
#         return self._salary * 0.1
    
#     def display_info(self):
#         print(f"Name:${self._name}")
#         print(f"Employee id:${self._emp_id}")
#         print(f"Salary:${self._salary}")
# employee = Employee('Bob',1,100)
# employee.display_info()
# bonus = employee.calculate_bonus()
# print(bonus)

# class Father:
#     def __init__(self,name):
#         self.name = name
    
#     def talk(self):
#         print(self.name)
#         print("I can talk")

# class child(Father):
#     def walk(self):
#         print("walk")

# class child2(Father):
#     def walk(self):
#         print("walk")


# child1 = child("Ram")
# child1.talk()
# child2 = child("Shyam")
# child2.talk()


class Employee:
    def __init__(self,name,emp_id):
        self._name = name
        self._emp_id = emp_id
       
    def display_info(self):
        print(f"Name:${self._name}")
        print(f"Employee id:${self._emp_id}")
       
class Manager(Employee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department = department
    def display_info(self):
        super().display_info()
        print(f'Department:{self.department}')

class Developer(Employee):
    def __init__(self,name,emp_id,programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang= programming_lang
    def display_info(self):
        super().display_info()
        print(f'Programming Language:{self.programming_lang}')
manager = Manager('Bob',1,'engineeering')
manager.display_info()
developer = Developer('Pritee',2,'JavaScript')
developer.display_info()

