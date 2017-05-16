def is_leap_year(YEAR):
    if (YEAR % 4) == 0:
        if (YEAR % 100) != 0:
            return True
        else: 
            if (YEAR % 400) == 0:
                return True
            else:
                return False
    else: return False
    

# I hate complicated if..else construction. I think there is a possibility to do it simpler. 
