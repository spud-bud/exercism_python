from math import copysign

class Clock(object):
    """docstring for Clock"""
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.time = self.time(self.hours, self.minutes)

    def time(self, hours, minutes):
        show_minutes = minutes % 60
        hours = (hours + (minutes // 60)) % 24
        result = '{0:0>2}:{1:0>2}'.format(hours, show_minutes)
        return result

    def add(self, minutes):
        bit = 60 - self.minutes #difference between next hour and the minutes on clock (i.e. self.minutes)
        carry_over = copysign((abs(minutes) % 60), minutes) #part of minutes past last multiple of 60
        if minutes >= 0:
            hours = (((self.hours + minutes // 60) % 24) + ((carry_over > bit) or (bit < minutes))) % 24
            new_minutes = (self.minutes + (minutes % 60)) % 60
            result = '{0:0>2}:{1:0>2}'.format(hours, new_minutes)
            self.time = result
            return self.time
        else:
            new_minutes = (self.minutes + minutes) % 60
            hours = (self.hours + int(minutes / 60) - (abs(carry_over) > self.minutes)) % 24
            result = '{0:0>2}:{1:0>2}'.format(hours, new_minutes)
            self.time = result
            return self.time

    def __repr__(self):
        return self.time


now = Clock(10, 3)
equal_clock = Clock(34, 37)
print(now.time)
print(now.add(-70))
