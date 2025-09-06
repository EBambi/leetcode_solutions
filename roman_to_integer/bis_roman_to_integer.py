class Solution(object):
     def romanToInt(self, s):
        sum = 0
        prevValue = 0
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for c in s:
            currentValue = value[c]
            sum += (currentValue - 2 * prevValue) if (currentValue > prevValue) else currentValue
            prevValue = currentValue
        return sum
