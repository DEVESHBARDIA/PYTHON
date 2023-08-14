class Employee:
    def __init__(self, name, id, dept, salary):
        self.name = name
        self.empId = id
        self.dept = dept
        self.salary = salary

    def display(self):
        print("Employee Details")
        print("Name : ", self.name)
        print("ID : ", self.empId)
        print("Dept : ", self.dept)
        print("Salary : ", self.salary)

    def update(self,per):
        self.salary = self.salary + self.salary * (per/100)


n = int(input("Enter the number of Employees: "))
emp = []
for i in range(n):
    name = input("Enter name: ")
    id = input("Enter id: ")
    dept = input("Enter department: ")
    salary = int(input("Enter the salary: "))
    emp.append(Employee(name, id, dept, salary))

for i in range(n):
    emp[i].display()

dept = input("Enter the department to hike salary: ")
hike = int(input("Enter hike percent "))
for i in range(n):
    if dept == emp[i].dept:
        emp[i].update(hike)

for i in range(n):
    emp[i].display()



#4475