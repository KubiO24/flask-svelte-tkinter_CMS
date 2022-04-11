<script>
  import Router, { link } from "svelte-spa-router";

  import Main from "./routes/Main.svelte";
  import Login from "./routes/Login.svelte";
  import Register from "./routes/Register.svelte";
</script>

<main>
  <Router
    routes={{
      "/": Main,
      "/login": Login,
      "/register": Register,
    }}
  />
</main>
