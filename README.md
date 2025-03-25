# Flask Todo App

## Description
A simple Flask-based To-Do application that allows users to create, update, and delete tasks. The app uses SQLite as a database and renders HTML templates for UI.

## Features
- Add new tasks with a title and description
- View all tasks
- Update existing tasks
- Delete tasks
- SQLite database integration

## Technologies Used
- Python
- Flask
- SQLite
- SQLAlchemy
- HTML & CSS (for templates)

## Installation
### Clone the Repository
```bash
git clone <repo-url>
cd flask-todo-app
```

### Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Database Setup
```bash
flask shell
from app import db
db.create_all()
exit()
```

## Running the Application
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`

## Routes
- `GET /` - Display all tasks
- `POST /` - Add a new task
- `GET /update/<int:sno>` - Display update task form
- `POST /update/<int:sno>` - Update a task
- `GET /delete/<int:sno>` - Delete a task
- `GET /about` - About page

## Contribution
Feel free to fork this repository and submit pull requests.

## License
This project is open-source and available under the MIT License.

