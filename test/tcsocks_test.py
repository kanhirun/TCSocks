import pytest
from unittest import TestCase

from tcsocks import TCSocks


class TestTCSocks(TestCase):

  def testGetProfit1(self):
    """
    You have no competitors. Your best path is 0 -> 2 -> 1 -> 0.
    You spend 50 + 10 + 0 units, and earn 200 units. So the total income is 140.
    """
    tcSocks     = TCSocks()
    state       = [0, 2, 1, 0]
    money       = [0, 100, 100, 100]

    cost        = [[0 , 50 , 50 , 200],
                   [0 , 0  , 50 , 200],
                   [0 , 10 , 0  , 200],
                   [0 , 0  , 0  , 0]]

    time        = [[0, 1, 1, 1],
                   [1, 0, 1, 1],
                   [1, 1, 0, 1],
                   [1, 1, 1, 0]]

    competitors = []
    expected    = 140

    profit = tcSocks.profit(state, money, cost, time, competitors)

    self.assertEqual(expected, profit)


  def testGetProfit2(self):
    tcSocks = TCSocks()
    state = [0, 1, 0]
    money = [0, 100, 100, 100]

    cost = [[0 , 50 , 50 , 200],
            [0 , 0  , 50 , 200],
            [0 , 10 , 0  , 200],
            [0 , 0  , 0  , 0]]

    time = [[0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]]

    competitors = [[3], [2, 3, 1], [2, 1]]

    results = tcSocks.profit(state, money, cost, time, competitors)

    self.assertEqual(50, results)
