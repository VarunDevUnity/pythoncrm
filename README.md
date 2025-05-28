# Chaudhary CRM

## Project Overview

Chaudhary CRM is a simple web-based Lead Reminder and Follow-up system built with Django. It helps sales teams manage leads, track their progress through a pipeline, add follow-up notes, and manage users.

## Features

-   **User Authentication:** Secure Login and Signup for users.
-   **Lead Management:**
    -   Add New Leads with details like Name, Email, Phone, and Company.
    -   View a list of all Leads in a responsive table format.
    -   Add Follow-up notes and dates for each Lead.
    -   Last Follow-up date is automatically updated.
-   **Kanban Board:** Visual pipeline view of leads by their stage (New, Engaged, Proposal, Won, Lost).
-   **Status/Stage Update:** Update lead stage directly from both Table view (dropdown) and Kanban board (drag-and-drop).
-   **User Management:** (Admin Only)
    -   Add new users (employees).
    -   View, Edit, and Delete existing users.

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

**1. Clone the repository:**

```bash
git clone https://github.com/VarunDevUnity/pythoncrm.git
cd pythoncrm
```

**2. Create and activate a virtual environment:**

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**

```bash
pip install Django djangorestframework
```

**4. Run database migrations:**

```bash
python manage.py migrate
```

**5. Create a superuser (for Admin access):**

```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

**6. Run the development server:**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

1.  Navigate to `http://127.0.0.1:8000/` in your browser. You will be redirected to the login page.
2.  Sign up for a new account or log in with your superuser credentials.
3.  After logging in, you will see the Lead List page.
4.  Use the "Add New Lead" button to add leads.
5.  Use the "Switch to Kanban" button to toggle between Table View and Kanban Pipeline view.
6.  In Kanban view, drag and drop leads between columns to update their stage.
7.  In Table view, use the status dropdown to update lead stage.
8.  (Admin only) Use the "User Management" button to add, edit, or delete users.

--- 