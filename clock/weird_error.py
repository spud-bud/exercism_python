class Clock(object):
    """docstring for Clock"""
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.time = self.time(self.hours, self.minutes)

    def time(self, hours, minutes):
        hours = hours % 24
        minutes = minutes % 60
        result = '{0:0>2}:{1:0>2}'.format(hours, minutes)
        return result

    def add(self, minutes):
        bit = 60 - self.minutes
        if bit < minutes:
            hours = ((self.hours + minutes // 60) % 24) + 1
            new_minutes = (self.minutes + (minutes % 60)) % 60
            result = '{0:0>2}:{1:0>2}'.format(hours, new_minutes)
            self.time = result
            return self.time
        else:
            result = '{0:0>2}:{1:0>2}'.format(self.hours, (self.minutes + minutes))
            self.time = result
            return self.time

        # if minutes // 60 == 0 and self.minutes + minutes > 59:
        #     hours = (self.hours + 1) % 24
        #     result = '{0:0>2}:{1:0>2}'.format(hours, (self.minutes + minutes) % 60)
        #     self.time = result
        #     return self.time
        # else:
        #     hours = (self.hours + minutes // 60) % 24
        #     result = '{0:0>2}:{1:0>2}'.format(hours, (self.minutes + minutes) % 60)
        #     self.time = result
        #     return self.time

    def __repr__(self):
        return self.time

now = Clock(0,45)
print(now.time)
print(now.add(160))

#trying to solve hour counting problem
# bit = 60 - self.minutes
# if bit < minutes:
#     hours = ((self.hours + minutes // 60) % 24) + 1
