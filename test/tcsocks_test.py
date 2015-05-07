import pytest
from unittest import TestCase

from tcsocks import TCSocks


class TestTCSocks(TestCase):
  def test1(self):
    tcSocks = TCSocks()
    money       = [0, 100, 100, 100]
    cost        = ["0 50 50 200", "0 0 50 200", "0 10 0 200", "0 0 0 0"]
    time        = ["0 1 1 1", "1 0 1 1", "1 1 0 1", "1 1 1 0"]
    competitors = []

    maxProfits = tcSocks.earnMoney(money, cost, time, competitors)

    self.assertEqual(140, maxProfits)
