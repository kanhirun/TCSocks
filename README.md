# TCSocks
Single Round Match 207 Round 1 - Division I, Level Two

## Dependencies

`$ python runtests.py` does not support python <=2.6 due to `argparse`
dependency.


## Problem Statement

You wish to earn money selling cute socks from the TC store. You live in Glastonbury, but its citizens are all long-time TopCoders, so you can’t sell any socks there. Thus you are going to visit several other cities, find new TopCoders there, and sell them some socks. Unfortunately, several other TC members are also sock salesmen. If one or more sock salesmen visits a city before you, or at the same time as you, your profit in that city will be halved once for each of the other salesmen (because some people will buy his socks). Hence, if two people visit the city before you, you will only get one fourth of the potential profit. Also, traveling between cities is not free, so you may lose money if you visit too many cities. However, you have your competitors’ plans, so you know which cities they will visit, and in what order they will visit them. Now you are planning your route, and want to maximize your profit. 

You will be given a int[], money, which gives maximal possible earnings for each city. You will also be given a String[], costs, which contains the costs of getting from one city to another. A String[], times, gives you the number of days it takes to get from one city to another (you may assume that it takes no time to sell socks once you get to a city). Both costs and times will be formatted in the same way. If they both have K elements, then each element of costs and times will contain K integers, each separated by a single space. The j<sup>th</sup> integer in the ith element of times will represent the number of days it takes to get from city i to city j. Similarly, the j<sup>th</sup> integer in the i<sup>th</sup> element of costs will represent the cost of traveling from city i to city j. Also, a String[], competitors, gives you the routes of your competitors. Each element of competitors will be formatted as “N1 N2 … Nk”, where N1 N2 … Nk are the numbers of the cities a competitor will visit (so first he will go to the city N1, then to the city N2 and so on). 

Your method must plan the route that maximizes your profit. You will start in Glastonbury (city 0) and then visit any number of the cities (not visiting a particular city more than once), before finally returning to Glastonbury. All your competitors start their routes in Glastonbury at the same time as you, and they sell socks along the routes specified in competitors. It takes them the same amount of time to travel between cities as it takes you. Your method should return your maximum possible profit.
