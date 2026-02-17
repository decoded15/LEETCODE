'''
LeetCode 401: Binary Watch
Approach: Brute Force + Bit Counting
Time Complexity: O(1)  (12 × 60 = 720 checks)
Space Complexity: O(k)  (depends on number of valid times)

A binary watch has:
- 4 LEDs representing hours (0–11)
- 6 LEDs representing minutes (0–59)

Given an integer turnedOn, return all possible valid times
where exactly turnedOn LEDs are ON.

The solution:
1. Iterate through all possible hours (0–11).
2. Iterate through all possible minutes (0–59).
3. Count total number of 1s in binary(hour) + binary(minute).
4. If equal to turnedOn, format and store the time.

Example:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
'''

def readBinaryWatch(turnedOn):
        result = []

        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append(str(hour) + ":" + "{:02d}".format(minute))

        return result