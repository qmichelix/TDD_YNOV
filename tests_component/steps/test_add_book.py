from behave import given, when, then
import requests

@given('the system is ready to add books')
def step_impl(context):
    context.url = "http://localhost/books"

@when('I add a book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    response = requests.post(context.url, json={"title": title, "author": author})
    context.response = response


@then(u'the book should be added successfully')
def step_impl(context):
    print("Response status code:", context.response.status_code)
    print("Response body:", context.response.json())
    assert context.response.status_code == 201
