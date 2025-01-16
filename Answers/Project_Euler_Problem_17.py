import time


start_time = time.time()


number_in_word_list1 = [3, 3, 5, 4, 4, 3, 5, 5, 4]
number_in_word_list2 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
number_in_word_list3 = [6, 6, 5, 5, 5, 7, 6, 6]
number_in_word_list4 = [10, 10, 12, 11, 11, 10, 12, 12, 11]

count1 = sum(number_in_word_list1)
# print(count1)
count2 = sum(number_in_word_list2)
# print(count2)
count3 = 0

and_count = 3*99*9

for i in number_in_word_list3:
    for n in number_in_word_list1:
        count3 = count3+i+n



count_of_ninety_number = count1+count2+count3 +sum(number_in_word_list3)


# print(count_of_one_hundred_number)

total_count = count_of_ninety_number * 10 + sum(number_in_word_list4)*100 + and_count + 11 

print("Letters used in 1 to 1000 is: {}".format(total_count))

finish_time = time.time()

difference = finish_time - start_time

print("this programme took {} seconds to finish".format(difference))
