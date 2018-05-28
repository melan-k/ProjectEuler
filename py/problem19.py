DAY_OF_THE_WEEK = \
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

DAYS_OF_MONTH = \
['PADDING', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def check_invalid_day(year, month, day) :
    assert(month <= 12 and month >= 1)
    if month != 2 :
        assert(day >= 1 and day <= DAYS_OF_MONTH[month])
    else :
        if leap_year(year) :
            assert(day >= 1 and day <= 29)
        else :
            assert(day >= 1 and day <= 28)

def leap_year(year) :
    return ( year % 4 == 0 and \
             not (year % 400 != 0 and year % 100 == 0) )

def get_passed_years_list(year1, year2) :
    if year1 < year2 :
        return range(year1 + 1, year2)
    else :
        return range(year2 + 1, year1)

def get_passed_months_list(month1, month2) :
    if month1 < month2 :
        return range(month1 + 1, month2)
    else :
        return range(month1 + 1, len(DAYS_OF_MONTH)) + range(1, month2)

def remaining_days_of_month(year, month, day) :
    assert(year != 0 and month != 0 and day != 0)
    if day == DAYS_OF_MONTH[month] :
        return 0

    if month == 2 :
        if leap_year(year) :
            assert(day <= DAYS_OF_MONTH[month] + 1)
            return 29 - day
        else :
            assert(day <= DAYS_OF_MONTH[month])
            return 28 - day
    else :
        assert(day <= DAYS_OF_MONTH[month])
        return DAYS_OF_MONTH[month] - day

def remaining_days_of_year(year, month, day) :
    diff = remaining_days_of_month(year, month, day)
    months = get_passed_months_list(month, 13)
    for month in months :
        if month == 2 and leap_year(year) :
            diff += DAYS_OF_MONTH[2] + 1
        else :
            diff += DAYS_OF_MONTH[month]

    assert(diff < 365)
    return diff

def get_day_of_the_week(year, month, day) :
    if year >= 1900 :
        diff = calc_days_diff(1900, 1, 1, year, month, day)
    else :
        diff = 7 - calc_days_diff(year, month, day, 1900, 1, 1)

    return DAY_OF_THE_WEEK[diff % 7]

def passed_days_of_year(year, month, day) :
    passed_months = range(1, month)
    passed = 0
    for month in passed_months :
        if month == 2 and leap_year(year) :
            passed += DAYS_OF_MONTH[2] + 1
        else :
            passed += DAYS_OF_MONTH[month]
    passed += day
    assert(passed < 365)

    return passed

def calc_days_diff(year1, month1, day1, year2, month2, day2) :
    check_invalid_day(year1, month1, day1)
    check_invalid_day(year2, month2, day2)

    days = 0
    years = get_passed_years_list(year1, year2)

    for year in years :
        if leap_year(year) :
            days += 366
        else :
            days += 365

    if year1 <= year2 :
        remaining = remaining_days_of_year(year1, month1, day1)
        passed = passed_days_of_year(year2, month2, day2)
    else :
        remaining = remaining_days_of_year(year2, month2, day2)
        passed = passed_days_of_year(year1, month1, day1)

    if year1 == year2 :
        return remaining + days + passed - 365
    else :
        return remaining + days + passed

def count_sunday_fell_on_first_of_the_month() :
    year = 1901
    cnt = 0
    while year <= 2000 :
        for month in range(1, 13) :
            if get_day_of_the_week(year, month, 1) == 'Sunday' :
                print("{}/{}/1".format(year, month))
                cnt += 1
        year += 1

    return cnt

print(count_sunday_fell_on_first_of_the_month())
