def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    
    return array

print(bubble_sort([5,54,87,3,9,47,12,65,92,45,78,2]))