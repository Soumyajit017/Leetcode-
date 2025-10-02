class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        empty = numBottles

        while empty >= numExchange:
            drink += empty // numExchange
            empty = (empty%numExchange) + (empty // numExchange)
        return drink