# Book List Management Application

This project is a simple Python application to manage a list of books, demonstrating a clean architecture and Test-Driven Development (TDD) approach.

## Project Structure

The project follows a hexagonal architecture organized as follows:

  - `APP/`: Contains the application logic separated into models and services.
  - `MODEL/`: Contains the data models, e.g., the `Book` class.
  - `USESCASES/`: Contains the use cases, e.g., cases for creating and listing books.
  - `DOMAIN/`: Contains domain interfaces, defining operations that can be performed on data, like a `BookInterface` for data persistence.
  - `INFRA/`: Contains implementations of domain interfaces, like `BookRepository` which interacts with the database.
  - `TEST/`: Contains all unit tests, e.g., `test_book.py` for testing the logic of the `Book` class and associated services.
domain - > model / port / usecases (tests)
## Models

### Book

The `Book` class represents a book with a title and an author. Both fields are required.

## Manager

### BookManager

The `BookManager` class provides methods to add a new book and list all books.

#### Methods

- `add_book(title, author)`: Adds a new book to the list. Both the title and author must be non-empty strings.
- `list_books()`: Returns a list of all books, sorted alphabetically by title.

## Domain Interfaces

### BookRepositoryInterface

An interface for book persistence, which can be implemented for any kind of database.

#### Methods

- `add_book(book)`: Persists a new book.
- `list_books()`: Retrieves all books.

## Testing

Tests are written using `pytest` and follow the TDD approach. Property-based tests are also included using the `hypothesis` library.

### Unit Tests

- `test_create_book_with_title_and_author()`: Ensures a book can be created with a title and an author.
- `test_create_book_without_title_should_raise_error()`: Ensures that creating a book without a title raises a `ValueError`.
- `test_create_book_without_author_should_raise_error()`: Ensures that creating a book without an author raises a `ValueError`.
- `test_add_book()`: Tests adding a book to the repository.
- `test_list_books_in_alphabetical_order()`: Tests that books are listed in alphabetical order by title.

### Property-Based Tests

- `test_create_book_with_non_empty_title_and_author()`: Property test ensuring that books with non-empty titles and authors are always valid.
- `test_list_books_in_alphabetical_order()`: Property test ensuring that books are always listed in alphabetical order, regardless of the order they were added.
- `test_list_books_has_no_duplicates()`: Property test ensuring that the list of books contains no duplicates.

## Continuous Integration and Deployment

CI/CD is handled through GitHub Actions which runs tests on every push and pull request to the main branch.

## How to Use

To set up the project:

1. Clone the repository.
2. Create a virtual environment. `conda env create -f environment.yml`
3. Active it `conda activate booklist_project`.
4. Run tests using `pytest -v` in the root directory.




[![codecov](https://codecov.io/gh/Jonathan2433/Book_Store/branch/master/graph/badge.svg?token=1087475e-4ba4-48a4-8d26-51cdf36f979a)](https://codecov.io/gh/Jonathan2433/Book_Store)



![image](https://github.com/qmichelix/TDD_YNOV/assets/109591838/1769e850-8250-4a87-987b-68c4c738f17c)

Le build s'est fait en 2mins et 28 secondes en passant tous les tests :D à la 237ème execution du workflow.
