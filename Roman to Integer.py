class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        output=0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        k=len(s)
        if len(s)>1:
            for i in range(len(s)-1):
                if d[s[i]]<d[s[i+1]]:
                    output=output-d[s[i]]
                else:
                    output=output+d[s[i]]
            output=output+d[s[i+1]]
        else:
            output=output+d[s[0]]
        return output