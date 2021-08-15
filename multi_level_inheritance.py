class Employee:
    type = "Employee"

    def __init__(self):
        print("This is an employee")


class Faculty(Employee):
    type = "Faculty"

    def __init__(self):
        super().__init__()
        print("This is a Faculty")


class Hod(Faculty):
    type = "HOD"
    print("This is an Hod")


if __name__ == '__main__':
    hod = Hod();
    print(f'{hod.type}')
