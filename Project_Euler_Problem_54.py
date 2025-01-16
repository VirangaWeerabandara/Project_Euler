import time
from collections import OrderedDict

start_time = time.time()


def order2(x):
    num_list = []
    for b in range(0, 10, 2):
        if str(x[b]).isdigit() == True:
            num_list.append(int(x[b]))
        elif str(x[b]).isalpha() == True:
            if ord(x[b]) == 84:
                num_list.append(10)
            elif ord(x[b]) == 74:
                num_list.append(11)
            elif ord(x[b]) == 81:
                num_list.append(12)
            elif ord(x[b]) == 75:
                num_list.append(13)
            elif ord(x[b]) == 65:
                num_list.append(14)
    num_list.sort()
    num_list = list(dict.fromkeys(num_list))
    return num_list[-1]


def order(x):
    order_list = []
    order_list1 = []
    for a in x:
        num_list = []
        letter_list = []
        new_num_list = []
        for b in range(0, 10, 2):
            if str(a[b]).isdigit() == True:
                num_list.append(a[b])
            elif str(a[b]).isalpha() == True:
                if ord(a[b]) == 84:
                    letter_list.append(a[b])
                    new_num_list.append(10)
                elif ord(a[b]) == 74:
                    letter_list.append(a[b])
                    new_num_list.append(11)
                elif ord(a[b]) == 81:
                    letter_list.append(a[b])
                    new_num_list.append(12)
                elif ord(a[b]) == 75:
                    letter_list.append(a[b])
                    new_num_list.append(13)
                elif ord(a[b]) == 65:
                    letter_list.append(a[b])
                    new_num_list.append(14)
        num_list.sort()
        for z in num_list:
            new_num_list.append(int(z))
        num_list.extend(letter_list)
        string = str("".join(map(str, num_list)))
        order_list.append(string)
        new_num_list.sort()
        new_num_list_e = list(dict.fromkeys(new_num_list))
        if new_num_list != new_num_list_e:
            for u in new_num_list_e:
                if new_num_list.count(u) == 1:
                    new_num_list.remove(u)
        order_list1.append(new_num_list[-1])
    return order_list, order_list1


def value_genarator(x, y):

    value_list = []
    for a in range(0, len(y)):
        y[a] = "".join(OrderedDict.fromkeys(y[a]))
    for b in range(0, len(x)):
        str_val = "".join(OrderedDict.fromkeys(x[b]))
        if x[b].isalpha() == True and len(str_val) == 5:
            value_list.append(10)
        elif len(y[b]) == 1 and x[b].isdigit() == True and len(x[b]) == 5:
            string11 = x[b]
            list1 = []
            for i in string11:
                list1.append(int(i))
            list1 = sorted(set(range(list1[0], list1[-1]))-set(list1))
            if list1 == []:
                value_list.append(9)
            else:
                value_list.append(6)
        elif len(str_val) == 2:
            list2 = list(x[b])
            if list2.count(str(str_val[0])) == 4 or list2.count(str(str_val[1])) == 4:
                value_list.append(8)
            elif list2.count(str(str_val[0])) == 2 or list2.count(str(str_val[1])) == 2:
                value_list.append(7)
        elif len(y[b]) == 1:
            value_list.append(6)
        elif x[b].isdigit() == True and len(str_val) == 5:
            string12 = x[b]
            list3 = []
            for n in string12:
                list3.append(int(n))
            list3 = sorted(set(range(list3[0], list3[-1]))-set(list3))
            if list3 == []:
                value_list.append(5)
            else:
                value_list.append(1)
        elif len(str_val) == 3:
            list4 = list(x[b])
            if list4.count(str_val[0]) == 3 or list4.count(str_val[1]) == 3 or list4.count(str_val[2]) == 3:
                value_list.append(4)
            elif (list4.count(str_val[0]) == 2 and list4.count(str_val[0]) == 2) or (list4.count(str_val[1]) == 2 and list4.count(str_val[2]) == 2) or (list4.count(str_val[0]) == 2 and list4.count(str_val[2]) == 2):
                value_list.append(3)
        elif len(str_val) == 4:
            value_list.append(2)
        elif len(str_val) == 5:
            value_list.append(1)
    return value_list


data = open("Project Euler Problem 54 Resorces.txt", "r").readlines()

player1_hands = []
player1_hands_cards = []
player2_hands = []
player2_hands_cards = []


for a in data:
    string = a.strip().replace(" ", "")
    player1_hands.append(string[0:10])
    player2_hands.append(string[10:20])

for b in player1_hands:
    string1 = ""
    for i in range(1, 10, 2):
        string1 += b[i]
    player1_hands_cards.append(string1)

for c in player2_hands:
    string2 = ""
    for n in range(1, 10, 2):
        string2 += c[n]
    player2_hands_cards.append(string2)


player1_hands_1 = order(player1_hands)[0]
player1_hands_2 = order(player1_hands)[1]
player2_hands_1 = order(player2_hands)[0]
player2_hands_2 = order(player2_hands)[1]


value_list_player1 = value_genarator(player1_hands_1, player1_hands_cards)
value_list_player2 = value_genarator(player2_hands_1, player2_hands_cards)


win_list = []
countv = 0
for x in range(0, len(value_list_player1)):
    v1 = value_list_player1[x]
    v2 = value_list_player2[x]
    num = v1 - v2
    if num < 0:
        win_list.append("player2")
    elif num > 0:
        win_list.append("player1")
    elif num == 0:
        num2 = player1_hands_2[x]-player2_hands_2[x]
        if num2 < 0:
            win_list.append("player2")
        elif num2 > 0:
            win_list.append("player1")
        elif num2 == 0:
            num11 = order2(player1_hands[x])
            num12 = order2(player2_hands[x])
            if num11 > num12:
                win_list.append("player1")
            elif num11 < num12:
                win_list.append("player2")

print("Player 1 wins {} hands".format(win_list.count("player1")))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
