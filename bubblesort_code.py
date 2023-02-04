import time

def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])



# 0 1 2 3 4 5 6
# 1 5 6 7 9 3 4

#PASSES : 6
# 1 5 6 7 3 4 9
# 1 5 6 3 4 7 9
# 1 5 3 4 6 7 9
# 1 3 4 5 6 7 9
# 1 3 4 5 6 7 9
# 1 3 4 5 6 7 9