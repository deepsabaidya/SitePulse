# SitePulse – Website Uptime Monitoring System

**A Python-based DevOps Mini Project**

SitePulse is a web-based website uptime monitoring system developed using Python and Flask. It allows users to monitor the availability of websites, measure their response time, maintain monitoring history, and visualize website performance through an interactive dashboard.

The project demonstrates the practical implementation of software development and DevOps concepts, including version control, database integration, automated testing, and Continuous Integration (CI) using Jenkins.

---

## 1. Project Overview

Website availability and response time are important factors in maintaining a reliable online presence. Websites may become temporarily unavailable due to server failures, network issues, or other technical problems.

SitePulse provides a simple monitoring solution that enables users to:

- Add websites for monitoring.
- Check whether a website is accessible.
- Identify website availability using UP and DOWN status.
- Measure HTTP response time.
- Store monitoring results in a database.
- Calculate website uptime percentage.
- View historical monitoring records.
- Visualize response-time trends through graphical charts.

The application provides a centralized dashboard for monitoring multiple websites.

## 2. Objectives

The main objectives of SitePulse are:

1. To develop a functional website monitoring application using Python and Flask.
2. To check website availability through HTTP requests.
3. To measure and record website response time.
4. To store website details and monitoring history using SQLite.
5. To calculate uptime statistics based on monitoring records.
6. To display monitoring information through an interactive dashboard.
7. To implement version control using Git and GitHub.
8. To perform automated application testing using Pytest.
9. To demonstrate a Continuous Integration workflow using Jenkins.

## 3. Key Features

### Website Monitoring
Users can add multiple website URLs and manually initiate availability checks.

### UP/DOWN Status Detection
The application identifies whether a website is accessible based on its HTTP response status.

- **UP:** HTTP response status between 200 and 399.
- **DOWN:** HTTP response status outside the accepted range or a connection/request failure.

### Response Time Measurement
SitePulse measures the time taken to receive an HTTP response and records it in milliseconds.

### Uptime Calculation
The system calculates uptime percentage using successful monitoring checks.

**Formula:**

Uptime (%) = (Successful Checks / Total Checks) × 100

### Monitoring History
Every monitoring result is stored in SQLite, allowing users to view previous checks, response codes, response times, timestamps, and errors.

### Interactive Dashboard
The dashboard displays:

- Total monitored websites.
- Total monitoring checks.
- Website uptime percentage.
- Average response time.
- Response-time history charts.

### Automated Testing
Pytest is used to test URL validation, website availability, HTTP responses, and connection failures.

### Continuous Integration
Jenkins is used to automate source-code checkout, Python environment setup, dependency installation, and automated testing.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive user interface |
| JavaScript | Dashboard interactions |
| Chart.js | Response-time visualization |
| SQLite | Database management |
| Requests | HTTP requests and website checks |
| Git | Version control |
| GitHub | Source-code repository |
| Pytest | Automated testing |
| Jenkins | Continuous Integration |
| Docker | Optional containerization extension |

## 5. System Architecture

SitePulse follows a modular application structure.

**Application workflow:**

1. The user enters a website URL through the dashboard.
2. Flask receives the request and validates the URL.
3. The monitoring module sends an HTTP request to the target website.
4. The application measures response time and determines the website status.
5. The monitoring result is stored in the SQLite database.
6. The dashboard retrieves stored information and calculates statistics.
7. Chart.js displays response-time history graphically.

**DevOps workflow:**

1. Source code is maintained in GitHub.
2. Jenkins checks out the project repository.
3. Jenkins creates a Python virtual environment.
4. Project dependencies are installed.
5. Pytest executes automated test cases.
6. The pipeline reports whether the tests have passed or failed.

## 6. Project Directory Structure

```text
SitePulse/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── monitor.py
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── dashboard.js
│
├── tests/
│   └── test_monitor.py
│
├── requirements.txt
├── run.py
├── Jenkinsfile
├── .gitignore
└── README.md
```

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or later.
- Git.
- A code editor such as Visual Studio Code.
- Internet connectivity for checking external websites.

### Step 1: Clone the Repository

```bash
git clone <https://github.com/deepsabaidya/SitePulse>
```

### Step 2: Navigate to the Project Directory

```bash
cd SitePulse
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Linux or GitHub Codespaces:

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python run.py
```

Open the local application using the URL displayed in the terminal or the forwarded port provided by GitHub Codespaces.

## 8. Dependencies

The project uses the following Python packages:

```text
Flask
requests
pytest
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 9. Running Automated Tests

SitePulse uses Pytest to verify the functionality of its website monitoring module.

Execute the following command:

```bash
python -m pytest tests/ -v
```

The test suite covers:

- Valid HTTP and HTTPS URL validation.
- Invalid URL handling.
- Successful website checks.
- HTTP error response handling.
- Connection failure handling.

Pytest provides a detailed execution report showing passed and failed test cases.

## 10. Jenkins Continuous Integration Pipeline

The project uses a Jenkinsfile to define its CI pipeline.

The pipeline contains the following stages:

| Stage | Description |
|---|---|
| Checkout | Retrieves the source code from GitHub. |
| Setup Python | Creates a virtual environment and installs dependencies. |
| Run Tests | Executes automated tests using Pytest. |
| Build | Completes the application build stage. |

The pipeline helps automate repetitive development tasks and provides early feedback when changes introduce errors.

## 11. Database Design

SitePulse uses SQLite for persistent storage.

The database contains two main tables:

### Websites

Stores the websites registered for monitoring.

| Column | Description |
|---|---|
| id | Unique website identifier |
| url | Website URL |
| created_at | Date and time of registration |

### Monitoring History

Stores the results of individual website checks.

| Column | Description |
|---|---|
| id | Unique monitoring record ID |
| website_id | Associated website identifier |
| status | UP or DOWN |
| status_code | HTTP response status code |
| response_time_ms | Response time in milliseconds |
| error | Error details, if applicable |
| checked_at | Monitoring timestamp |

A foreign key connects monitoring history records with their corresponding website entries.

## 12. Expected Output

The application provides a dashboard where users can:

- Register websites for monitoring.
- Trigger manual availability checks.
- View website uptime percentages.
- Review average response times.
- Access historical monitoring records.
- Analyze response-time trends through charts.

The system provides a simple interface for observing website availability and performance over multiple checks.

## 13. Limitations

- Website checks are initiated manually by the user.
- Automatic periodic monitoring is not currently implemented.
- Notifications and alerting mechanisms are not included.
- Uptime calculations are based on recorded checks rather than continuous real-world availability.
- SQLite is used for local project data storage.
- The Jenkins pipeline requires a configured Jenkins environment and compatible agent.

## 14. Future Enhancements

Possible future improvements include:

- Automatic scheduled website monitoring.
- Email notifications for website downtime.
- Response-time threshold alerts.
- User authentication and role management.
- More detailed performance analytics.
- Docker-based containerization.
- Support for additional database systems.

## 15. Conclusion

SitePulse demonstrates the development of a functional website monitoring application while integrating important DevOps practices.

The project combines Python-based application development, database management, version control, automated testing, and Continuous Integration into one practical implementation.

Through this project, concepts such as Git, GitHub, Pytest, Jenkins, and modular application development are applied to a real-world monitoring use case.

SitePulse provides a foundation for understanding how software development and DevOps workflows can work together to improve application reliability, maintainability, and testing efficiency.

---

**Project Name:** SitePulse – Website Uptime Monitoring System  
**Project Type:** DevOps Mini Project  
**Primary Language:** Python  
**Framework:** Flask  
**Database:** SQLite  
**Development Environment:** GitHub Codespaces
