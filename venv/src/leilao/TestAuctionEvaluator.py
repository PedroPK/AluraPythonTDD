from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao, AuctionEvaluator


class TestAuctionEvaluator(TestCase):

    def test_evaluate_twoBids_withSmallerBidFirst(self):
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

    def test_evaluate_twoBids_withBiggerBidFirst(self):
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

    def test_evaluate_withOnlyOneBid(self):
        gui     =   Usuario("Guilherme")

        lance   =   Lance(gui, 150.0)

        leilao  =   Leilao("Celular")
        leilao.lances.append(lance)

        evaluator   =   AuctionEvaluator()
        evaluator.evaluate(leilao)

        self.assertEqual(150.0,     evaluator.smaller_bid )
        self.assertEqual(150.0,     evaluator.bigger_bid )

    def test_evaluate_withThreeBids_inGrowingOrder(self):
        gui     =   Usuario('Guilherme')
        yuri    =   Usuario('Yuri')
        vini    =   Usuario("Vinicius")

        lance_yuri  =   Lance(yuri, 100.0)
        lance_gui   =   Lance(gui, 150.0)
        lance_vini  =   Lance(vini, 200.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_yuri)
        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_vini)

        evaluator = AuctionEvaluator()
        evaluator.evaluate(leilao)

        menorExpected = 100.0
        maiorExperado = 200.0

        self.assertEqual(menorExpected, evaluator.smaller_bid)
        self.assertEqual(maiorExperado, evaluator.bigger_bid)

if __name__ == '__main__':
    unittest.main()
