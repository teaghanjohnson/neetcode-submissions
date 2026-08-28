class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        #loop forward store in array
        #loop backward store in array
        # if arrays are identical palindrome
        forward = []
    
        for char in s:
            if char.isalnum():
                forward.append(char.lower())
        
        return forward == forward[::-1]
    
        