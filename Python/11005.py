data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fit, num = input().split()
fit = int(fit)
num = int(num)

temp = 0
while True:
    if num ** temp > fit:
        break
    temp += 1
result = ""
for i in range(temp - 1, -1, -1):
    result += data[fit // (num ** i)]
    fit = fit % (num ** i)
print(result)
