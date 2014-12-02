# Linear
# Find largest sum of contiguous ints
# list = [0,4,-2,1,4]. = 7

def large_contig_sum(l1):
    maxSum = l1[0]
    curSum = 0
    for e in l1:
        if curSum + e < e:
            curSum = e
        else:
            curSum += e
        if curSum > maxSum:
            maxSum = curSum
    return maxSum


list1 = [0,4,-2,1,4] # 7
list2 = [0,-1,-2,9,8,4,-1,-6]
list3 = [0,4,-6,3,8,9]
list4 = [0,4,-6, 9]
list5 = [0,4,9]
list6 = [7]
list7 = [-7]
list8 = [-3,-4,-2,-5, 0]
list9 = [1,1,1,1,1]
list10 = [9,8,-6,-2,-20,16,-2]
list11 = [1,1,1,-3,1,1,1]
list12 = [0,-2,5,-4,-3]
print large_contig_sum(list1) == 7
print large_contig_sum(list2) == 21
print large_contig_sum(list3) == 20
print large_contig_sum(list4) == 9
print large_contig_sum(list5) == 13
print large_contig_sum(list6) == 7
print large_contig_sum(list7) == -7
print large_contig_sum(list9) == 5
print large_contig_sum(list10) == 17
print large_contig_sum(list11) == 3
print large_contig_sum(list12) == 5
