'''
    @Author: v sanjay kumar
    @Date: 2024-07-30 03:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-30 03:00:30
    @Title : Employee wage problems

'''
import random

print("Welcome to Employee Wage Computation")

def CheckAttendance():
    
    """
    Description:
    Function that check the attendence for employee.

    Parameters:
    - None.
    Returns:
    -None.
    """

    attendnce =random.randint(0,2)

    if attendnce == 1:
        return 'full time'
    elif attendnce == 2:
        return 'part time'
    else:
        return "Employee is absent"

        



def Dailywage():
    
    '''Description:
    Function that caluculate the daily employe wage.

    Parameters:
    - None.
    Returns:
    -None.
    '''
    dailywage = 20
    hours = 8
    Employee_daily_wage = dailywage *hours
    return Employee_daily_wage


def PartTime():
    '''Description:
    Function that caluculate the part time employee wage.

    Parameters:
    - None.
    Returns:
    -None.
    '''
    wage_Hour = 20

    Employee_Part_wage =wage_Hour* hours

    return Employee_Part_wage


def monthlywage():
    '''Description:
    Function that caluculate the part time employee wage.

    Parameters:
    - None.
    Returns:
    -None.
    '''
    print( "Employee monthly wage",Dailywage()*20)


def main():
    print("Choose Your Choice ")
    print("1 - Check the attendence of employee")
    print("2 - Check the parttime wage of employee")
    print("3 - Check the full time wage of employee")
    print("4 - Check the monthly wage of employee")
    print("5 - Exit ")
    chioce =int(input("Enter your Choice :",))
    

    while True:
        match chioce:
            case 1:
                CheckAttendance()
            case 2:
                PartTime()
            case 3:
                Dailywage()
            case 4:
                monthlywage()
            case 5:
                exit()


if __name__ =="__main__": 
    main()