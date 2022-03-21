import argparse

class MyParser:
    def __init__(self):
        # body of the constructor
        parser = argparse.ArgumentParser(description='Process command line inputs.')
        parser.add_argument('-s', '--sal', type=str, default="DKSalaries.csv", help='name of input salary file')
        parser.add_argument('-l', '--line', type=str, default="lineups.csv", help='desired name of output lineup file')
        parser.add_argument('-t', '--type', type=str, default="classic", help='name of contest type (\"classic\" or \"showdown\" or \"tiers\")')
        self.args = parser.parse_args()

    def get_args():
        return self.args
