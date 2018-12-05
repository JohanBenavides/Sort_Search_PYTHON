from random import randint

def insertion_sort(a):
    for i in range(1, len(a)):#select value to be moved
        x = a[i]
        index_hole = i#locate hole position for the value to be inserted

        while index_hole > 0 and a[index_hole - 1] > x:
            a[index_hole] = a[index_hole - 1]
            index_hole -= 1
        #insert the value at hole position
        a[index_hole] = x

def bubble_sort(a):
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1):#compare to adjacent elements
            if a[j] > a[j + 1]:#swap them
                swap = a[j]
                a[j] = a[j + 1]
                a[j + 1] = swap
                swapped = True

        if not swapped:#if no number was swapped, the array is sorted now
            break

def merge_sort(input_list):
    #array is already sorted
    if len(input_list) > 1:
        #split the lists into two sublists and recursively split sublists
        midpoint = int(len(input_list) / 2)
        left = merge_sort(input_list[:midpoint])
        right = merge_sort(input_list[midpoint:])
        #following the strategy Divide & Conquer
        return merge(left, right)

    else:
        return input_list

def merge(left,right):
    i,j = 0,0
    temp = []
    #iterate through both left and right sublist
    while i<len(left) and j<len(right):
        #if left value is lower than right then append it to the result
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            #if right value is lower than left then append it to the result
            temp.append(right[j])
            j += 1
    #concatenate the rest of the left and right sublists
    temp += left[i:]
    temp += right[j:]
    #return the result
    return temp

def quick_sort(a):
    if len(a) <= 1:#array A is already sorted
        return a
    else:#take first set element as a pivot
        pivot = a[0]
        less_subarray = []
        greater_subarray = []

        for i in range(1, len(a)):#build both less and greater than pivot sub-arrays
            if a[i] < pivot:
                less_subarray.append(a[i])
            else:
                greater_subarray.append(a[i])
        #call recursion for each one of the subarrays, and concatenate the results
        quick_sort(less_subarray)
        quick_sort(greater_subarray)
        #concatenate the results
        result = []
        result.extend(quick_sort(less_subarray))
        result.append(pivot)
        result.extend(quick_sort(greater_subarray))

    return result

def lineal_search(a,x):
    index = -1
    for i in range (0,len(a)):#compare with all the elements of the array
        if a[i]==x:
            index=i
            break
    return index

def binary_search (a, x):
    lowerBound = 0
    upperBoind = len(a) - 1
    index = -1

    while lowerBound < upperBoind:#if upper bound is less than lower bound, there is not a feasible solution
        middlePoint = int ((lowerBound + upperBoind)/2)
        if x == int (a[middlePoint]):#x has been found
            index = middlePoint
            break
        else:
            if x < a[middlePoint]:
                upperBoind = middlePoint - 1
            else:
                lowerBound = middlePoint + 1

    if lowerBound == upperBoind and a[lowerBound] == x:
        index = lowerBound#x has been found

    return index#x has been found

def binary_search_recursive (a, x,lowerBound,upperBound):
    middlePoint = int ((lowerBound+upperBound)/2)#if upper bound is equal than lower bound, there is justone feasible solution

    if lowerBound == upperBound:
        if x == a[middlePoint]:#element x has been found
            return middlePoint
        else:
            return -1
    else:
        if x == a[middlePoint]:
            return middlePoint
        else:
            if x < a[middlePoint]:
                return binary_search_recursive(a, x, lowerBound, middlePoint)
            else:
                return binary_search_recursive(a, x, middlePoint + 1, upperBound)

def interpolation_search(a,x):
    lowerBound = 0
    upperBound = int (len(a) - 1)
    index = -1

    while lowerBound < upperBound:#if upper bound is less than lower bound, there is not a feasible solution
        middlepoint = int (lowerBound + ((upperBound - lowerBound)/(a[upperBound] - a[lowerBound]))*(x - a[lowerBound]))
        if x == a[middlepoint]:#x has been found
            index = middlepoint
            break
        else:
            if x < a[middlepoint]:
                upperBound = middlepoint - 1
            else:
                lowerBound = middlepoint +1

    if lowerBound == upperBound and a[lowerBound] == x:
        index = lowerBound#x has been found

    return index#x has been found


def interpolation_search_recursive(a, x, lowerBound, upperBound):
    while lowerBound < upperBound:#if upper bound is less than lower bound, there is not a feasible solution
        middlepoint = int (lowerBound + ((upperBound - lowerBound)/(a[upperBound] - a[lowerBound]))*(x - a[lowerBound]))
        if x == a[middlepoint]:#x has been found
            return middlepoint
        else:
            if x < a[middlepoint]:
                return interpolation_search_recursive(a, x, lowerBound, middlepoint)
            else:
                return interpolation_search_recursive(a, x, middlepoint + 1, upperBound)

#MAIN
"""CREACION DE CADENA ALEATORIA DE TAMAÑO n"""
n = 10#array numbers
a = [randint(1, n) for i in range(n)]
print("Cadena desordenada: ", a, "\n")

#SORT ALGORITHMS
print("¿CUAL METODO DE ORDENAMIENTO QUIERE USAR?")
print("\n1.Insertion Sort\n2.Bubble Sort\n3.Merge Sort\n4.Quick Sort\nOpcion: ",end="")

option = 0
while option!=4:#MENU
    option = int (input())
    if option==1:
        insertion_sort(a)#method of insertion ordering algorithm
        print("\nCadena ordenada mediante Insertion Sort: ", a, "\n")
        break

    if option==2:
        bubble_sort(a)#method of sorting bubble algorithm
        print("\nCadena ordenada mediante Bubble Sort: ", a, "\n")
        break

    if option==3:
        a=merge_sort(a)#merge sorting algorithm method
        print("\nCadena ordenada mediante Merge Sort: ",a, "\n")
        break

    if option==4:
        a=quick_sort(a)#Method Sorting algorithm Quick Sort
        print("\nCadena ordenada mediante Quick Sort: ", a, "\n")
        break

    if option != 1 and  option != 2 and  option != 3 and  option != 4:
        print("¡OPCIÓN NO VALIDA!")

#SEARCH ALGORITHMS
print("¿CUAL METODO DE BUSQUEDA QUIERE USAR?")
print("\n1.Lineal Search\n2.Binary Search\n3.Binary Search Recursive\n4.Interpolation Search\n5.Interpolation Search Recursive\nOpcion: ",end="")
option2 = 0
while option2!=5:
    option2 = int(input())
    if option2==1:
        x = int(input("\nIngrese el número que desea buscar: "))
        print("\n",a,"\n\nMediante Lineal Search, el número ",x," se encuentra en el Indice: ",lineal_search(a,x))#linear search algorithm method
        break

    if option2 == 2:
        x = int(input("\nIngrese el número que desea buscar: "))
        print("\n",a,"\n\nMediante Binary Search, el número ", x, " se encuentra en el Indice: ",binary_search(a,x))#binary search algorithm method
        break

    if option2 == 3:
        x = int(input("\nIngrese el número que desea buscar: "))
        print("\n",a,"\n\nMediante Binary Search Recursive, el número ", x, " se encuentra en el Indice: ",binary_search_recursive(a,x,0,(len(a))-1))#recursive binary search algorithm method
        break

    if option2 == 4:
        x = int(input("\nIngrese el número que desea buscar: "))
        print("\n",a,"\n\nMediante Interpolation Search, el número ", x, " se encuentra en el Indice: ",interpolation_search(a,x))#method search algorithm interpolation
        break
    if option2 == 5:
        x = int(input("\nIngrese el número que desea buscar: "))
        print("\n", a, "\n\nMediante Interpolation Search Recursive, el número ", x, " se encuentra en el Indice: ",interpolation_search_recursive(a, x, 0, (len(a)) - 1))#recursive interpolation search algorithm method
        break
    if option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4 and option2 != 5:
        print("¡OPCIÓN NO VALIDA!")


