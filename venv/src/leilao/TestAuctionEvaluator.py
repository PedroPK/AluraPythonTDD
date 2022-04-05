from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao, AuctionEvaluator


class TestAuctionEvaluator(TestCase):

    def test_evaluate_smallerBidFirst(self):
        gui     =   Usuario('Guilherme')
        yuri    =   Usuario('Yuri')

        lance_yuri      =   Lance(yuri, 100.0)
        lance_gui       =   Lance(gui,  150.0)

        leilao  =   Leilao('Celular')
        leilao.lances.append(lance_yuri)
        leilao.lances.append(lance_gui)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(leilao)

        menorExpected   =   100.0
        maiorExperado   =   150.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

    def test_evaluate_biggerBidFirst(self):
        gui     =   Usuario('Guilherme')
        yuri    =   Usuario('Yuri')

        lance_gui       =   Lance(gui,  150.0)
        lance_yuri      =   Lance(yuri, 100.0)

        leilao  =   Leilao('Celular')
        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_yuri)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(leilao)

        menorExpected   =   100.0
        maiorExperado   =   150.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

if __name__ == '__main__':
    unittest.main()
