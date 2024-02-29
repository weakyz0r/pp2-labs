# from datetime import datetime, timedelta

# today = datetime.now()

# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)

# print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("Today:", today.strftime("%Y-%m-%d"))
# print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
two_years_later = today + timedelta(days=730)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
print("Two_years_later : " , two_years_later)
