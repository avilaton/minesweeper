# Minesweeper

API Demo: https://minesweeper-avila.herokuapp.com/docs
Frontend Demo: https://minesweeper-avila.herokuapp.com

## Tools
I used flask and flask-restplus because it already bundles a documentation endpoint using swagger.
Client libraries can be built using swagger for many supported languages.

I used pytest to make sure I got the game mechanics correct.
I then refactored to store that game in postgres so I could deploy it fast to heroku.
I am not happy with the JSON columns, I got a bug from saving to them tuples and reading
back (you get arrays). I would prefer to make a `cell` table and store both mines and visited
cells there.
I did not implement the empty cell expansion (clicking on an empty cell should propagate to 
all neighbouring cells) to get to make a frontend for it.

To wrap it up, I would like to implement that cell expansion, show all bombs on game over and many 
other minor updates. Allowing the difficulty to be chosen and the size of the board are fairly simple
to get going.

As far as a frontend is concerned, I hacked together something using Vue.js because I had been
wanting to try it out honestly. It is incomplete, I added the build results to the repository to 
get it online but one could get heroku to build it or host the fronend somewhere else.

## Development
To run the project in development mode
```
cp .env.dev .env
pipenv run flask run
```
