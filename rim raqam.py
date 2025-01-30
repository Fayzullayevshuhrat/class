class Solution:
    @staticmethod
    def rim_to_arab(rim):
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for char in rim:
            if char not in d:
                raise ValueError(f"Invalid Roman numeral character: {char}")
        
        ans = 0
        for i in range(len(rim) - 1):
            if d[rim[i]] < d[rim[i + 1]]:
                ans -= d[rim[i]]
            else:
                ans += d[rim[i]]

        ans += d[rim[-1]]
        return ans


print(Solution.rim_to_arab("CCCCM"))
