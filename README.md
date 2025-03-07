# TiDB Python Connector Examples

This repository contains example code demonstrating how to use TiDB with Python, specifically designed for [TiDB Labs](https://labs.tidb.io). The examples showcase various ways to interact with TiDB using two popular Python MySQL clients:

1. **MySQL Connector/Python**: The official MySQL driver for Python
2. **PyMySQL**: A pure Python MySQL client library

## Prerequisites

- Python 3.11 or later
- Poetry (Python package manager)
- Access to a TiDB database instance

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/tidb-lab-python.git
   cd tidb-lab-python
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Create a `.env` file in the root directory with your TiDB connection details:

   ```properties
   TIDB_HOST=your_tidb_host
   TIDB_PORT=4000
   TIDB_USER=your_username
   TIDB_PASSWORD=your_password
   TIDB_DB_NAME=your_database
   ```

## Examples

This repository includes examples demonstrating different aspects of working with TiDB using both MySQL Connector/Python and PyMySQL:

### MySQL Connector/Python Examples (`./mysql_connector_python_demo`)

The `mysql_connector_python_demo` directory contains examples using the official MySQL Connector/Python:

#### Basic Connection
- `demo_connection.py`: Shows how to establish a basic connection to TiDB with SSL verification

#### Query Examples
- `query_fetch_all.py`: Demonstrates how to fetch all rows from a query result
- `query_fetch_one.py`: Shows how to fetch a single row from a query result
- `positional_placeholders.py`: Examples of using positional placeholders in queries
- `named_placeholders.py`: Examples of using named placeholders in queries

#### Data Manipulation
- `batch_insert.py`: Shows how to perform efficient batch insertions
- `prepared_statement.py`: Demonstrates the use of prepared statements

### PyMySQL Examples (`./pymysql_demo`)

The `pymysql_demo` directory contains equivalent examples implemented using PyMySQL. These examples demonstrate the same functionality but use PyMySQL's API. The examples include:

- `demo_connection.py`: Basic connection example
- `query_fetch_all.py`: Fetching multiple rows
- `query_fetch_one.py`: Fetching single rows
- `positional_placeholders.py`: Using positional parameters
- `named_placeholders.py`: Using named parameters
- `batch_insert.py`: Batch insert operations

## Choosing Between MySQL Connector/Python and PyMySQL

- **MySQL Connector/Python**
  - Official MySQL driver
  - Full feature support including native prepared statements
  - Better performance with C extension
  - Larger installation size

- **PyMySQL**
  - Pure Python implementation
  - Lighter weight installation
  - Simpler API
  - Good for environments where installing C extensions is difficult
  - No native prepared statement support (emulated)

## Usage

Each example can be run directly using Python. For example:

```bash
# Run MySQL Connector/Python example
python mysql_connector_python_demo/demo_connection.py

# Run PyMySQL example
python pymysql_demo/demo_connection.py
```

## Project Structure

```bash
.
├── README.md
├── pyproject.toml          # Poetry project configuration
├── poetry.lock            # Poetry dependency lock file
├── .env                   # Environment variables (create this)
└── mysql_connector_python_demo/  # MySQL Connector/Python examples
│   ├── demo_connection.py       # Basic connection example
│   ├── query_fetch_all.py      # Fetch all rows example
│   ├── query_fetch_one.py      # Fetch single row example
│   ├── positional_placeholders.py  # Positional parameters
│   ├── named_placeholders.py   # Named parameters
│   ├── batch_insert.py         # Batch operations
│   └── prepared_statement.py   # Prepared statements
└── pymysql_demo/              # PyMySQL examples
    ├── README.md              # PyMySQL specific documentation
    ├── demo_connection.py     # Basic connection example
    ├── query_fetch_all.py     # Fetch all rows example
    ├── query_fetch_one.py     # Fetch single row example
    ├── positional_placeholders.py  # Positional parameters
    ├── named_placeholders.py   # Named parameters
    └── batch_insert.py         # Batch operations
```

## Dependencies

- `mysql-connector-python`: Official MySQL driver for Python
- `pymysql`: Pure Python MySQL client library
- `python-dotenv`: For loading environment variables from .env file

## Contributing

Feel free to submit issues and enhancement requests!
