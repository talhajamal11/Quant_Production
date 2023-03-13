import financedatabase as fd
import pandas as pd


class Equities:
    def __init__(self, country: str = 'USA') -> None:
        self.country = country

    def __repr__(self):
        return f'Country: {self.country}'

    def countries(self):
        """
        Obtain ALL countries
        """
        return list(fd.Equities().options('country'))

    def sectors(self):
        """
        Obtain ALL Sectors
        """
        return list(fd.Equities().options('sector'))

    def industry_group(self):
        """
        Obtain ALL Industry Groups
        """
        return list(fd.Equities().options('industry_group'))

    def industry(self):
        """
        Obtain ALL Industries
        """
        return list(fd.Equities().options('industry'))

    def exchange(self):
        """
        Obtain ALL Exchanges
        """
        return list(fd.Equities().options('exchange'))


if __name__ == '__main__':
    eq = Equities()
    eq


