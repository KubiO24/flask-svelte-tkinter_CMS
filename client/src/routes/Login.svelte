<script>
  // let rand = -1;
  // fetch("./rand")
  //     .then((d) => d.text())
  //     .then((d) => (rand = d));
  function validateForm() {
    console.log("submit");
  }
</script>

<form id="loginForm" method="post" on:submit|preventDefault={validateForm}>
  <div id="loginContainer">
    <div>
      <label for="uname"><b>Username</b></label>
      <input type="text" placeholder="Enter Username" name="uname" required />
    </div>

    <div>
      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="psw" required />
    </div>

    <button class="btn-grad" type="submit">Login</button>
  </div>
</form>

<style>
  :global(#loginForm) {
    width: 25%;
    height: 400px;

    margin: auto;
    margin-top: 100px;

    padding: 40px;

    background-color: white;
    border: 2px solid black;
    border-radius: 20px;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  :global(#loginContainer) {
    width: 100%;
    height: 100%;

    background-color: white;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
  }

  .btn-grad {
    margin: 10px;
    padding: 15px 45px;
    text-align: center;
    text-transform: uppercase;
    transition: 0.5s;
    background-size: 200% auto;
    color: white;
    box-shadow: 0 0 20px #eee;
    border-radius: 10px;
    display: block;
    cursor: pointer;

    background-image: linear-gradient(
      to right,
      #314755 0%,
      #26a0da 51%,
      #314755 100%
    );
  }

  .btn-grad:hover {
    background-position: right center;
    color: #fff;
    text-decoration: none;
  }
</style>
