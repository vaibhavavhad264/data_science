import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")


@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Pass@123",
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary = True)
    try:
        yield cursor
        connection.commit()      # <-- This is required
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

def fetch_by_date(expense_date):
    logger.info(f"Fetching expense by date {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"Insert expense by date: {expense_date}, amount : {amount}, category : {category}, notes : {notes}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("insert into expenses (expense_date, amount, category, notes) values (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))

def delete_expenses_for_date(expense_date):
    logger.info(f"Delete expense by date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("delete from expenses where expense_date = %s", (expense_date,))


def fetch_expense_summary(st_date, end_date):
    logger.info(f"Fetching expense summary by date {st_date} and end date {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, SUM(amount) AS total 
                       FROM expenses WHERE expense_date 
                       BETWEEN %s AND %s GROUP BY category;''',
                       (st_date, end_date))
        data = cursor.fetchall()
        return data

if __name__ == "__main__":

    exp = fetch_by_date("2024-08-01")
    print(exp)
    delete_expenses_for_date("2024-08-25")
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for data in summary:
        print(data)


    # insert_expenses("2024-08-20", 1200, "Food", "ICE-CREAM")
    # exp = fetch_by_date("2024-08-20")
    # print(exp)
    #

    # exp = fetch_by_date("2024-08-20")
    # print(exp)

    # summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    # for data in summary:
    #     print(data)





