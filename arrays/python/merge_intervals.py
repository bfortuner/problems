"""
Merge Intervals

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
    	return str((self.start,self.end))

class Solution:

	def reorder(self, inter):
		if inter.end < inter.start:
			tmp = inter.end
			inter.end = inter.start
			inter.start = tmp

	def is_overlap(self, inter, new_inter):
		return not max(inter.start, new_inter.start) >= \
			min(inter.end, new_inter.end)

	def insert(self, intervals, new_interval):
		self.reorder(new_interval)
		result = []
		start_index = None
		end_index = None
		
		if len(intervals) < 1: # empty intervals
			return [new_interval]
		if new_interval.end < intervals[0].start:
			return [new_interval] + intervals
		if new_interval.start > intervals[-1].end:
			return intervals + [new_interval]
		if new_interval.start <= intervals[0].start and \
		new_interval.end >= intervals[-1].end:
			return [new_interval]

		i = 0
		while i < len(intervals):
			if start_index is None and end_index is None and \
			i > 0 and new_interval.start > intervals[i-i].end \
				and new_interval.end < intervals[i].start:
				return intervals[:i] + [new_interval] + intervals[i:] 
			elif start_index is None:
				if self.is_overlap(intervals[i], new_interval):
					start_index = i
			elif end_index is None:
				if not self.is_overlap(intervals[i], new_interval):
					end_index = i-1
			i += 1
		if start_index is None:
			start_index = 0
		if end_index is None:
			end_index = len(intervals)-1
		return intervals[:start_index] \
		+ [self.merge(intervals[start_index], intervals[end_index], new_interval)] \
		+ intervals[end_index+1:]


	def merge(self, start, end, new):
		return Interval(min(start.start, new.start), 
			max(end.end, new.end))


# New solution Tests

a1 = [Interval(1,3),Interval(6,9)]
a2 = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
a3 = [Interval(1,3),Interval(4,9)]
a4 = [Interval(1,3),Interval(4,9)]
a5 = []
a6 = [Interval(3,4),Interval(5,9)]
a7 = [Interval(3,5),Interval(8,10)]
a8 = [Interval(31935139, 38366404), Interval(54099301, 76986474), Interval(87248431, 94675146)]

m1 = Interval(2,5)
m2 = Interval(4,9)
m3 = Interval(0,3)
m4 = Interval(4,5)
m5 = Interval(20,30)
m6 = Interval(0,1)
m7 = Interval(1,12)
m8 = Interval(10,3)
m9 = Interval(43262807, 68844111)

sol = Solution()

def test_is_overlap():
	print "TESTIN IS OVERLAP"
	assert sol.is_overlap(m1,m2) == True
	assert sol.is_overlap(m2,m3) == False
	assert sol.is_overlap(m1,m3) == True

def test_insert():
	print "TESTIN INSERT"
	print sol.insert(a1, m1)
	print sol.insert(a2, m2)
	print sol.insert(a1, m3)
	print sol.insert(a1, m4)
	print sol.insert(a5, m4)
	print sol.insert(a4, m5)
	print sol.insert(a6, m6)
	print sol.insert(a7, m7)
	print sol.insert(a7, m8)
	print sol.insert(a8, m9)

if __name__ == "__main__":
	test_is_overlap()
	test_insert()

