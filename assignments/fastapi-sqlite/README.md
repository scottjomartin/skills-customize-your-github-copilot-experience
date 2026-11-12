# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Build a FastAPI directory for school clubs and store its data in SQLite. Learn how to create a table, run parameterized SQL queries, and keep club information available after the server restarts.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description
Set up a local SQLite database file and create a table for clubs when the API starts.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module and create a `clubs.db` file.
- Create a `clubs` table with an integer primary key and required columns for the club name, description, and meeting day.
- Use `CREATE TABLE IF NOT EXISTS` so starting the API more than once does not erase existing data.
- Configure database connections to return rows by column name.

### 🛠️ Connect the API to the Database

#### Description
Add endpoints for listing, viewing, creating, updating, and deleting clubs using database queries.

#### Requirements
Completed program should:

- Implement `GET /clubs` and `GET /clubs/{club_id}` using `SELECT` queries.
- Implement `POST /clubs`, `PUT /clubs/{club_id}`, and `DELETE /clubs/{club_id}` using the matching SQL statements.
- Use `?` placeholders and query parameters rather than building SQL with string formatting.
- Return HTTP 404 when an update, deletion, or lookup targets a club that does not exist.
- Try the endpoints at `/docs`, restart the server, and confirm that saved clubs remain available.
