class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            "I":"1",
            "V":"5",
            "X":"10",
            "L":"50",
            "C":"100",
            "D":"500",
            "M":"1000"
        }
        result = 0
        for index, x in enumerate(s):
            if x in ['I','X','C'] and index+1 < len(s):
                if x == 'I' and (s[index+1] == 'V' or s[index+1] == 'X'):
                    result -= int(num.get(x))
                elif x == 'X' and (s[index+1] == 'L' or s[index+1] == 'C'):
                    result -= int(num.get(x))
                elif x == 'C' and (s[index+1] == 'D' or s[index+1] == 'M'):
                    result -= int(num.get(x))
                else:
                    result += int(num.get(x))    
            else: 
                result += int(num.get(x))
        return result
