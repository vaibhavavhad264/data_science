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
        return expenses


def fetch_by_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expenses(expense_date, amount, category, notes):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("insert into expenses (expense_date, amount, category, notes) values (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))

def delete_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("delete from expenses where expense_date = %s", (expense_date,))

def fetch_expense_summary(st_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, SUM(amount) AS total 
                       FROM expenses WHERE expense_date 
                       BETWEEN %s AND %s GROUP BY category;''',
                       (st_date, end_date))
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # exp = fetch_by_date("2024-08-03")
    # for expenses in exp:
    #     print(expenses)

    # insert_expenses("2024-08-20", 1200, "Food", "ICE-CREAM")
    # exp = fetch_by_date("2024-08-20")
    # print(exp)

    # delete_expenses_for_date("2024-08-20")
    # exp = fetch_by_date("2024-08-20")
    # print(exp)

    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for data in summary:
        print(data)





