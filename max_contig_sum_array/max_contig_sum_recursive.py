# Recursive
# Find largest sum of contiguous ints
# list = [0,4,-2,1,4]. = 7

def large_contig_sum(l1, maxSum, curSum):
    if len(l1) == 0:
        return maxSum
    elif curSum + l1[0] < l1[0]:
        curSum = l1[0]
    else:
        curSum += l1[0]

    if curSum > maxSum:
        return large_contig_sum(l1[1:], curSum, curSum)
    else:
        return large_contig_sum(l1[1:], maxSum, curSum)


list1 = [0,4,-2,1,4]
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
print large_contig_sum(list1, list1[0], 0) == 7
print large_contig_sum(list2, 0, 0) == 21
print large_contig_sum(list3, 0, 0) == 20
print large_contig_sum(list4, 0, 0) == 9
print large_contig_sum(list5, 0, 0) == 13
print large_contig_sum(list6, 0, 0) == 7
print large_contig_sum(list7, list7[0], 0) == -7
print large_contig_sum(list8, 0, 0) == 0
print large_contig_sum(list9, 0, 0) == 5
print large_contig_sum(list10, 0, 0) == 17
print large_contig_sum(list11, 0, 0) == 3
print large_contig_sum(list12, 0, 0) == 5
