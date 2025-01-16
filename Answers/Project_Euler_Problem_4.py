import time

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    return digit_list


def is_palindrome(n):

    digit_list = digits(n)
    digit_list1 = [i for i in reversed(digit_list)]
    if digit_list == digit_list1:
        return True
    else:
        return False


palindrome_number_list = []
multiple_list1 = []
multiple_list2 = []

for i in range(999, 99, -1):
    for k in range(999, 99, -1):
        n = k*i
        new_bool = is_palindrome(n)
        # print(n)

        if new_bool == True:
            palindrome_number_list.append(n)
            multiple_list1.append(i)
            multiple_list2.append(k)

max_palindrome_number = palindrome_number_list.index(
    max(palindrome_number_list))

number = max(palindrome_number_list)
multiple1 = multiple_list1[max_palindrome_number]
multiple2 = multiple_list2[max_palindrome_number]


print("The Largest Palindrome made from the products of two 3 digit numbers is {} which is {} x {} = {}".format(
    number, multiple1, multiple2, number))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
