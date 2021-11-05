class Algorithhm:
    #insertion Sort
    def insertionSort(array):
        for i in range (1, len(array)):
            key = array[i]
            j = i-1
        while j >= 0 and key < array[j]:
                array [j + 1] = array[j]
                j -= 1
        array [j + 1] = key
    array = [23, 11, 73, 15, 6]
    insertionSort(array)
    for i in range(len(array)):
        print ("% d" % array[i])
    #merge sort
    # def mergeSort(array):
    #     if len(array) > 1:
    #        r = len(array)//2
    #        L = array [: r]
    #        M = array[r:]
    #        mergeSort(L)
    #        mergeSort(M)
    #        i = j = k = 0
    #     while i < len(L) and j < len(M):
    #         if L[i] < M[j]:
    #             array[k] = L[i]
    #             i += 1
    #         else:
    #             array[k] = M[j]
    #             j += 1
    #         k += 1
    #     while i < len(L):
    #         array[k] = L[i]
    #         i += 1
    #         k += 1
    #     while j < len(M):
    #         array[k] = M[j]
    #         j += 1
    #         k += 1
    # def printList(array):
    #     for i in range(len(array)):
    #         print(array[i], end=" ")
    # print ()
    # if __name__ == '__main__':
    #     array = [6, 5, 12, 10, 9, 1]

    #     mergeSort(array)

    #     print ("Sorted array is: ")
    #     printList(array)
    #quick Sort
    

    # def quick_sort (start, end, array):
    #     if (start < end):
    #         p = partition(start, end, array)
    #         quick_sort (start, p - 1, array)
    #         quick_sort (p + 1, end, array)
    # array = [ 10, 7, 8, 9, 1, 5]
    # quick_sort(0, len(array) - 1, array)
    # print (f'Sorted array: {array}')

    # def partition (start, end, array):
    #     pivot_index = start 
    #     pivot = array[pivot_index]
    #     while start < end: 
    #         while start < len(array) and array[start] <= pivot:
    #             start += 1
    #     while array[end] > pivot:
    #         end -= 1
    #     if (start < end):
    #         array[start], array[end] = array[end], array[start]
    #         array[end], array[pivot_index] = array[pivot_index], array[end]
    #         return end 

    # Bubble Sort
    def bubbleSort(array):
        for i in range(len(array)):
           for j in range (0, len(array) - i - 1):
            if array[j] > array [j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    data = [-2, 45, 0, 11, -9]
    bubbleSort(data)
    print ('Sorted Array in Ascending Order:')
    print(data)
    # Selection Ssort
    def selectionSort (array, size):   
        for step in range(size):
            min_idx = step
        for i in range (step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array [step], array[min_idx]) = (array[min_idx], array[step])
    data = [-1, 45, 0, 21, -9]
    size = len(data)
    selectionSort (data, size)
    print ('Sorted Array:')
    print(data)
    # Bucket Sort
    def bucketSort(array):
        bucket = []
        for i in range(len(array)):
            bucket. append ([])
        for j in array:
            index_b = int (10 * j)
            bucket[index_b]. append(j)
        for i in range(len(array)):
            bucket[i] = sorted(bucket[i])
        k = 0
        for i in range(len(array)):
            for j in range(len(bucket[i])):
                array[k] = bucket[i][j]
                k += 1
        return array
    array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted Array in descending order is")
    print(bucketSort(array))


