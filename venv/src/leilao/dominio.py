import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances


class AuctionEvaluator:

    def __init__(self):
        self.bigger_bid = sys.float_info.min
        self.smaller_bid = sys.float_info.max

    def evaluate(self, pLeilao: Leilao):
        for bid in pLeilao.lances:

            if bid.valor > self.bigger_bid:
                self.bigger_bid = bid.valor

            if bid.valor < self.smaller_bid:
                self.smaller_bid = bid.valor
