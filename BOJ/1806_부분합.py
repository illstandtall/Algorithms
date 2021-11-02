import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
sums = nums[left]
res = sys.maxsize

while left <= right < n:
    if sums >= s:
        res = min(res, right-left+1)
        sums -= nums[left]
        left += 1
    else:
        right += 1
        if right != n:
            sums += nums[right]

if res == sys.maxsize:
    print(0)
else:
    print(res)
