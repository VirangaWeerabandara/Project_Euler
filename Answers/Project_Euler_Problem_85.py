import time

start_time = time.time()


def rectangles_count(x, y):
    total_rectangles = x*y*(x+1)*(y+1)/4
    return total_rectangles


number = 2000000
n = 2000
m = 1


grid_list = []

while n >= m:
    rectangles = rectangles_count(n, m)
    if rectangles > number:
        n -= 1
    elif rectangles < number:
        grid_list.append([rectangles, n, m])
        m += 1

grid_list.sort()
print("Area of the grid closest to 2,000,000 is {} whitch has {} rectangles".format(
    grid_list[-1][1]*grid_list[-1][2], int(grid_list[-1][0])))

end_time = time.time()

difference = end_time-start_time

print("Code took {} seconds to execute".format(difference))
