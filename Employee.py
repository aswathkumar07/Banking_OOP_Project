def load_to_db(original_func):
    def wrapper_func(self, first_name, last_name, phone_no, email_id):
        import sqlite3
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO employees VALUES (:first, :last, :phone, :email)", {
                      'first': first_name, 'last': last_name, 'phone': phone_no, 'email': email_id})
        return original_func(self, first_name, last_name, phone_no, email_id)
    return wrapper_func


class Employee:
    @load_to_db
    def __init__(self, first_name, last_name, phone_no, email_id, branch, salary):
        """Initializes instance of Employee class"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.email_id = email_id
        self.branch = branch
        self.salary = salary

    def update_phone_no(self, phone_no, first_name, last_name):
        """Gets new phone_no from user and updates value in customer database"""
        self.phone_no = phone_no
        import sqlite3
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        with conn:
            c.execute("""UPDATE employees SET phone_no= :phone
                      WHERE first_name = :first AND last_name = :last""",
                      {'phone': phone_no, 'first': first_name, 'last': last_name})

    def update_email_id(self, email_id, first_name, last_name):
        """Gets new email-id from user and updates value in customer database"""
        self.email_id = email_id
        import sqlite3
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        with conn:
            c.execute("""UPDATE employees SET email_id= :email
                      WHERE first_name = :first AND last_name = :last""",
                      {'email': email_id, 'first': first_name, 'last': last_name})
