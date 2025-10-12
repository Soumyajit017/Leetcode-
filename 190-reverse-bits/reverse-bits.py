class Solution:
    def reverseBits(self, n: int) -> int:
       s = bin(n)[2:].zfill(32)
       s = s[::-1]
       return int(s,2)
       #bin(n) -> converts n to "ob1010" binary form,[2:] -> cuts off the "ob", .zfill(32) -> fill it up with leading zeros upto 32 bits
       # int(s,2) -> tells the interpreter that s is a binary-2 number 

