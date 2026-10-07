import bisect
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts=[(interval[0],i) for i,interval in enumerate(intervals)]

        starts.sort()
        sorted_start_times = [item[0] for item in starts]

        result=[]
        for interval in intervals:
            end_time=interval[1]
            idx = bisect.bisect_left(sorted_start_times,end_time)

            if idx < len(starts):
                result.append(starts[idx][1])
            else:
                result.append(-1)
        return result