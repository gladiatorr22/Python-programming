class Solution():
    def solution(self, Arr, n):
        max_min_score = 0

        for i in range(1, n - 1):       # Split A and B
            for j in range(i + 1, n):   # Split B and C
                A = Arr[:i]
                B = Arr[i:j]
                C = Arr[j:]

                min_score = float('inf')
                for w1 in A:
                    for w2 in B:
                        for w3 in C:
                            score = abs(w1 - w2) + abs(w2 - w3)
                            min_score = min(min_score, score)

                max_min_score = max(max_min_score, min_score)

        return max_min_score
n=int(input("Enter the number of elements in the array: "))
Arr = list(map(int, input("Enter the elements of the array: ").split()))  
sol = Solution()
result = sol.solution(Arr, n)
print("The maximum of the minimum scores is:", result)