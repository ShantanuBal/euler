import datetime
start = datetime.datetime.now()

sum_squares = 0
square_sums = 0

for each in range(1,101):
    sum_squares += pow(each,2)
    square_sums += each
square_sums = pow(square_sums,2)

end = datetime.datetime.now()
print square_sums - sum_squares
print end - start
