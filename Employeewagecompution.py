'''
    @Author: v sanjay kumar
    @Date: 2024-08-02 11:30:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-08-02 11:30:30
    @Title :Refactor the Code to write a Class Method to Compute Employee Wage
'''


import random

class EmployeeWageComputation:
    def __init__(self):
        self.daily_wage_rate = 20
        self.full_time_hours = 8
        self.part_time_hours = 4

    def check_attendance(self):
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

    def daily_wage(self):
        """
        Calculate the daily employee wage for full time.

        Returns:
        - Employee's daily wage for full time work
        """
        return self.daily_wage_rate * self.full_time_hours

    def part_time_wage(self):
        """
        Calculate the part-time employee wage.

        Returns:
        - Employee's wage for part-time work
        """
        return self.daily_wage_rate * self.part_time_hours

    def monthly_wage(self):
        """
        Calculate the monthly employee wage assuming full time work for 20 days.

        Returns:
        - Employee's monthly wage for full time work
        """
        return self.daily_wage() * 20

    def condition_wages(self):
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
            attendance = self.check_attendance()
            if attendance == 'full time':
                total_hours += self.full_time_hours
                daily_wage = self.daily_wage()
                total_wage += daily_wage
                all_monthly_wages.append(daily_wage)
                
            elif attendance == 'part time':
                total_hours += self.part_time_hours
                part_time_wage = self.part_time_wage()
                total_wage += part_time_wage
                all_monthly_wages.append(part_time_wage)
            else:
                all_monthly_wages.append(0)

        total_days += 1       

        return all_monthly_wages

    def main(self):
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
                print("The Employee attendence is",self.check_attendance())
            elif choice == 2:
                print("The part time wage of employee is:",self.part_time_wage())
            elif choice == 3:
                print("The full time wage of Employee is :",self.daily_wage())
            elif choice == 4:
                monthly_wages_all =self.condition_wages()
                print(monthly_wages_all)
                print("The total wage of Employee is(per month)$",sum(monthly_wages_all))
                print("The monthly wages of Employee is",monthly_wages_all)
            elif choice == 5:
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    employee_wage_computation = EmployeeWageComputation()
    employee_wage_computation.main()
