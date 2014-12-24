# Find largest sum of contiguous ints
#list = [0,4,-2,1,4]. = 7

def large_contig_sum(l1):
    maxSum = l1[0]
    curSum = 0
    n = len(l1)
    i = 1 #length of chunk
    while i <= n:
        j = 0
        while j <= n-i:
            k = 0
            while k < i:
                curSum += l1[j+k]
                k += 1
            if curSum > maxSum:
                maxSum = curSum
            curSum = 0
            j += 1
        i += 1
    return maxSum


list1 = [0,4,-2,1,4] # 7
list2 = [0,-1,-2,9,8,4,-1,-6]
list3 = [0,4,-6,3,8,9]
list4 = [0,4,-6, 9]
list5 = [0,4,9]
list6 = [7]
list7 = [-7]
print large_contig_sum(list1) == 7
print large_contig_sum(list2) == 21
print large_contig_sum(list3) == 20
print large_contig_sum(list4) == 9
print large_contig_sum(list5) == 13
print large_contig_sum(list6) == 7
print large_contig_sum(list7) == -7
