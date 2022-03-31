<script>
  import Router, { link } from 'svelte-spa-router'

  import Main from './routes/Main.svelte'
  import Random from './routes/Random.svelte'
</script>


<main>
  <Router
    routes = {{
      "/": Main,
      "/random": Random
    }}
  />
</main>