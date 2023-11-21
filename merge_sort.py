def merge_sort(array):
    if len(array) > 1:      #if len(array) is greater than 1, do the recursion
        mid = len(array) // 2       #divide the array into two halves
        left_half = array[:mid]     #found the left half of the array
        right_half = array[mid:]    #found the right half of the array
        merge_sort(left_half)       #recursively sort the left half
        merge_sort(right_half)      #recursively sort the right half

        #indexes are equal to zero
        left_ind = 0
        right_ind = 0
        array_ind = 0

        while left_ind < len(left_half) and right_ind < len(right_half):    #while left index is in left half and right index is in right half
            if left_half[left_ind] <= right_half[right_ind]:   #if left index is less than right index, then put left index in array
                array[array_ind] = left_half[left_ind] #put left index in array
                left_ind += 1 #increment left index
            else: #if right index is greater than right index
                array[array_ind] = right_half[right_ind] #put right index in array
                right_ind += 1 #increment right index
            array_ind += 1 #increment array index

        while left_ind < len(left_half): #while left index is in left half
            array[array_ind] = left_half[left_ind] #put left index in array
            left_ind += 1
            array_ind += 1

        while right_ind < len(right_half): #while right index is in right half
            array[array_ind] = right_half[right_ind] #put right index in array
            right_ind += 1
            array_ind += 1

    return array

