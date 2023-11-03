import time
from behave import given, when, then

from basic_maths_gui import MyApp  # Import GUI application

@given("I launch the Basic Math GUI")
def launch_app(context):
    context.app = MyApp()  # Instantiate GUI application
    context.app.show()
    time.sleep(1)  # Adjust this time as needed for GUI to load

@when('I enter "{value}" into the first input field')
def enter_value_into_first_input(context, value):
    context.app.enter_value_into_first_input(value)

@when('I enter "{value}" into the second input field')
def enter_value_into_second_input(context, value):
    context.app.enter_value_into_second_input(value)

@when('I select "{operator}" from the operator dropdown')
def select_operator(context, operator):
    context.app.select_operator(operator)

@when('I click the "Calculate" button')
def click_calculate(context):
    context.app.click_calculate()

@then('I should see "{expected_result}" as the result')
def verify_result(context, expected_result):
    result = context.app.get_result()
    assert result == expected_result, f"Expected result: {expected_result}, Actual result: {result}"

@then('I should see an error message')
def verify_error_message(context):
    error_message = context.app.get_error_message()
    assert "Invalid input" in error_message
