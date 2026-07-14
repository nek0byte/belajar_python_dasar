class BankAccount:
    def __init__(self, no: str, balance: float = 0) -> None:
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            # gunakan kata kunci "raise" untuk memanggil error massage
            raise ValueError("Saldo tidak cukup")
        self.balance -= amount


try:
    account1 = BankAccount("123", 10000)
    account1.transfer(1000000)
except ValueError as e:
    print(f"Error: {e}")


# ============================
# Custom Exception
"""
Exception adalah error yang terjadi saat program berjalan,
bisa ditangkap (try/except) agar program tidak crash.

Custom Exception adalah exception buatan sendiri yang diturunkan
dari class Exception, berguna untuk membuat error yang lebih
spesifik sesuai konteks aplikasi.
"""


class BalanceNotEnough(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class BankAccount2:
    def __init__(self, no: str, balance: float = 0) -> None:
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough(
                f"Saldo tidak cukup ( punya: {self.balance}, tarik: {amount} )"
            )
        self.balance -= amount


try:
    account2 = BankAccount2("456", 10000)
    account2.transfer(1000000)
except BalanceNotEnough as e:
    print(f"Custom Error: {e}")
