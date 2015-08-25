class Date:

    month_lengths = {
                    1:31,
                    2:28,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31}

    month_lengths_leapyear = {
                    1:31,
                    2:29,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31}


    def __init__(self):
        self.year = 1900
        self.month = 1
        self.day = 1
        self.dayofweek = 1
        self.leapyear = 1


    def AdvanceDayOfWeek(self):
        if self.dayofweek < 7:
            self.dayofweek += 1
        else:
            self.dayofweek = 1


    def AdvanceYear(self):
        self.month = 1
        self.day = 1
        self.year += 1
        if self.year % 400 == 0:
            self.leapyear = 1
        elif self.year % 100 == 0:
            self.leapyear = 0
        elif self.year % 4 == 0:
            self.leapyear = 1
        else:
            self.leapyear = 0


    def AdvanceMonth(self):
        if self.month < 12:
            self.month += 1
            self.day = 1
        else:
            self.AdvanceYear()
    

    def AdvanceDay(self):
        if self.leapyear:
            if self.day < self.month_lengths_leapyear[self.month]:
                self.day +=1
                self.AdvanceDayOfWeek()
            else:
                self.AdvanceMonth()
                self.AdvanceDayOfWeek()
        else:
            if self.day < self.month_lengths[self.month]:
                self.day +=1
                self.AdvanceDayOfWeek()
            else:
                self.AdvanceMonth()
                self.AdvanceDayOfWeek()


CurrentDate = Date()
SundayCount = 0

while(True):
    if CurrentDate.year == 1900:
        CurrentDate.AdvanceDay()
        continue
    if CurrentDate.day == 1 and CurrentDate.dayofweek == 1:
        SundayCount += 1
    if CurrentDate.day == 31 and CurrentDate.month == 12 and CurrentDate.year == 2000:
        break
    CurrentDate.AdvanceDay()

print SundayCount
