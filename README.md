# Webtoon
Flask API to Create, Read, Delete Webtoons data from PostgreSQL

#Setup
Please create a Database and Assign DB URL into DATABASE_URL variable in .env file

SQL Query for table creation:

sql
CREATE TABLE webtoons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    characters TEXT[] NOT NULL
);

 Make sure to install all the required modules from the 'requirements.txt'

paths:
  /webtoons:
    get:
      summary: Fetch all webtoons
      responses:
        '200':
          description: A list of webtoons
    post:
      summary: Add a new webtoon
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                summary:
                  type: string
                characters:
                  type: array
                  items:
                    type: string
      responses:
        '201':
          description: Webtoon created successfully
  /webtoons/{id}:
    get:
      summary: Fetch a specific webtoon by ID
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the webtoon
          schema:
            type: integer
      responses:
        '200':
          description: Detailed information about a webtoon
    delete:
      summary: Remove a webtoon by ID
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the webtoon
          schema:
            type: integer
      responses:
        '204':
          description: Webtoon deleted successfully

