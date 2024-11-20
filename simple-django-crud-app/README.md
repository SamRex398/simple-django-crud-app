# Backend Intern Assessment: CRUD Notes API in Django


### Objective
The goal of this assessment is to build a Notes API in Django with Create, Read, Update, and Delete (CRUD) functionality, along with basic authentication.

### Requirements
  #### Setup
  Create a Django project and a notes app.
  Use Django REST Framework to implement the API endpoints listed below.
  API Endpoints
  POST /notes/

#### Description: Creates a new note.
Fields: title (string), content (string), timestamp (datetime, auto-generated).
Example:
bash
```
curl -X POST -H "Authorization: Token <your_token>" -H "Content-Type: application/json" -d '{"title": "Sample Note", "content": "This is a note."}' http://localhost:8000/notes/
```
GET /notes/

#### Description: Retrieves a list of all notes.
Example:
bash
```
curl -X GET -H "Authorization: Token <your_token>" http://localhost:8000/notes/
```
GET /notes/{id}/

#### Description: Retrieves a specific note by its ID.
Example:
bash
```
curl -X GET -H "Authorization: Token <your_token>" http://localhost:8000/notes/1/
```
PUT /notes/{id}/

### Description: Updates the title or content of a specific note.
Example:
bash
```
curl -X PUT -H "Authorization: Token <your_token>" -H "Content-Type: application/json" -d '{"title": "Updated Note", "content": "Updated content."}' http://localhost:8000/notes/1/
```
DELETE /notes/{id}/

### Description: Deletes a specific note by its ID.
Example:
bash
```
curl -X DELETE -H "Authorization: Token <your_token>" http://localhost:8000/notes/1/
```

### Additional Features
Authentication: Implement basic token-based authentication using Django REST Framework's token authentication.
Error Handling: Include basic error handling for cases such as invalid or non-existent IDs.

## Setup Instructions

#### Clone the Repository

```
git clone <repository-url>
cd <project-directory>
```

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Set Up Database and Migrate

```
python manage.py migrate
```

### Run the Server

```
python manage.py runserver
```

### Generate Tokens (optional)

Use the Django REST Framework's built-in command to create tokens for authentication.

### Example Requests
See the examples above for each endpoint.

### Submission
GitHub Repository: Create a public GitHub repository for your project.
Submission Link: Submit the link to your repository with your application.
