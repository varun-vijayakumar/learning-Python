class Account:
    _number = 123
    __password = "pass"

    def get(self):
        return self.__password


if __name__ == '__main__':
    a = Account()
    print(f'{a._number}')
    # print(f'{a.__password()}') # error
    print(f'{a.get()}')
    print(f'{a._Account__password}')  # Names Mangling
