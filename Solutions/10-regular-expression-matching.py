# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# Difficulty: Hard
# Status: Partial solution — passes 277/354 test cases
# Note: fails on complex overlapping wildcards; full solution requires DP or recursion

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        q = ""
        l = []
        for x in s:
            l.append(x)
        for x in p[::-1]:
            q = q + x
        skip_next = False
        for x in range(len(p)):
            if skip_next:
                skip_next = False
                continue
            elif q[x] == "*":
                if q[x+1] == ".":
                    skip_next = True
                    while l:
                        l.pop()
                elif q[x+1:]:
                    skip_next = True
                else:
                    q = ""
                if q and q[x+1] and q[x+1] in l:
                    while q[x+1] in l:
                        l.remove(q[x+1])
            elif q[x] == "." and l:
                l.pop()
            else:
                if q[x] in l:
                    l.remove(q[x])
                else:
                    return False
        if l == []:
            return True
        else:
            return False