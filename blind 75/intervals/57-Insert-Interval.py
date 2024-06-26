# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


#my sol:

#got error
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals==[]:
            return newInterval
        res = []
        ol = []
        for i in range(len(intervals)):
            if (newInterval[0]>=intervals[i][0] and newInterval[0]<=intervals[i][1]) or (newInterval[1]>=intervals[i][0] and newInterval[1]<=intervals[i][1]):
                ol.append(intervals[i])
            else:
                res.append(intervals[i])
            if intervals[i][0]>newInterval[0] and intervals[i][1]<newInterval[1]:
                res.remove(intervals[i])

        a = ol[0][0]
        b = ol[len(ol)-1][1]
        if a>newInterval[0]: a = newInterval[0]
        if b<newInterval[1]: b = newInterval[1]
        res.append([a,b])
        return sorted(res)


#op sol:
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
