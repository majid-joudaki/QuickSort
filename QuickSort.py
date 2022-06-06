# sort a list based on Quick sort
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)

# main function
def main():
    A = [10,8,5,7,3,4,6,2,9,1]
    print(QuickSort(A))

if __name__ == "__main__":
    main()

    

    
    
    
    


    

    