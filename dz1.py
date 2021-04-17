data = int(input(':'))
answ = 0
while True:
    if data % 2 == 0:
        data /= 2
        answ += 1
        continue
    else:
        break
print(answ)


