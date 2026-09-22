
import re
class Solution:
    def reverseWords(self, s: str) -> str:

        clean=re.findall(r'\b\w+\b', s)

        return " ".join(clean[::-1])