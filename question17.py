from datetime import date, timedelta


def count_business_days(start_date, end_date):
    weekdays = {0, 1, 2, 3, 4}

    business_day_count = 0

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() in weekdays:
            business_day_count += 1
        current_date += timedelta(days=1)

    return business_day_count


start_date = date(2022, 9, 22)
end_date = date(2022, 10, 5)

result = count_business_days(start_date, end_date)
print("Number of business days:", result)