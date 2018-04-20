<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h2>Minesweeper</h2>
    <button v-on:click="getBoards">Get boards</button>
    <button v-on:click="createBoard">New Game</button>
      <div v-for="(row, y) in rows">
        <button v-for="(col, x) in row" v-on:click="onClickCell(x, y)">
          {{ col.label }}
        </button>
      </div>
      <h3 v-if="board.over">Game Over</h3>
      <p>{{ msg }}</p>
      <pre>{{board}}</pre>
  </div>

</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      apiBase: '/api/boards',
      board: {
        over: false
      },
    }
  },
  methods: {
    getBoards() {
      fetch(this.apiBase).then((res) => {return res.json()}).then((boards) => {
        console.log(boards)
      })
    },
    createBoard() {
      fetch(this.apiBase, {method: 'POST'}).then((res) => {return res.json()}).then((board) => {
        this.board = board
      })
    },
    onClickCell(x, y) {
      const boardId = this.board.id
      const url = this.apiBase + `/${boardId}/cells/${x}/${y}`
      fetch(url, {method: 'PUT'}).then((res) => {
        if (res.ok) {
          return res.json()
        } else {
          throw Error('already visited');
        }
      }).then((board) => {
        this.board = board
      }).catch((error) => {
        this.msg = error.message
      })
    }
  },
  computed: {
    rows: function () {
      let rv = [
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
        [{v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}, {v: null, label: '_'}],
      ]
      if (this.board.id) {
        this.board.cells.forEach(cell => {
          rv[cell.y][cell.x].v = cell.value
          rv[cell.y][cell.x].label = cell.value === null? 'X': cell.value
        });
      }
      return rv
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
pre {
  text-align: left;
}
</style>
