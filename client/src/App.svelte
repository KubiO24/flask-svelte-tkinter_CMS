<script>
  import Router, { link } from "svelte-spa-router";

  import Header from "./components/header.svelte";
  import Main from "./routes/Main.svelte";
  import Login from "./routes/Login.svelte";
  import Register from "./routes/Register.svelte";
</script>

<main>
  <Header />
  <Router
    routes={{
      "/": Main,
      "/login": Login,
      "/register": Register,
    }}
  />
</main>

<style>
  :global(body) {
    margin: 0px;
    padding: 0;
    box-sizing: border-box;
  }
</style>
