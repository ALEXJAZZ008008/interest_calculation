import copy
from decimal import Decimal, ROUND_HALF_UP
from datetime import date, timedelta


class Deposit(object):
    def __init__(self, deposited_amount, deposit_date, deposited_currency):
        self.deposited_amount = deposited_amount
        self.deposit_date = deposit_date
        self.deposited_currency = deposited_currency

        self.accrued_interest = Decimal("0.00")

        return


class InterestRate(object):
    def __init__(self, current_interest_rates, current_interest_boundaries, current_interest_start_date,
                 current_interest_end_date, current_interest_currency):
        self.current_interest_rates = current_interest_rates
        self.current_interest_boundaries = current_interest_boundaries

        self.current_interest_start_date = current_interest_start_date
        self.current_interest_end_date = current_interest_end_date

        self.current_interest_currency = current_interest_currency

        return


def interest_rates(end_date):
    current_interest_rates = []

    current_interest_rates.insert(0, InterestRate(current_interest_rates=[Decimal("0.05")],
                                                  current_interest_boundaries=[[Decimal("0.00"),
                                                                                Decimal("Infinity")]],
                                                  current_interest_start_date=date(year=2025, month=3, day=30),
                                                  current_interest_end_date=end_date,
                                                  current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.10")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2024, month=12, day=30),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2022, month=12, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.001")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2016, month=12, day=30),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.01")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2016, month=1, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.03")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2015, month=6, day=30),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.05")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2014, month=10, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.10")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2013, month=12, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.15")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2013, month=2, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2012, month=4, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.35")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2010, month=2, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.50")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2009, month=5, day=18),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.75")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2009, month=1, day=22),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.00")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2006, month=12, day=27),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.75")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2005, month=1, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.750"), Decimal("1.000")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2004, month=2, day=5),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.750"), Decimal("1.000"), Decimal("1.250")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2003, month=10, day=15),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("0.750"), Decimal("1.125"), Decimal("1.250")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2003, month=6, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.000"), Decimal("1.125"), Decimal("1.250")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2003, month=2, day=27),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.00"), Decimal("1.25"), Decimal("1.50")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2003, month=1, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.00"), Decimal("1.25"), Decimal("1.50")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("5000.00")],
                                                     [Decimal("5000.00"), Decimal("25000.00")],
                                                     [Decimal("25000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2002, month=1, day=15),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="EUR"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.00"), Decimal("1.25"), Decimal("1.75")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2001, month=9, day=17),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.25"), Decimal("1.50"), Decimal("2.00")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2001, month=7, day=20),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.25"), Decimal("1.75"), Decimal("2.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2001, month=5, day=16),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.50"), Decimal("2.00"), Decimal("2.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("50000.00")],
                                                     [Decimal("50000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=2000, month=6, day=30),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.25"), Decimal("1.75")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1999, month=12, day=15),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1999, month=5, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.50")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1999, month=2, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("1.50"), Decimal("2.00")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("10000.00")],
                                                     [Decimal("10000.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1997, month=5, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("2.00")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1993, month=8, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("2.25")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1993, month=5, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    current_interest_rates.insert(
        0, InterestRate(current_interest_rates=[Decimal("2.50")],
                        current_interest_boundaries=[[Decimal("0.00"), Decimal("Infinity")]],
                        current_interest_start_date=date(year=1993, month=1, day=1),
                        current_interest_end_date=current_interest_rates[0].current_interest_start_date,
                        current_interest_currency="DEM"))

    return current_interest_rates


def convert_eur_to_dem(eur):
    dem = eur * Decimal("1.95583")

    return dem


def convert_dem_to_eur(dem):
    eur = dem / Decimal("1.95583")

    return eur


def calculate_daily_interest(current_amount, current_interest_rates):
    updated_current_amount = copy.deepcopy(current_amount)

    for i in range(len(current_interest_rates)):
        if (current_interest_rates[i].current_interest_start_date <= updated_current_amount.deposit_date <
                current_interest_rates[i].current_interest_end_date):
            if updated_current_amount.deposited_currency == "DEM":
                if current_interest_rates[i].current_interest_currency == "EUR":
                    updated_current_amount.deposited_amount = (
                        convert_dem_to_eur(updated_current_amount.deposited_amount))
                    updated_current_amount.accrued_interest = (
                        convert_dem_to_eur(updated_current_amount.accrued_interest))

                    updated_current_amount.deposited_currency = "EUR"
            else:
                if current_interest_rates[i].current_interest_currency == "DEM":
                    updated_current_amount.deposited_amount = (
                        convert_eur_to_dem(updated_current_amount.deposited_amount))
                    updated_current_amount.accrued_interest = (
                        convert_eur_to_dem(updated_current_amount.accrued_interest))

                    updated_current_amount.deposited_currency = "DEM"

            for j in range(len(current_interest_rates[i].current_interest_rates)):
                if (current_interest_rates[i].current_interest_boundaries[j][0] <=
                        updated_current_amount.deposited_amount <
                        current_interest_rates[i].current_interest_boundaries[j][1]):
                    updated_current_amount.accrued_interest = (
                            updated_current_amount.accrued_interest +
                            (updated_current_amount.deposited_amount *
                             ((current_interest_rates[i].current_interest_rates[j] / Decimal("100")) /
                              Decimal((date(updated_current_amount.deposit_date.year + 1, 1, 1) -
                                       date(updated_current_amount.deposit_date.year, 1, 1)).days))))

                    break

            break

    return updated_current_amount


def accrue_interest(current_amount):
    updated_current_amount = copy.deepcopy(current_amount)

    updated_current_amount.deposited_amount = (updated_current_amount.deposited_amount +
                                               updated_current_amount.accrued_interest)
    updated_current_amount.accrued_interest = Decimal("0.00")

    return updated_current_amount

def output_currency(unquantised_currency):
    quantised_currency = unquantised_currency.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return quantised_currency


def calculate_interest(deposit, end_date):
    initial_amount = copy.deepcopy(deposit)
    current_amount = copy.deepcopy(initial_amount)
    current_year_end_amount = copy.deepcopy(current_amount)

    current_interest_rates = interest_rates(end_date)

    if initial_amount.deposited_currency == "DEM":
        print(f"Initial amount: {output_currency(convert_dem_to_eur(initial_amount.deposited_amount)):>9} Euro")
    else:
        print(f"Initial amount: {output_currency(initial_amount.deposited_amount):>9} Euro")

    print(f"")

    while current_amount.deposit_date <= end_date:
        current_amount = calculate_daily_interest(current_amount, current_interest_rates)

        if current_amount.deposit_date.month == 12 and current_amount.deposit_date.day == 31:
            current_amount = accrue_interest(current_amount)

            if current_amount.deposited_currency == "DEM":
                current_amount_euros = convert_dem_to_eur(current_amount.deposited_amount)

                if current_year_end_amount.deposited_currency == "DEM":
                    print(f"{current_amount.deposit_date.year}: {output_currency(current_amount_euros):>9} Euro, {output_currency(current_amount_euros - convert_dem_to_eur(current_year_end_amount.deposited_amount)):>6} Euro change")
                else:
                    print(f"{current_amount.deposit_date.year}: {output_currency(current_amount_euros):>9} Euro, {output_currency(current_amount_euros - current_year_end_amount.deposited_amount):>6} Euro change")
            else:
                if current_year_end_amount.deposited_currency == "DEM":
                    print(f"{current_amount.deposit_date.year}: {output_currency(current_amount.deposited_amount):>9} Euro, {output_currency(current_amount.deposited_amount - convert_dem_to_eur(current_year_end_amount.deposited_amount)):>6} Euro change")
                else:
                    print(f"{current_amount.deposit_date.year}: {output_currency(current_amount.deposited_amount):>9} Euro, {output_currency(current_amount.deposited_amount - current_year_end_amount.deposited_amount):>6} Euro change")

            current_year_end_amount = copy.deepcopy(current_amount)

        current_amount.deposit_date = current_amount.deposit_date + timedelta(days=1)

    current_amount = accrue_interest(current_amount)

    print(f"")

    if current_amount.deposited_currency == "DEM":
        current_amount_euros = convert_dem_to_eur(current_amount.deposited_amount)

        if initial_amount.deposited_currency == "DEM":
            print(f"End amount: {output_currency(current_amount_euros):>9} Euro, {output_currency(current_amount_euros - convert_dem_to_eur(initial_amount.deposited_amount)):>6} Euro change")
        else:
            print(f"End amount: {output_currency(current_amount_euros):>9} Euro, {output_currency(current_amount_euros - initial_amount.deposited_amount):>6} Euro change")
    else:
        if initial_amount.deposited_currency == "DEM":
            print(f"End amount: {output_currency(current_amount.deposited_amount):>9} Euro, {output_currency(current_amount.deposited_amount - convert_dem_to_eur(initial_amount.deposited_amount)):>6} Euro change")
        else:
            print(f"End amount: {output_currency(current_amount.deposited_amount):>9} Euro, {output_currency(current_amount.deposited_amount - initial_amount.deposited_amount):>6} Euro change")

    print(f"")
    print(f"")

    return current_amount


def main():
    calculate_interest(Deposit(deposited_amount=Decimal("1000.00"), deposit_date=date(year=1993, month=1, day=1),
                               deposited_currency="DEM"),
                       end_date=date(year=2026, month=12, day=31))

    return True


if __name__ == "__main__":
    main()
