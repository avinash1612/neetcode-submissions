"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = []
        ends = []
        count = 0
        for i in range(len(intervals)-1):
            count = 0
            for j in range(i+1,len(intervals)):
                print(intervals[j].start,intervals[i].end)
               # print(i.start)
                if((intervals[j].start<intervals[i].end)):
                    if((intervals[j].end > intervals[i].start)):
                        return False
        
        return True
        
        