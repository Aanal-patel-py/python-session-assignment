from datetime import datetime,date
class DateUtils:

    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def days_until(self,target_date):
        d1=date(target_date.year,target_date.month,target_date.day)
        d2=date(self.year,self.month,self.day)
        return (d2-d1).days

    
    @classmethod
    def from_string(cls,date_string, format):
        date_obj=datetime.strptime(date_string,format)
        return cls(date_obj.year,date_obj.month,date_obj.day)
        
    @staticmethod
    def is_valid_date(year, month, day):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
                return False

    @staticmethod
    def is_leap_year(year):
        if year%4==0:
            return True
        else:
            False

d=DateUtils.from_string("2025-12-10","%Y-%m-%d")
print(d.year, d.month, d.day)
x= DateUtils(2025,10,27)
print(x.days_until(DateUtils(2025,10,20)))
