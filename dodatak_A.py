import getpass
from math import nan
import bcrypt

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if self.b == 0:
            return nan
        return self.a / self.b

    def toFloat(x):
        try:
            result = float(x)
            return result
        except:
            return nan


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    bytePassword = password.encode('utf-8')
    #salt = bcrypt.gensalt()
    salt = b'$2b$12$UxzsjL/TQ4BAhiC6U6fyku'
    hashedPassword = b'$2b$12$UxzsjL/TQ4BAhiC6U6fykuNiV.nV0d0PrpQRe8hDkAopCn1Km7X8e'
    if user != "root" or bcrypt.hashpw(bytePassword, salt) != hashedPassword:
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())

