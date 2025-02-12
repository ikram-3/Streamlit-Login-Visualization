# Advanced Streamlit Login with Data Visualization
This repository contains a Python application built using Streamlit that provides a secure login system and allows users to upload CSV files for data visualization. The application integrates with a MySQL database for user authentication and offers various plotting options using Seaborn and Matplotlib.

## Features

- **User Authentication**: Secure login system using a MySQL database to store and authenticate user credentials.
- **CSV File Upload**: Users can upload CSV files to visualize data.
- **Data Visualization**: Supports multiple plot types including Line Plot, Bar Plot, Scatter Plot, and Histogram.
- **Interactive Interface**: Built with Streamlit for an interactive and user-friendly interface.

## Requirements

To run this application, you need the following Python packages installed:

- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `mysql-connector-python`

You can install these packages using pip:

```bash
pip install streamlit pandas matplotlib seaborn mysql-connector-python
```

## Setup

1. **Database Configuration**:
   - Ensure you have MySQL installed and running.
   - Create a database named `login` (or any name you prefer).
   - Update the `DatabaseHandler` class initialization in the code with your MySQL credentials:
     ```python
     db_handler = DatabaseHandler("localhost", "root", "your_password", "login")
     ```

2. **Initialize the Database**:
   - Run the application once to initialize the database and create the `users` table.

3. **Run the Application**:
   - Use the following command to run the Streamlit application:
     ```bash
     streamlit run your_script_name.py
     ```

## Usage

1. **Login**:
   - Enter your username and password in the sidebar to log in.
   - If you don't have an account, you can add a new user by modifying the code to include a registration feature.

2. **Upload CSV**:
   - After logging in, upload a CSV file using the file uploader.

3. **Visualize Data**:
   - Select the type of plot you want to generate from the dropdown menu.
   - Choose the appropriate columns for the X-axis and Y-axis (if applicable).
   - The selected plot will be displayed.

4. **Logout**:
   - Use the logout button in the sidebar to log out of the application.

## Example

Here is a quick example of how to use the application:

1. Log in with your credentials.
2. Upload a CSV file containing data.
3. Select "Line Plot" from the dropdown menu.
4. Choose the appropriate columns for the X-axis and Y-axis.
5. View the generated line plot.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
