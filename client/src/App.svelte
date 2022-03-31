<script>
  import Router, { link } from 'svelte-spa-router'

  import Main from './routes/Main.svelte'
  import Login from './routes/Login.svelte'
</script>


<main>
  <Router
    routes = {{
      "/": Main,
      "/login": Login,
      "/register": Login
    }}
  />
</main>