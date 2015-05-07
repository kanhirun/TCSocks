class TCSocks(object):

  def profit(self, visitedCities, money, cost, time, competitors):
    totalProfit = 0
    currCity    = 0

    for nextCity in visitedCities:
      revenue    = money[nextCity]
      travelCost = cost[currCity][nextCity]
      localProfit = (revenue - travelCost)

      currCity     = nextCity
      totalProfit += localProfit

    return totalProfit


  def _listFromFormatString(self, s):
    numbers = s.split()
    return [int(number) for number in numbers]
