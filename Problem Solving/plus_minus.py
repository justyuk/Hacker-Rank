def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    l=len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
    print(f"{pos/l:.6f}")
    print(f"{neg/l:.6f}")
    print(f"{zero/l:.6f}")