from Backend import db_helper
import os
import sys


def test_fetch_expense_for_date():
    expense = db_helper.fetch_by_date("2024-08-15")
    assert len(expense) == 1
    assert expense[0]['amount'] == 10.0
    assert expense[0]['category'] == "Shopping"
    assert expense[0]['notes'] == "Bought potatoes"

def test_fetch_expense_for_data_aug15():
    expense = db_helper.fetch_by_date("2024-08-15")
    assert len(expense) == 1
    assert expense[0]['amount'] == 10.0
    assert expense[0]['category'] == "Shopping"
    assert expense[0]['notes'] == "Bought potatoes"

def test_fetch_expense_for_date_invalid_date():
    expense = db_helper.fetch_by_date("2080-08-15")
    assert len(expense) == 0

def test_fetch_expense_summary_invalid_range():
    exp = db_helper.fetch_expense_summary("2080-08-15", "2080-08-25" )
    assert len(exp) == 0
