# Eduyemek QA Automation Project

This project is a Selenium-based test automation project that includes automated testing processes for the [Eduyemek](https://www.eduyemek.com) web application.

## 📋 About the Project

This project is a web automation test project developed using the Page Object Model (POM) design pattern. It is designed to test the core functionalities of the Eduyemek platform.

### Tested Features

- ✅ User login
- ✅ Invalid login attempts
- ✅ Restaurant selection
- ✅ Menu selection
- ✅ Add items to cart

## 🏗️ Project Structure

```
eduyemek_qa/
├── configurations/
│   ├── __init__.py
│   └── config.ini                 # Test configuration file
├── logs/                          # Test logs
├── pages/                         # Page Object Model classes
│   ├── __init__.py
│   ├── login_page.py             # Login page
│   ├── user_page.py              # User page
│   └── usermain_page.py          # Main user page
├── reports/                       # Test reports
├── screenshots/                   # Test screenshots
├── test_data/                     # Test data
├── tests/                         # Test files
│   ├── __init__.py
│   ├── conftest.py               # Pytest configuration
│   ├── login_test.py             # Login tests
│   └── user_test.py              # User operation tests
├── utilities/                     # Utility tools
│   ├── __init__.py
│   └── read_properties.py        # Configuration reader
└── requirements.txt              # Python dependencies
```

## 🚀 Installation

### Requirements

- Python 3.7+
- Chrome browser
- Git

### Steps

1. **Clone the project:**

   ```bash
   git clone https://github.com/okancem/eduyemek_qa.git
   cd eduyemek_qa
   ```

2. **Create virtual environment (recommended):**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings:**
   Edit the `configurations/config.ini` file to enter your test information:

   ```ini
   [login info]
   login_url = https://www.eduyemek.com/account/login
   email = your-email@itu.edu.tr
   invalid_email = invalid@itu.edu.tr
   password = your-password

   [restaurant info]
   restaurant_name = Test Restaurant (BETA)
   ```

## 🧪 Running Tests

### Run all tests:

```bash
pytest
```

### Run specific test file:

```bash
# Only login tests
pytest tests/login_test.py

# Only user tests
pytest tests/user_test.py
```

### Run with HTML report:

```bash
pytest --html=reports/report.html
```

### Run in parallel:

```bash
pytest -n auto
```

### Run with Allure report:

```bash
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## 📊 Test Reports

The project supports the following reporting options:

- **HTML Reports**: Detailed HTML reports generated with `pytest-html`
- **Allure Reports**: Allure framework for rich visual reports
- **Screenshots**: Automatic screenshots for failed tests

## 🛠️ Technologies Used

- **Selenium WebDriver**: For web automation
- **Pytest**: Test framework
- **Page Object Model**: For test maintainability
- **WebDriver Manager**: For driver management
- **Allure**: For test reporting
- **OpenPyXL**: For Excel file operations

## 📝 Test Scenarios

### 1. Login Tests (`login_test.py`)

- **test_login**: Login with valid user credentials
- **test_invalid_login**: Login attempt with invalid user credentials

### 2. User Operation Tests (`user_test.py`)

- **test_add_to_basket**: Restaurant selection, menu selection, and adding items to cart

## 🔧 Configuration

Test settings are managed in the `configurations/config.ini` file:

- **Login URL**: Login page to be tested
- **Email/Password**: Test user credentials
- **Restaurant Name**: Restaurant name to be tested

## 📸 Screenshots

Failed tests are automatically saved to the `screenshots/` folder:

- `test_login_failed.png`
- `test_invalid_login_failed.png`
- `test_add_to_basket_failed.png`

## 📄 License

This project is licensed under the MIT License.

## 🔄 Updates

### v1.0.0

- Initial version
- Basic login and user operation tests
- Page Object Model implementation
- HTML and Allure reporting support

## 📧 Contact

Feel free to reach out if you want to discuss the project or ask questions! 

| Contact Channel | Information |
| :--- | :--- |
| **Email** | okancem1122@gmail.com |
| **LinkedIn** | https://www.linkedin.com/in/okan-cem/ |
