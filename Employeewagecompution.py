'''
@Author: v sanjay kumar
@Date: 2024-07-30 03:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-30 03:00:30
@Title : 
'''
import random


def CheckAttendance():
    
    """
    Description:
    Function that check the attendence for employee.

    Parameters:
    - None.
    Returns:
    -None.
    """

    attendnce =random.choice((0,1))
    print(attendnce)

    if attendnce == 1:
        print(f"the employe is present")
    else:
        print(f"the employe is absent")
    



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
    print(Employee_daily_wage)


def PartTime():
    '''Description:
    Function that caluculate the part time employee wage.

    Parameters:
    - None.
    Returns:
    -None.
    '''
    wage_Hour = 20

    hours = 4

    Employee_Part_wage =wage_Hour* hours
    
    print(Employee_Part_wage)
