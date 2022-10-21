n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first= data[n-1]
second = data[n-2]

result = 0

count = (m//(k+1) * k) + (m%(k+1))

result += count * first
result += (m-count) * second


# while m != 0:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     result += second
#     m -= 1    

print(result)