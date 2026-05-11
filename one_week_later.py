
# -----------------------------
# Global Constants
# -----------------------------
DAYS_IN_WEEK = 7

# Days in each month (no leap year handling)
FEB_DAYS = 28
LONG_MONTH_DAYS = 31  # Jan, Mar, May, Jul, Aug, Oct, Dec
SHORT_MONTH_DAYS = 30 # Apr, Jun, Sep, Nov

# -----------------------------
# User Input
# -----------------------------
user_month = int(input("Enter a month (1–12): "))
user_day = int(input("Enter a day (1–31): "))

# Copy input values so we can keep originals for final output
month = user_month
day = user_day

# -----------------------------
# Add 7 days
# -----------------------------
day += DAYS_IN_WEEK

# -----------------------------
# Adjust for month boundaries
# -----------------------------

# February (28 days)
if month == 2 and day > FEB_DAYS:
    month += 1
    day -= FEB_DAYS

# Months with 31 days
elif (month == 1 or month == 3 or month == 5 or
      month == 7 or month == 8 or month == 10 or
      month == 12) and day > LONG_MONTH_DAYS:
    month += 1
    day -= LONG_MONTH_DAYS

# Months with 30 days
elif day > SHORT_MONTH_DAYS:
    month += 1
    day -= SHORT_MONTH_DAYS

# Wrap around past December
if month > 12:
    month %= 12

# -----------------------------
# Output
# -----------------------------
print("A week after " + str(user_month) + "/" + str(user_day) +
      " is " + str(month) + "/" + str(day))
