# polymorphism without inheritance
class A:
    def display(self):
        return "A"


class B:
    def display(self):
        return "B"


# polymorphism with inheritance
class C(A):
    def display(self):
        return "C"


if __name__ == '__main__':
    a = A();
    b = B();
    c = C();
    print(f'{a.display()}')
    print(f'{b.display()}')
    print(f'{c.display()}')
