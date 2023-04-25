def sockMerchant(n, ar):
    # Write your code here
    map = {}
    for i in ar:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
     
    count = 0
    for sock in map.values():
        count += sock // 2
    return count