def binary_search(array, target):
    first = 0   #first number in the array
    last = len(array) - 1   #last number is equal to length of array minus 1
    while last >= first:     #while we are in array
        mid = (first + last) // 2   #middle number is equal to first + last // 2
        if array[mid] == target:    #if num in array[mid] is equal to target
            return True     #we found our target in array
        else:   #if we have not found our target in array
            if target < array[mid]:     #check if target is less than num in array[mid]
                last = mid - 1      #if target is less, then last is decreased by 1
            else:
                first = mid + 1     #if target is greater, then first is increased by 1
    return False    #if we did not find our target in array return False

