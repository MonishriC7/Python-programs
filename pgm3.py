n = int(input())
nums = list(map(int, input().split()))

answer = []

for i in range(n):
    current_product = 1
    for j in range(n):
        if j != i:
            current_product *= nums[j]
    answer.append(current_product)

print(*answer)
