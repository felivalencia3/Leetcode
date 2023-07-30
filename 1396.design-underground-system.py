#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.rider_map = dict() # {id: [(startStation, time)]}
        self.time_map = defaultdict(list) # {"startStation - endStation": [times]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.rider_map[id] = (stationName, t) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # remove self.rider_map[id], calculate time, and add to time time_map
        start_station, start_time = self.rider_map[id]
        del self.rider_map[id]
        self.time_map[f"{start_station}-{stationName}"].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.time_map[f"{startStation}-{endStation}"]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
sys = UndergroundSystem()
sys.checkIn(45, "L", 3)
sys.checkIn(32, "P", 8)
sys.checkIn(27, "L", 10)
sys.checkOut(45, "W", 15)
sys.checkOut(27, "W", 20)
sys.checkOut(32, "C", 22)
print(sys.getAverageTime("P", "C")) # returns 14.000
print(sys.getAverageTime("L", "W")) # returns 11.000
