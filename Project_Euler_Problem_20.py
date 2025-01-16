import time,math

start_time = time.time()

num = 100
number = math.factorial(int(num))

#print(number)

digit_list = []

n = 10

while number >= 1:
    p = number % n
    number = number//n
    digit_list.append(p)


print("Sum of the Digits of the 100! is: {}".format(sum(digit_list)))

end_time = time.time()

difference = end_time-start_time

print("programme took {} seconds calculate".format(difference))
