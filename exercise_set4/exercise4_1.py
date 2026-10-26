from datetime import date

today = date.today()

todays_date = today.strftime("%d.%m.%Y")
client_name = "Bibek Giri"
dob = "2002"
balance = 999

print(f"{client_name} ({dob}), balance: {balance} €, updated on {todays_date}.")