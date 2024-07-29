# Bank_Project_
 
# Bank Project

This my Bank Project for a REST based project it is a Django-based project that provides APIs for basic banking operations such as deposit, withdraw, transfer, and retrieving account statements (USING REST). It also includes dummy data generation for testing purposes.

## Features
- Account management
- Deposit and withdraw funds
- Transfer funds between accounts
- Retrieve account statements
- Generate dummy data for testing

## Technologies Used
- Django
- Django REST Framework
- SQLite (default database)
- Postman (for API testing)
- Faker (for dummy data generation)
### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps followed to achieve
1. **Clone the repository**
    ```bash
    git clone [https://github.com/Mr-Kommi/](https://github.com/Mr-Kommi/bank_project)
    
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create seed data**
    ```bash
    python manage.py generate_dummy_data
    ```

6. **Start the development server**
    ```bash
    python manage.py runserver
    ```

## Usage

### Running the Server
To start the server, run:
```bash
python manage.py runserver
```

### API Endpoints

#### Deposit Funds
- **URL:** `/api/deposit/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "iban": "DE8937040040443201300",
      "amount": 100
  }

#### Withdraw Funds
- **URL:** `/api/withdraw/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "iban": "DE8937040040443201300",
      "amount": 50
  }

#### Transfer Funds
- **URL:** `/api/transfer/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "from_iban": "DE8937040040443201300",
      "to_iban": "DE8937040040443201301",
      "amount": 30
  }

#### Retrieve Account Statement
- **URL:** `/api/statement/`
- **Method:** `GET`
- **Parameters:** `iban`, `sort` (asc/desc), `page`

#### List All Accounts
- **URL:** `/api/accounts/`
- **Method:** `GET`

#### List All Transactions
- **URL:** `/api/transactions/`
- **Method:** `GET`

#### List Transactions for an Account
- **URL:** `/api/transactions/<account_id>/`
- **Method:** `GET`
