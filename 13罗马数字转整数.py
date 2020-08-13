class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} 
        value1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        z = 0
        for i,j in value.items():
            if s:
                if i in s:
                    z += s.count(i)*j
                    s=s.replace(i,'')
            else:
                return z
        for i1,j1 in value1.items():
            if s:
                if i1 in s:
                    z += s.count(i1)*j1
                    s=s.replace(i1,'')
            else:
                return z
        return z
print(Solution().romanToInt('IX'))
