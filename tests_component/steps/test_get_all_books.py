from behave import given, when, then
import requests

@given('the system is ready to list books')
def step_impl(context):
    context.url = "http://127.0.0.1:5000/books"

@when('I request the list of books')
def step_impl(context):
    response = requests.get(context.url)
    context.response = response

@then('I should receive a list of books')
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)
