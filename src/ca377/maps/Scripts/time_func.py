#!/usr/bin/env python


# Class taking in integers (seconds and meters), converting them to their higher units, if needed,
# and adding a string to the end with units and returning the values

class TimeDisFormat:

    def __init__(self, total_dur, step_dur, total_dis, step_dis):
        self.total_dur = total_dur
        self. step_dur = step_dur
        self.total_dis = total_dis
        self.step_dis = step_dis

    # Convert seconds to mins and hrs
    def time_math(self):
        # Convert seconds to mins after calculating remaining time
        remain_dur = round(float((self.total_dur - self.step_dur) / 60), 0)

        # if dur is greater than 59 mins (an hour)
        if remain_dur > 59:
            # if dur is greater than 1439 mins (a day)
            hours = round(remain_dur / 60)
            mins = round(remain_dur % 60)
            return [mins, hours]
        else:
            mins = round(remain_dur)
            return [mins]

    # Adding a string with units and combining them
    def time_str(self, vals):
        remain_dur_str = ""
        if len(vals) == 2:
            hours = vals[1]
            # if there are hours concatenate the string
            if hours > 1:
                remain_dur_str = str(hours) + " hours "
            else:
                remain_dur_str = str(hours) + " hour "

        #  if there are mins concatenate the string
        mins = vals[0]
        if mins > 0:
            if mins > 1:
                remain_dur_str += str(mins) + " mins"
            elif mins == 0:
                remain_dur_str = "-"
            else:
                remain_dur_str += str(mins) + " min"

        return remain_dur_str

    # Convert meters to kms
    def dis_math(self):
        remain_dis = self.total_dis - self.step_dis

        # If dis is greater than 999m
        if remain_dis > 999:
            km = round(float(remain_dis / 1000), 1)
            return km
        else:
            m = remain_dis
            return m

    # Adding a string with units and combining them
    def dis_str(self, val):
        remain_dis_str = ""
        if isinstance(val, int) is True:
            remain_dis_str += str(val) + " m"
        elif val == 0:
            remain_dis_str = "-"
        else:
            remain_dis_str += str(val) + " km"
        return remain_dis_str

    def concatenate(self):
        return TimeDisFormat.time_str(self, TimeDisFormat.time_math(self)),\
               TimeDisFormat.dis_str(self, TimeDisFormat.dis_math(self))
