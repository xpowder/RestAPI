# Project README

## Overview

This project is a Django-based web application with a RESTful API for managing customers, categories, products, and orders. It includes various views for handling CRUD operations and incorporates user permissions to restrict access to specific actions.

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST Framework

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd Project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    Pipenv Shell
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Customer Endpoints

- **GET /customers/**
  - Retrieves a list of all customers.
  - **Permissions:** Authenticated users.
  - **Response Format:** JSON or HTML.

### Category Endpoints

- **GET /categories/**
  - Retrieves a list of all categories.
  - **Permissions:** Public.

### Product Endpoints

- **GET /products/**
  - Retrieves a list of all products.
  - **Permissions:** Authenticated users.

- **POST /products/**
  - Creates a new product.
  - **Permissions:** Authenticated users with manager role.

### Product Detail Endpoints

- **GET /products/<id>/**
  - Retrieves details of a specific product.
  - **Permissions:** Authenticated users.

- **PUT /products/<id>/**
  - Updates a specific product.
  - **Permissions:** Authenticated users with manager role.

### Order Endpoints

- **GET /orders/**
  - Retrieves a list of all orders.
  - **Permissions:** Authenticated users.

- **PUT /orders/<id>/**
  - Updates a specific order.
  - **Permissions:** Authenticated users (owner of the order).

- **DELETE /orders/<id>/**
  - Deletes a specific order.
  - **Permissions:** Authenticated users (owner of the order).

### User Order Endpoints

- **GET /user/orders/**
  - Retrieves a list of orders for the authenticated user.
  - **Permissions:** Authenticated users.

- **PUT /user/orders/<id>/**
  - Updates a specific order for the authenticated user.
  - **Permissions:** Authenticated users (owner of the order).

- **DELETE /user/orders/<id>/**
  - Deletes a specific order for the authenticated user.
  - **Permissions:** Authenticated users (owner of the order).

## Permissions

- **IsAuthenticated:** Ensures the user is logged in.
- **IsManagerUser:** Custom permission that ensures the user is authenticated and has a 'manager' role.

## Serializers

- **CustomerSerializers:** Serializes customer data.
- **CategorySerializers:** Serializes category data.
- **ProductSerializers:** Serializes product data.
- **OrdersSerializers:** Serializes order data.

## Running Tests

To run tests, use the following command:

```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django
- Django REST Framework

For any queries, feel free to contact (kadmarmouad8@gmail.com).

---

This README provides an overview of the project, including setup instructions, API endpoints, permissions, serializers, and how to run tests. Adjust the URLs, email, and other details to match your project's specifics.
