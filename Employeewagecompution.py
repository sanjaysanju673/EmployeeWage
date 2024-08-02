'''
@Author: v sanjay kumar
@Date: 2024-07-22 02:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 02:00:30
@Title : Employee wage
'''

import random
import abc
class EmployeeWageComputation:
    def __init__(self,working_hours_per_month,wage_per_hour,no_of_working_days):
        self.wage_per_hour= wage_per_hour
        self.full_time_hours = 8
        self.part_time_hours = 4
        self.no_of_working_days = no_of_working_days
        self.working_hours_per_month =working_hours_per_month

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
        return self.wage_per_hour * self.full_time_hours

    def part_time_wage(self):
        """
        Calculate the part-time employee wage.

        Returns:
        - Employee's wage for part-time work
        """
        return self.wage_per_hour* self.part_time_hours

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

        while total_hours <= self.working_hours_per_month and total_days <self.no_of_working_days:
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
                
            total_days +=1   
        print("Total Wage of Employee in $",total_wage)
        return all_monthly_wages

    def main(self):
        print("-----------------------------------------")
        print("Welcome to Employee Wage Computation")
        
if __name__ == "__main__":
    employee_wage_computation = EmployeeWageComputation(100,20,20)
    employee_wage_computation.main()
    print("The monthly wages of employee =",employee_wage_computation.condition_wages())