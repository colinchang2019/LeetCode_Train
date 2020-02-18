class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour*60+minutes)/(60*12)*360
        m = minutes/60*360
        res = abs(m-h)
        return res if res<=180 else 360-res 
