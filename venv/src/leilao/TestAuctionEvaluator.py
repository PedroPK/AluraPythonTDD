from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao, AuctionEvaluator


class TestAuctionEvaluator(TestCase):

    def setUp(self):
        self.gui = Usuario('Guilherme')
        self.yuri = Usuario('Yuri')
        self.vini = Usuario("Vinicius")

        self.lance_yuri = Lance(self.yuri, 100.0)
        self.lance_gui = Lance(self.gui, 150.0)
        self.lance_vini = Lance(self.vini, 200.0)

        self.leilao = Leilao('Celular')


    def test_evaluate_twoBids_withSmallerBidFirst(self):
        self.leilao.lances.append(self.lance_yuri)
        self.leilao.lances.append(self.lance_gui)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(self.leilao)

        menorExpected   =   100.0
        maiorExperado   =   150.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

    def test_evaluate_twoBids_withBiggerBidFirst(self):
        self.leilao.lances.append(self.lance_gui)
        self.leilao.lances.append(self.lance_yuri)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(self.leilao)

        menorExpected   =   100.0
        maiorExperado   =   150.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

    def test_evaluate_withOnlyOneBid(self):
        self.leilao.lances.append(self.lance_gui)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(self.leilao)

        self.assertEqual(150.0,     evaluator.smaller_bid )
        self.assertEqual(150.0,     evaluator.bigger_bid )

    def test_evaluate_withThreeBids_inGrowingOrder(self):
        self.leilao.lances.append(self.lance_yuri)
        self.leilao.lances.append(self.lance_gui)
        self.leilao.lances.append(self.lance_vini)

        evaluator = AuctionEvaluator()
        evaluator.evaluate(self.leilao)

        menorExpected = 100.0
        maiorExperado = 200.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

if __name__ == '__main__':
    unittest.main()
