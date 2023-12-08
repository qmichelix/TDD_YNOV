Feature: Book management

  Scenario: Add a new book
    Given the system is ready to add books
    When I add a book with title "1984" and author "George Orwell"
    Then the book should be added successfully

  Scenario: Retrieve all books
    Given the system has books
    When I request a list of all books
    Then I should receive a list containing all books
