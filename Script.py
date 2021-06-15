from Employee import Employee
from Customer import Customer, create_customer
from Banking_Services import BankAccount
import logging

logger = logging.getLogger(__name__)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Update customer details


def update_customer_details():
    """Get first and last name from user and asks the user if he wants to update phone_number or email-id"""
    first_name = input('What is your first name:\n')
    last_name = input('What is your last name:\n')
    print('Select the relevant option:')
    update_sel = input('1. Phone number\n2. Email ID\n')
    if update_sel == '1':
        phone_number = input('Enter your new phone number: ')
        Customer.update_phone_no(phone_number, first_name, last_name)
    elif update_sel == '2':
        e_mail_id = input('Enter your new e-mail id: ')
        Customer.update_email_id(e_mail_id, first_name, last_name)
    else:
        logger.error(
            f'Customer entered {update_sel} in update personal details screen')
        print('Invalid entry. Please try again.')

# Update employee details


def update_employee_details():
    """Get first and last name from user and asks the user if he wants to update phone_number or email-id"""
    first_name = input('What is your first name:\n')
    last_name = input('What is your last name:\n')
    print('Select the relevant option:')
    update_sel = input('1. Phone number\n2. Email ID\n')
    if update_sel == '1':
        phone_number = input('Enter your new phone number: ')
        Employee.update_phone_no(phone_number, first_name, last_name)
    elif update_sel == '2':
        e_mail_id = input('Enter your new e-mail id: ')
        Employee.update_email_id(e_mail_id, first_name, last_name)
    else:
        logger.error(
            f'Employee entered {update_sel} in update personal details screen')
        print('Invalid entry. Please try again.')


# Execution start
print('Hello User!')
user_sel = input(
    'Enter the relevant option:\n1. New user\n2. Returning user\n3. Employee\n')

# For new users to create a profile with first_name,last_name, etc.
if user_sel == '1':
    create_customer()
elif user_sel == '2':  # For returning users who already have an account
    returning_user_sel = input(
        'Enter the relevant option:\n1. Update Personal Details\n2. Deposit amount\n3. Withdraw amount\n')
    if returning_user_sel == '1':
        update_customer_details()
    elif returning_user_sel == '2':
        amt = input('Enter deposit amount:\n')
        BankAccount.deposit(amt)
    elif returning_user_sel == '3':
        with_drw = input('Enter withdrawal amount:\n')
        BankAccount.withdraw(with_drw)
    else:
        logger.error(
            f'User entered {returning_user_sel} in returning user screen')
        print('Invalid Entry. Please try again.')
elif user_sel == '3':
    employee_user_sel = input(
        'Enter the relevant option:\n1. Update Personal Details:')
    if employee_user_sel == '1':
        update_employee_details()
    else:
        logger.error(
            f'User entered {employee_user_sel} in employee user screen')
        print('Invalid Entry. Please try again.')
else:
    logger.error(f'User entered {user_sel} in welcome screen')
    print('Invalid entry. Please try again.')
