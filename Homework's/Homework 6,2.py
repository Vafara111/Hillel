time1 = int(input("Enter time: "))
days, rest = divmod(time1, 86400)
hours, rest = divmod(rest, 3600)
minutes, seconds  = divmod(rest, 60)
if days % 10 == 0 or days % 10 >= 5 or 10 < days < 20:
    day = "днів"
elif 2 <= days % 10 < 5:
    day = "дні"
else:
    day = "день"
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)
print(f"{days} {day}, {hours}:{minutes}:{seconds}")