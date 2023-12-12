
def getListMonthsRemain(month_num: int) -> [int]:
    # validation
    if month_num < 1 or month_num > 12:
        return None
    
    remain_months = [month for month in range(1,13,1) if month >= month_num]
    return remain_months


def getListDaysRemain(day_num: int) -> [int]:
    # validation
    if day_num < 1 or day_num > 31:
        return None
    
    remain_days = [day for day in range(1,32,1) if day >= day_num]
    return remain_days