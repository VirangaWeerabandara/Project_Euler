import time

start_time = time.time()


string = ""
i = 1

while len(string) < 1000000:
    string += str(i)
    i += 1

answer = int(string[0])*int(string[9])*int(string[99])*int(string[999]
                                                           )*int(string[9999])*int(string[99999])*int(string[999999])

print("Value of the given expression is {}".format(answer))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
