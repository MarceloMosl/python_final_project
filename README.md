# Personal Finance Tracker

The **Personal Finance Tracker** app helps users manage their financial transactions, budgets, and spending habits effectively. It includes features for tracking transactions, setting budgets, analyzing spending patterns, and visualizing financial data.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
  - [Using the Command Line](#using-the-command-line)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description
The **Personal Finance Tracker** app is a Python-based application designed to help users manage their finances. It provides functionalities for adding, editing, and deleting transactions, setting and managing budgets, and generating data visualizations for financial insights.

## Features
- Add, edit, and delete transactions.
- Set income and budget goals with customizable alerts.
- Analyze spending habits by category.
- Generate visual reports such as line, bar, and pie charts.

## Installation and Setup
To set up the project, follow one of the methods below:

### Using the Command Line
1. **Clone the repository**:
   ```bash
   git clone https://github.com/MarceloMosl/python_final_project
   cd python_final_project


### Usage
**Activate the virtual environment**:
  ```bash
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
  ```

**Run the app using the main.py file**:
```
  python main.py
```

## Project Structure
**How its set up**:

    personal-finance-tracker/
    ├── src/                         # Source code directory
    │   ├── main.py                  # Main script to run the app
    │   ├── functions/               # Directory for function modules
    │   │   ├── csv_functions/       # Functions for handling CSV operations
    │   │   ├── data_management/      # Functions for managing data
    │   │   ├── data_visualization/   # Functions for visualizing data
    │   │   ├── spending_analysis/    # Functions for spending analysis
    │   │   ├── common.py             # Common utilities for the app
    │   │   └── switcher.py          # Switcher functionality for the app
    ├── requirements.txt              # List of dependencies
    ├── .gitignore                   # Excludes unnecessary files/folders (e.g., pycache, venv/)
    └── README.md                    # Project documentation




## Contributing
**To contribute to this project**:
  1. Fork the repository:

  2. Create a feature branch (`git checkout -b feature-branch-name`).
  3. Commit your changes (git commit -m "Add feature") and push to the branch (`git push origin feature-branch-name`).
  4. Create a Pull Request to merge your changes.



## License

**No License**:
  Go crazy do whatever you want. :D