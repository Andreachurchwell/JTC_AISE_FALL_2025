"""LeetCode Problem 1603 Design Parking System"""


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        # setting big
        self.big = big
        #setting medium
        self.medium = medium
        #setting small
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        # if its big
        if carType == 1:
            # if its got a 1 or higher, then theres a spot
            if self.big > 0:
                # subtract a spot bc its gonna use that space
                self.big -= 1
                # successfully returns a bool
                return True
            else:
                return False
        # if its a med size car
        elif carType == 2:
            # if theres a number over 0, then theres a spot
            if self.medium > 0:
                # need to remove 1 of available spots
                self.medium -= 1
                # returning bool 
                return True
            # if its 0 -> that means no spot
            else:
                return False
        # if carType is small
        elif carType == 3:
            # if num is greater than 0, theres a spot for it
            if self.small > 0:
                # need to remove 1 of available spots
                self.small -= 1
                # return bool 
                return True
            else:
                # bool for no spot
                return False
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# --- TEST CASES ---

# Test 1: Basic Example from the prompt
ps1 = ParkingSystem(1, 1, 0)
print(ps1.addCar(1))  # True  (1 big spot used, left: 0)
print(ps1.addCar(2))  # True  (1 medium spot used, left: 0)
print(ps1.addCar(3))  # False (no small spots)
print(ps1.addCar(1))  # False (no big spots left)

# Test 2: More small spots than others
ps2 = ParkingSystem(0, 1, 2)
print(ps2.addCar(3))  # True  (small spot used)
print(ps2.addCar(3))  # True  (second small spot used)
print(ps2.addCar(3))  # False (now out of small spots)
print(ps2.addCar(2))  # True  (medium spot used)
print(ps2.addCar(1))  # False (no big spots at all)

# Test 3: All spaces full quickly
ps3 = ParkingSystem(1, 0, 1)
print(ps3.addCar(1))  # True  (big spot used)
print(ps3.addCar(1))  # False (no more big)
print(ps3.addCar(2))  # False (no medium)
print(ps3.addCar(3))  # True  (small spot used)
print(ps3.addCar(3))  # False (no more small)

# Test 4: Check independence of different ParkingSystem instances
ps4 = ParkingSystem(2, 2, 2)
print(ps4.addCar(1))  # True
print(ps4.addCar(1))  # True
print(ps4.addCar(1))  # False (big full, but others still open)
print(ps4.addCar(2))  # True
print(ps4.addCar(3))  # True