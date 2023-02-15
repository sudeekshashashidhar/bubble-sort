def bubblesort(arr):
  bs = len(arr)
  
  #transverse through all array elements
  for i in range(bs - 1):
  #range(n) also works but outer loop will repeat one time more than needed

    #last i elements are already in place
    for j in range(0, bs - i - 1):
    # transverse the array from 0 - i - 1
    # swap if the element found is greater
    # than the next elemnt
      
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]


# driver code to test above
arr = [13, 45, 76, 32, 0, 10, 100, 99, 81, 93, 67, 55]

bubblesort(arr)
# to call the function

print("The sorted array from ascending to descending order is: ")
for i in range(len(arr)):
  print("%d" %arr[i])