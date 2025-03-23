 class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        reverse = 0
        while (a>0):
            reverse = reverse * 10 + a%10
            a//=10
        return  reverse == x
