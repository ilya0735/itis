import pytest
from main import BankAccount

class TestMain:
    @pytest.fixture
    def empty_account(self):
        return BankAccount(balance=0)

    @pytest.fixture
    def account(self):
        return BankAccount(balance=11000)


    @pytest.mark.parametrize("deposit_amounts, expected", [
        [[1, 2, 3, 4], sum([1, 2, 3, 4])],
        [[0, 0, 0, 0], 0],
        [[1221343, 12523543, 123214, 3123183423], sum([1221343, 12523543, 123214, 3123183423])]
    ])
    def test_deposit(self, deposit_amounts, expected):
        empty_acc = BankAccount(balance=0)
        for amount in deposit_amounts:
            empty_acc.deposit(amount)
        assert empty_acc.balance == expected

    @pytest.mark.parametrize("withdraw_amounts, expected", [
        [[1, 2, 3, 4], 100 - sum([1, 2, 3, 4])],
        [[0, 0, 0, 0], 100],
        [[64, 30, 6], 0],
    ])
    def test_withdraw(self, withdraw_amounts, expected):
        acc = BankAccount(balance=100)
        for amount in withdraw_amounts:
            acc.withdraw(amount)
        assert acc.balance == expected

    def test_withdraw_invalid(self, empty_account):
        with pytest.raises(ValueError):
            empty_account.withdraw(100)

    def test_transfer(self, empty_account, account):
        account.transfer(empty_account, 1000)
        assert empty_account.balance == 1000
        assert account.balance == 10000
        empty_account.transfer(account, 1000)
        assert empty_account.balance == 0
        assert account.balance == 11000

    def test_transfer_invalid(self, empty_account, account):
        with pytest.raises(ValueError):
            empty_account.transfer(account, 1000)



