This is a RESTful API project built using Django REST Framework that allows you to manage Companies and their Employees. The project demonstrates basic CRUD operations, relationships between models, and the use of DRF for building scalable backend APIs.

🚀 Features
Create, Retrieve, Update, and Delete Companies

Create, Retrieve, Update, and Delete Employees

Each Employee is associated with a Company (ForeignKey relationship)

Clean and modular code structure

Django Admin for managing data

API tested with tools like Postman or cURL

🧱 Tech Stack
Python 3

Django

Django REST Framework

SQLite (default) or any supported database

Postman (for testing)

📁 API Endpoints Example
Companies
GET /api/v1/companies/ – List all companies

POST /api/v1/companies/ – Create a new company

GET /api/v1/companies/<id>/ – Retrieve a company

PUT /api/v1/companies/<id>/ – Update a company

DELETE /api/v1/companies/<id>/ – Delete a company

Employees
GET /api/v1/employees/ – List all employees

POST /api/v1/employees/ – Create a new employee

GET /api/v1/employees/<id>/ – Retrieve an employee

PUT /api/v1/employees/<id>/ – Update an employee

DELETE /api/v1/employees/<id>/ – Delete an employee