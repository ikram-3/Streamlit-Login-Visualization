import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            st.error(f"Database error: {err}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def init_db(self):
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(50) NOT NULL
            )
        ''')
        self.conn.commit()
        self.disconnect()

    def add_user(self, username, password):
        self.connect()
        self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        self.conn.commit()
        self.disconnect()

    def authenticate(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = self.cursor.fetchone()
        self.disconnect()
        return user is not None

db_handler = DatabaseHandler("localhost", "root", "ikram", "login")
db_handler.init_db()

st.title("Advanced Streamlit Login with Data Visualization")

# Login Section
st.sidebar.header("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if db_handler.authenticate(username, password):
        st.session_state.logged_in = True
        st.sidebar.success("Logged in successfully!")
    else:
        st.sidebar.error("Invalid username or password")

# Main App (only accessible after login)
if st.session_state.get("logged_in", False):
    st.header("Welcome to the Data Visualization App")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data")
        st.dataframe(df)

        # Plot selection
        st.write("### Select Plot Type")
        plot_type = st.selectbox("Choose a plot type", ["Line Plot", "Bar Plot", "Scatter Plot", "Histogram"])

        # Plotting
        if plot_type == "Line Plot":
            st.write("### Line Plot")
            columns = df.columns
            x_axis = st.selectbox("Select X-axis", columns)
            y_axis = st.selectbox("Select Y-axis", columns)
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif plot_type == "Bar Plot":
            st.write("### Bar Plot")
            columns = df.columns
            x_axis = st.selectbox("Select X-axis", columns)
            y_axis = st.selectbox("Select Y-axis", columns)
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif plot_type == "Scatter Plot":
            st.write("### Scatter Plot")
            columns = df.columns
            x_axis = st.selectbox("Select X-axis", columns)
            y_axis = st.selectbox("Select Y-axis", columns)
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif plot_type == "Histogram":
            st.write("### Histogram")
            columns = df.columns
            x_axis = st.selectbox("Select Column", columns)
            plt.figure(figsize=(10, 6))
            sns.histplot(data=df, x=x_axis, kde=True)
            st.pyplot(plt)

# Logout Button
if st.session_state.get("logged_in", False):
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.sidebar.success("Logged out successfully!")
