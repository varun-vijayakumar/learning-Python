class Employee:
    clg_name = "ABC"

    def __init__(self, id):
        self.id = id

    def getId(self):
        return self.id


class HR(Employee):
    pass


class Faculty(Employee):
    pass


class Admin(Employee):
    pass


if __name__ == '__main__':
    f = Faculty(100)
    h = HR(101)
    a = Admin(102)
    print(f'{f.getId()}')
    print(f'{h.getId()}')
    print(f'{a.getId()}')
