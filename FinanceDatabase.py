import financedatabase as fd
import pandas as pd


class Equities:
    def __init__(self, country: str = 'USA') -> None:
        self.country = country

    def __repr__(self):
        return f'Country: {self.country}'

    @staticmethod
    def countries():
        """
        Obtain ALL countries
        """
        return list(fd.Equities().options('country'))

    @staticmethod
    def sectors():
        """
        Obtain ALL Sectors
        """
        return list(fd.Equities().options('sector'))

    @staticmethod
    def industry_group():
        """
        Obtain ALL Industry Groups
        """
        return list(fd.Equities().options('industry_group'))

    @staticmethod
    def industry():
        """
        Obtain ALL Industries
        """
        return list(fd.Equities().options('industry'))

    @staticmethod
    def exchange():
        """
        Obtain ALL Exchanges
        """
        return list(fd.Equities().options('exchange'))

    def equities_country(self):
        return fd.Equities().search(country=self.country)

    @staticmethod
    def equities_exchange(exchange: str):
        return fd.Equities().search(exchange=exchange)


def main():
    eq = Equities(country='USA')
    nyse = eq.equities_exchange(exchange='NYSE')
    print(type(nyse))


if __name__ == '__main__':
    eq = Equities(country='United States')

    countries = eq.countries()
    # print(len(countries))

    sectors = eq.sectors()
    # print(len(sectors))

    industry = eq.industry()
    # print(len(industry))

    industry_groups = eq.industry_group()
    # print(len(industry_groups))

    exchanges = eq.exchange()
    # print(len(exchanges))

    LSE = eq.equities_exchange(exchange='LSE')

    USA = eq.equities_country()

    NYSE = eq.equities_exchange(exchange='NYQ')
