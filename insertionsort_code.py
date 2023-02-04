import time

def insertion_sort(data, drawData, delay):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drawData(data, ['yellow' if x == k or x == i else 'blue' for x in range(len(data))])
        time.sleep(delay)
        
    drawData(data, ['blue' for x in range(len(data))])