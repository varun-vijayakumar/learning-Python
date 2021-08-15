class Employee:
    clg_name = "ABC"

    def __init__(self):
        print("This is an employee")


class SME:
    clg_name = "XYZ"


class Faculty(Employee, SME):
    pass


class GuestFaculty(SME, Employee):
    pass


if __name__ == '__main__':
    faculty = Faculty()
    guestFaculty = GuestFaculty()
    print(f'{faculty.clg_name}')
    print(f'{guestFaculty.clg_name}')
