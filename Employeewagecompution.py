import random

daily_wage_rate = 20
full_time_hours = 8
part_time_hours = 4

def check_attendance():
    """
    Check the attendance for an employee.

    Returns:
    - 'full time' if employee is present full time
    - 'part time' if employee is present part time
    """
    attendance = random.randint(0, 2)
    if attendance == 1:
        return 'full time'
    elif attendance == 2:
        return 'part time'
    else:
        return 'absent'

def daily_wage():
    """
    Calculate the daily employee wage for full time.

    Returns:
    - Employee's daily wage for full time work
    """
    return daily_wage_rate * full_time_hours

def part_time_wage():
    """
    Calculate the part-time employee wage.

    Returns:
    - Employee's wage for part-time work
    """
    return daily_wage_rate * part_time_hours

def monthly_wage():
    """
    Calculate the monthly employee wage assuming full time work for 20 days.

    Returns:
    - Employee's monthly wage for full time work
    """
    return daily_wage() * 20

def condition_wages():
    """
    Calculate wages based on attendance for a month (maximum 20 days or 100 hours).

    Returns:
    - List of daily wages for the month
    """
    total_hours = 0
    total_days = 0
    total_wage = 0
    all_monthly_wages = []

    while total_hours <= 100 and total_days < 20:
        attendance = check_attendance()
        if attendance == 'full time':
            total_hours += full_time_hours
            daily_wage_amount = daily_wage()
            total_wage += daily_wage_amount
            all_monthly_wages.append(daily_wage_amount)
            
        elif attendance == 'part time':
            total_hours += part_time_hours
            part_time_wage_amount = part_time_wage()
            total_wage += part_time_wage_amount
            all_monthly_wages.append(part_time_wage_amount)
        else:
            all_monthly_wages.append(0)
        total_days +=1
    total_wage

    return all_monthly_wages,total_wage

def main():
    print("Welcome to Employee Wage Computation")
    while True:
        print("Choose Your Choice:")
        print("1 - Check the attendance of employee")
        print("2 - Check the part-time wage of employee")
        print("3 - Check the full-time wage of employee")
        print("4 - Check the monthly wage of employee")
        print("5 - Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("The employee attendence is",check_attendance())
        elif choice == 2:
            print("The part Time wage of employee",part_time_wage())
        elif choice == 3:
            print("The full time wage of employee",daily_wage())
        elif choice == 4:
            monthly_wages,total_wage=condition_wages()
            print("The monthly wages of employee is",monthly_wages)
            print("The total wage of Employee is (per month)&:",total_wage)
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
