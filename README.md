# ETL Automation Testing Framework

This repository contains an ETL automation testing framework built using Python and pytest. The framework is designed to test ETL processes for accuracy, uniqueness, completeness, and consistency using automated test cases.

## 1. Introduction

The ETL Automation Testing Framework is designed to ensure the integrity, accuracy, and reliability of ETL processes by automating the testing of data transformations. Built using Python and pytest, this framework facilitates comprehensive testing of ETL workflows, providing detailed reports on data quality and consistency.

## 2. Objectives

- **Automate ETL Testing**: Reduce manual effort in testing ETL processes by automating the validation of data transformations.
- **Ensure Data Quality**: Verify the accuracy, uniqueness, completeness, and consistency of data.
- **Provide Detailed Reporting**: Generate and store HTML reports to document test results.

## 3. Project Structure

The framework is organized into the following directory structure:

- `etl_auto_framework/`
  - `utilities/`
    - `db_conn.py`: Manages connections to MySQL databases, facilitating access to source and target tables for testing.
    - `run_test.py`: Executes pytest test cases, generates HTML reports, and ensures reports are stored in the `reports/` directory.
  - `tests/`
    - `test_accuracy.py`: Contains tests to verify the accuracy of data transformations.
    - `test_uniqueness.py`: Ensures that data remains unique after transformation.
    - `test_completeness.py`: Verifies that all expected data is present in the target tables.
    - `test_consistency.py`: Checks for data consistency across various stages of the ETL process.
  - `reports/`: Stores the generated HTML reports documenting test results.
  - `requirements.txt`: Lists the Python dependencies required for the framework.

## 4. Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd etl_auto_framework

#### Install the required dependencies:
bash

pip install -r requirements.txt
5. Running the Tests
To execute the ETL test cases, run the test runner script:

bash
```
python utilities/run_test.py
````
This script will:

Establish a connection to the MySQL database.
Execute all pytest test cases located in the tests/ directory.
Generate an HTML report and save it to the reports/ directory.

### 6. Test Scenarios
The framework includes the following test scenarios:

#### 1) Accuracy Testing:

* Validates that data has been accurately transformed.
* Example: Ensuring that numerical calculations or data mappings are correct.
* Uniqueness Testing:

Checks that duplicate data does not exist after transformation.
Example: Ensuring that primary keys remain unique.

#### 2)Completeness Testing:

Verifies that all expected data is loaded into the target tables.
Example: Ensuring no records are missing.
Consistency Testing:

Ensures data consistency across different stages of the ETL process.
Example: Ensuring that data format and values remain consistent.

#### 7. Reporting
The framework generates detailed HTML reports after each test execution. These reports provide a summary of test results, including:

Number of tests executed
Test status (pass/fail)
Detailed logs and error messages for failed tests

#### 8. Contributing
We welcome contributions! To contribute to this project:

#### Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your branch.
Submit a pull request with a detailed description of your changes.
