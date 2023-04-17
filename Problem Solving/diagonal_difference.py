def diagonalDifference(arr):
    # Write your code here
    diagL = 0
    diagR = 0
    l = len(arr)
    for i in range(l):
        diagL += (arr[i][l-1-i])
        diagR += (arr[i][i])
    return abs(diagL - diagR)