# ETL Automation Testing Framework

This repository contains an ETL automation testing framework built using Python and pytest. The framework is designed to test ETL processes for accuracy, uniqueness, completeness, and consistency using automated test cases.

## Directory Structure

The project directory structure is organized as follows:

- `etl_auto_framework/`
  - `utilities/`: Contains utility scripts for database connections and test execution.
    - `db_conn.py`: Script for establishing a connection with MySQL database tables.
    - `run_test.py`: Script to execute test cases and generate HTML reports.
  - `tests/`: Contains pytest test cases for ETL testing.
    - Various Python test files (`test_accuracy.py`, `test_uniqueness.py`, `test_completeness.py`, `test_consistency.py`) implementing specific test scenarios.
  - `reports/`: Directory to store generated HTML reports.
    - (Reports will be generated and stored here if not previously generated.)

## Setup and Installation

### Requirements

Ensure you have Python and pip installed on your system. Use the following command to install project dependencies:

```bash
pip install -r requirements.txt
