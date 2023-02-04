import time

def partition(data, start, end, drawData, delay):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, drawData, delay):
    if start < end:
        pivot_position = partition(data, start, end, drawData, delay)
        quick_sort(data, start, pivot_position-1, drawData, delay)
        quick_sort(data, pivot_position+1, end, drawData, delay)

        drawData(data, ["PURPLE" if x >= start and x < pivot_position else "YELLOW" if x == pivot_position
                        else "pink" if x > pivot_position and x <=end else 'blue' for x in range(len(data))])
        time.sleep(delay)
        
    drawData(data, ['blue' for x in range(len(data))])