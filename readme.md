# Minesweeper

API Demo: https://minesweeper-avila.herokuapp.com/docs

## Tools
I used flask and flask-restplus because it already bundles a documentation endpoint using swagger.
Client libraries can be built using swagger for many supported languages.

I used pytest to make sure I got the game mechanics correct.
I then refactored to store that game in postgres so I could deploy it fast to heroku.
I am not happy with the JSON columns, I got a bug from saving to them tuples and reading
back (you get arrays). I would prefer to make a `cell` table and store both mines and visited
cells there.

## Development
To run the project in development mode
```
cp .env.dev .env
pipenv run flask run
```
