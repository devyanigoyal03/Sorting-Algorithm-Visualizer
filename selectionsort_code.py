import time

def selection_sort(data, drawData, delay):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, ["YELLOW" if x == minimum or x == i else 'blue' for x in range(len(data))] )
        time.sleep(delay)
        
    drawData(data, ['blue' for x in range(len(data))])

# 0 1 2 3 4 5 6
# 1 5 6 7 9 3 4