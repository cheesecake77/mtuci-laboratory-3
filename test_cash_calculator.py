from main import CashCalculator
from main import Record

S
def test_get_today_cash_remained():
    cash = CashCalculator(500)
    cash.add_record(Record(100, 'сапоги'))
    cash.add_record(Record(100, 'шапка'))
    print(cash.get_today_cash_remained("usd"))
    res = cash.get_today_cash_remained("usd")
    assert res == 4.29
