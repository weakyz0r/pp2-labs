from datetime import datetime

def difference_in_seconds(date1, date2):
    datetime1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    difference = abs((datetime2 - datetime1).total_seconds())
    
    return difference

date1 = input("1st date is : ")
date2 = input("2nd date is : ")

difference_seconds = difference_in_seconds(date1, date2)
print("Difference in sec-s:", difference_seconds)




# print(x.strftime("%A"))
