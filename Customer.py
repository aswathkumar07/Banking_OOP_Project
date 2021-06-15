# def load_to_json(original_func):
#     def wrapper_func(self, first_name, last_name, phone_no, email_id):
#         data = {}
#         data['customer'] = []
#         data['customer'].append({
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone_no': phone_no,
#             'email_id': email_id
#         })
#         with open('data.txt', 'a') as file:
#             json.dump(data, file)
#         return original_func(self, first_name, last_name, phone_no, email_id)
#     return wrapper_func

def load_to_db(original_func):
    def wrapper_func(self, first_name, last_name, phone_no, email_id):
        import sqlite3
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO customers VALUES (:first, :last, :phone, :email)", {
                      'first': first_name, 'last': last_name, 'phone': phone_no, 'email': email_id})
        return original_func(self, first_name, last_name, phone_no, email_id)
    return wrapper_func


class Customer:
    @load_to_db
    def __init__(self, first_name, last_name, phone_no, email_id):
        """Initializes instance of Customer class"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.email_id = email_id

    @staticmethod
    def update_phone_no(phone_no, first_name, last_name):
        """Gets phone_no from user and updates new value in customer database"""
        import sqlite3
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        with conn:
            c.execute("""UPDATE customers SET phone_no = :phone
                      WHERE first_name = :first AND last_name = :last""",
                      {'phone': phone_no, 'first': first_name, 'last': last_name})

    @staticmethod
    def update_email_id(email_id, first_name, last_name):
        """Gets email-id from user and updates new value in customer database"""
        import sqlite3
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        with conn:
            c.execute("""UPDATE customers SET email_id = :email
                      WHERE first_name = :first AND last_name = :last""",
                      {'email': email_id, 'first': first_name, 'last': last_name})

# Runs when a new user wants to register


def create_customer():
    """Gets first_name, last_name, phone_no and email-id as input from user"""
    f_name = input('Enter your first name: ')
    l_name = input('Enter your last name name: ')
    p_no = input('Enter your phone number: ')
    e_id = input('Enter your e-mail id: ')
    cust = Customer(f_name, l_name, p_no, e_id)
    print(
        f'Hello {cust.first_name} {cust.last_name}! You are now our valued customer')
