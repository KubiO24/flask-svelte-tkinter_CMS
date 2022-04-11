<script>
  // let rand = -1;
  // fetch("./rand")
  //     .then((d) => d.text())
  //     .then((d) => (rand = d));
  function validateForm() {
    console.log("submit");
  }
</script>

<form method="post" on:submit|preventDefault={validateForm}>
  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required />

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required />

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember" /> Remember me
    </label>
  </div>
</form>
