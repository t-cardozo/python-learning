# double price money weekend bonanza

prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize*2)

print(dbl_prizes)

#Comprehensions method
dbl_prizes = [prize*2 for prize in prizes] 

print(dbl_prizes)
