class Node:
    def __init__(self, num):
        self.num = num
        self.next = None


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def get_min_max(self, A):
        """
        returns (min,max)
        """
        min_num = A[0]
        max_num = A[0]
        for num in A:
            if num < min_num:
                min_num = num
            elif num > max_num:
                max_num = num
        return (min_num, max_num)

    def maximumGapCounting(self, A):
        if len(A) < 2:
            return 0
        min_max = self.get_min_max(A)
        min_num = min_max[0]
        max_num = min_max[1]
        N = max_num - min_num
        buckets = [None for x in range(N+1)]
        for num in A:
            index = num-min_num
            buckets[index] = 1
        max_gap = 0
        start = 0
        i = 0
        while i < len(buckets):
            if buckets[i] == 1:
                if i-start > max_gap:
                    max_gap = i-start
                start = i
            i+=1
        return max_gap

    def maximumGapBucket(self, A):
        if len(A) < 2:
            return 0
        buckets = self.get_buckets(A)
        max_gap = 0
        prev_node = None
        i = 0
        while i < len(buckets):
            if buckets[i] is not None:
                if prev_node is None:
                    prev_node = buckets[i]
                cur_node = buckets[i]
                while cur_node is not None:
                    cur_gap = cur_node.num - prev_node.num
                    if cur_gap > max_gap:
                        max_gap = cur_gap
                    prev_node = cur_node
                    cur_node = cur_node.next
            i+=1
        return max_gap

    def get_buckets(self, A):
        max_num = max(A)
        min_num = min(A)
        N = len(A)
        buckets = [None for x in range(N)]
        bucket_size = (max_num-min_num+1)/float(N)
        for num in A:
            index_to_place = int((num-min_num)/bucket_size)
            self.insert(buckets, num, index_to_place)
        return buckets

    def insert(self, buckets, num, index):
        new_node = Node(num)
        if buckets[index] is None:
            buckets[index] = new_node
            return
        prior = buckets[index]
        if new_node.num <= prior.num:
            new_node.next = prior
            buckets[index] = new_node
            return
        cur_node = prior.next
        while cur_node is not None \
        and cur_node.num < new_node.num:
            prior = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            prior.next = new_node
        else:
            prior.next = new_node
            new_node.next = cur_node


## Tests

sol = Solution()


print "Running get_buckets -----"
print sol.get_buckets([2,10,5])
print sol.get_buckets([2,3,1,1,1,1,6,3,1,1,3,3,2,10,5])
print sol.get_buckets([1,1,1,1,1])
print sol.get_buckets([1,2,3,4,5])
print sol.get_buckets([100, 100, 100, 100, 100])

print "Running maximumGapBucket -----"
print sol.maximumGapBucket([1])
print sol.maximumGapBucket([1,10])
print sol.maximumGapBucket([1,10,5,17])
print sol.maximumGapBucket([1,10,5])
print sol.maximumGapBucket([2,3,1,1,1,1,6,3,1,1,3,3,2,10,5])
print sol.maximumGapBucket([ 83564666, 2976674, 46591497, 24720696, 16376995, 63209921, 25486800, 49369261, 20465079, 64068560, 7453256, 14180682, 65396173, 45808477, 10172062, 28790225, 82942061, 88180229, 62446590, 77573854, 79342753, 2472968, 74250054, 17223599, 47790265, 24757250, 40512339, 24505824, 30067250, 82972321, 32482714, 76111054, 74399050, 65518880, 94248755, 76948016, 76621901, 46454881, 40376566, 13867770, 76060951, 71404732, 21608002, 26893621, 27370182, 35088766, 64827587, 67610608, 90182899, 66469061, 67277958, 92926221, 58156218, 44648845, 37817595, 46518269, 44972058, 27607545, 99404748, 39262620, 98825772, 89950732, 69937719, 78068362, 78924300, 91679939, 52530444, 71773429, 57678430, 75699274, 5835797, 74160501, 51193131, 47950620, 4572042, 85251576, 49493188, 77502342, 3244395, 51211050, 44229120, 2135351, 47258209, 77312779, 37416880, 59038338, 96069936, 20766025, 35497532, 67316276, 38312269, 38357645, 41600875, 58590177, 99257528, 99136750, 4796996, 84369137, 54237155, 64368327, 94789440, 40718847, 12226041, 80504660, 8177227, 85151842, 36165763, 72764013, 36326808, 80969323, 22947547, 76322099, 7536094, 18346503, 65759149, 45879388, 53114170, 92521723, 15492250, 42479923, 20668783, 64053151, 68778592, 3669297, 73903133, 28973293, 73195487, 64588362, 62227726, 17909010, 70683505, 86982984, 64191987, 71505285, 45949516, 28244755, 33863602, 18256044, 25110337, 23997763, 81020611, 10135495, 925679, 98158797, 73400633, 27282156, 45863518, 49288993, 52471826, 30553639, 76174500, 28828417, 41628693, 80019078, 64260962, 5577578, 50920883, 16864714, 54950300, 9267396, 56454292, 40872286, 33819401, 75369837, 6552946, 26963596, 22368984, 43723768, 39227673, 98188566, 1054037, 28292455, 18763814, 72776850, 47192134, 58393410, 14487674, 4852891, 44100801, 9755253, 37231060, 42836447, 38104756, 77865902, 67635663, 43494238, 76484257, 80555820, 8632145, 3925993, 81317956, 12645616, 23438120, 48241610, 20578077, 75133501, 46214776, 35621790, 15258257, 20145132, 32680983, 94521866, 43456056, 19341117, 29693292, 38935734, 62721977, 31340268, 91841822, 22303667, 96935307, 29160182, 61869130, 33436979, 32438444, 87945655, 43629909, 88918708, 85650550, 4201421, 11958347, 74203607, 37964292, 56174257, 20894491, 33858970, 45292153, 22249182, 77695201, 34240048, 36320401, 64890030, 81514017, 58983774, 88785054, 93832841, 12338671, 46297822, 26489779, 85959340 ])

print "Running maximumGapCounting -----"
print sol.maximumGapCounting([1])
print sol.maximumGapCounting([1,10])
print sol.maximumGapCounting([1,10,5,17])
print sol.maximumGapCounting([1,10,5])

print sol.get_min_max([1,3,10,-3])