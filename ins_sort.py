def insertion_sort(array):
    for i in range(1, len(array)):      #for each num in array
        value = array[i]      #get the value of num
        while i > 0 and array[i - 1] > value:       #while i is not first and i-1 is grater than value
            array[i] = array[i - 1]     # swap num with last num
            i -= 1      #decrement i
        array[i] = value    #put num in array
    return array
