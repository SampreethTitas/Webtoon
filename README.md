# Webtoon
Flask API to Create, Read, Delete Webtoons data from PostgreSQL

# Setup
Please create a Database and Assign DB URL into DATABASE_URL variable in .env file

Make sure to install all the required modules from the 'requirements.txt'

SQL Query for table creation(PostgreSQL):

sql
CREATE TABLE webtoons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    characters TEXT[] NOT NULL
);

 

# paths
GET /webtoons: Fetch all webtoons with basic details (title, description, characters).

POST /webtoons: Add a new webtoon entry, including title, summary, and characters.

GET /webtoons/ : Fetch a specific webtoon by its ID, returning detailed information.

DELETE /webtoons/ : Remove a webtoon entry by its ID.
       

