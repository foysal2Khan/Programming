k, n, w = map(int, input().split())
payable = 0

for x in range(w):
    payable += (x + 1) * k  # Add cost of each banana

need = max(0, payable - n)
print(need)
