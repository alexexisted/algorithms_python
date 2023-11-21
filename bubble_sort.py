def bubble_sort(array):
    arr_len = len(array)    #get the length of array
    for i in range(arr_len):    #for each num in array
        for j in range(arr_len - i - 1):    #compare last num with next num in array
            if array[j] > array[j + 1]:     #if last num is greater than next num
                array[j], array[j + 1] = array[j + 1], array[j]     #swap last num with next num
    return array
