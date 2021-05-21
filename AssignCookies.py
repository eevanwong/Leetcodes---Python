# Runtime: 136 ms, faster than 69.06% of Python online submissions for Assign Cookies.
# Memory Usage: 14.8 MB, less than 73.58% of Python online submissions for Assign Cookies.

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        cookieptr = 0
        childptr = 0
        while childptr < len(g) and cookieptr < len(s):
            if s[cookieptr] >= g[childptr]:
                count += 1
                cookieptr += 1
                childptr += 1
            else:
                cookieptr += 1
        return(count)
    