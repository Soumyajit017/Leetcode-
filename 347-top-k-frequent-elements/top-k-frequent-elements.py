class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #taking a hashset to take the freq of elements
        freq=[[]for i in range(len(nums)+1)] #a list of list with freq: key, value(elements of array) : value, list lenght: array +1 len
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n) #take the freq:key, value:elements, freq[3]:1,1 got 3 frequency
        res = [] #list to return the k elements
        for i in range(len(freq)-1,-1,-1): #descending order to get the most frequency elements first
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: #only return the k no elements, with freq
                    return res
          
