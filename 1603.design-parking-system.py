#
# @lc app=leetcode id= lang=python3
#
# [] Design Parking System
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = []
        self.medium = []
        self.small = []

    def addCar(self, carType: int) -> bool:
        # add the corresponding car type to the car list
        if carType == 1:
            self.big.append(carType)
            return True
        elif carType == 2:
            self.medium.append(carType)
            return True
        elif carType == 3:
            self.small.append(carType)
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end
