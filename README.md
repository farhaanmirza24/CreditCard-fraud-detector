<img width="1470" height="832" alt="Screenshot 2026-07-17 at 6 57 32 PM" src="https://github.com/user-attachments/assets/684df654-9fd4-4c57-898b-90642eb606a1" />
<img width="1470" height="834" alt="credit-card" src="https://github.com/user-attachments/assets/6a136f29-5369-437d-887d-50c68bcc6b38" />
# Identifying Fraudulent Credit Card Transactions Using Ensemble Learning

This project implements a web-based application for identifying fraudulent credit card transactions using Ensemble Learning techniques. It provides a platform where users can log in, view transaction data, and predict whether transactions are fraudulent or legitimate.

## Overview

Based on research related to *IEEE Transaction Access on Machine Learning* (Volume: 12, Issue Date: 23 April 2024), this system utilizes machine learning—specifically ensemble learning methods—to tackle credit card fraud detection in Fintech. It leverages both simulated and real-world datasets for comprehensive training and testing.

## Features

The system is divided into two main roles: **Remote User** and **Service Provider**.

### Remote User
*   **Authentication**: Secure login and registration for users.
*   **Profile Management**: Ability to view and manage user profile details.
*   **Fraud Detection**: Interface to input or upload transaction details to detect fraudulent activities.

### Service Provider (Admin)
*   **Authentication**: Dedicated service provider login.
*   **User Management**: View and monitor registered remote users.
*   **Model Training & Data Management**: Train and test datasets for the machine learning models.
*   **Analytics & Charts**: 
    *   View detected fraudulent transactions categorized by type.
    *   View the ratio of fraudulent to non-fraudulent transactions using interactive charts.
*   **Data Export**: Download predicted datasets for further analysis.

## Dataset Features

The models analyze the following transaction attributes to make predictions:
*   `Fid`: Fraud ID
*   `Trans_Date`: Transaction Date
*   `CC_No`: Credit Card Number
*   `CC_type`: Credit Card Type
*   `Trans_Type`: Transaction Type
*   `Amount`: Transaction Amount
*   `Firstname` & `Lastname`: Cardholder's Name
*   `Gender`: Cardholder's Gender
*   `Age`: Cardholder's Age
*   `lat` & `lon`: Geographical coordinates of the transaction
*   `Transid`: Transaction ID
*   `Prediction`: Fraud prediction outcome

## Technology Stack

*   **Backend Framework**: Django (Python)
*   **Machine Learning**: Python-based Ensemble Learning models
*   **Frontend**: HTML, CSS, JavaScript (via Django Templates)
*   **Database**: SQLite/MySQL (configured in Django settings)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Identifying-Fradulent-Credit-Card-Transactions-Using-Ensemble-Learning-main
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Navigate to the project directory:**
   ```bash
   cd Identifying_Fraudulent/Identifying_Fraudulent
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.
