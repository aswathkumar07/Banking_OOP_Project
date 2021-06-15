# import sqlite3

# conn1 = sqlite3.connect('employee.db')
# conn2 = sqlite3.connect('customer.db')

# c = conn1.cursor()
# d = conn2.cursor()
# c.execute("""CREATE TABLE employees(
#     first_name text,
#     last_name text,
#     phone_no text,
#     email_id text,
#     salary float,
#     branch text)"""
#           )

# conn1.commit()

# d.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     phone_no text,
#     email_id text)"""
#           )
# conn2.commit()

# conn1.close()
# conn2.close()
