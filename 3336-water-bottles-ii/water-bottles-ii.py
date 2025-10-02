class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink=0
        empty=0
        while numBottles>0:
            drink +=numBottles
            empty +=numBottles
            numBottles=0
            if empty>=numExchange:
                empty-=numExchange
                numBottles+=1
                numExchange+=1
        return drink
