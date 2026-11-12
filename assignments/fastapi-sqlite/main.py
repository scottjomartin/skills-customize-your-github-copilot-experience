from contextlib import closing
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="School Club Directory API")
DATABASE_PATH = "clubs.db"


class ClubInput(BaseModel):
    name: str
    description: str
    meeting_day: str


class Club(ClubInput):
    id: int


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        # TODO: Create the clubs table if it does not already exist.
        # Include an integer primary key and required name, description, and meeting_day columns.
        connection.commit()


def club_from_row(row: sqlite3.Row) -> Club:
    return Club(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        meeting_day=row["meeting_day"],
    )


initialize_database()


@app.get("/")
def read_root():
    return {"message": "School Club Directory API"}


@app.get("/clubs", response_model=list[Club])
def list_clubs():
    with closing(get_connection()) as connection:
        # TODO: Select all clubs and convert each row with club_from_row.
        pass


@app.get("/clubs/{club_id}", response_model=Club)
def get_club(club_id: int):
    with closing(get_connection()) as connection:
        # TODO: Select one club by ID, or raise HTTPException with status 404.
        pass


@app.post("/clubs", response_model=Club, status_code=201)
def create_club(club_input: ClubInput):
    with closing(get_connection()) as connection:
        # TODO: Insert the club with query parameters, commit, and return the new club.
        pass


@app.put("/clubs/{club_id}", response_model=Club)
def update_club(club_id: int, club_input: ClubInput):
    with closing(get_connection()) as connection:
        # TODO: Update the club by ID, commit, and return the updated club.
        # Raise HTTPException with status 404 if no club was updated.
        pass


@app.delete("/clubs/{club_id}")
def delete_club(club_id: int):
    with closing(get_connection()) as connection:
        # TODO: Delete the club by ID and commit the change.
        # Raise HTTPException with status 404 if no club was deleted.
        pass
