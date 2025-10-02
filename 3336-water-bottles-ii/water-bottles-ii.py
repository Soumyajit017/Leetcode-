class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        empty = 0
        while numBottles > 0:
            #drink all bottles

            drink +=numBottles
            empty +=numBottles
            numBottles = 0
            
            #try to exchange

            if empty >=numExchange:
                empty -=numExchange
                numBottles +=1
                numExchange +=1
        return drink
