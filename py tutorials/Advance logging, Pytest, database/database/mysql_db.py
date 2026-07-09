import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Pass@123",
        database = "expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Connection Failed")

    cursor = connection.cursor(dictionary = True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses")
        expenses = cursor.fetchall()
        for exp in expenses:
            print(exp)


def fetch_by_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for exp in expenses:
            print(exp)

def insert_expenses(expense_data, amount, category, data):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("insert into expenses (expense_data, amount, category, data) values (%s, %s, %s, %s)",
                       (expense_data, amount, category, data)
                       )

def delete_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("delete from expenses where expense_date = %s", (expense_date,))


if __name__ == "__main__":
    # fetch_all_records()
    #fetch_by_date("2024-08-03")
    insert_expenses("2024-08-20", 200, "Food", "Panipuri")
    print("##########Fetched##########")
    fetch_by_date("2024-08-03")
    print("##########Deleted##########")
    delete_expenses_for_date("2024-08-03")
    print("##########Fetched##########")
    fetch_by_date("2024-08-03") 

