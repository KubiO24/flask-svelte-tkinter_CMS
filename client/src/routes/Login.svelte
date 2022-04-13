<script>
  // let rand = -1;
  // fetch("./rand")
  //     .then((d) => d.text())
  //     .then((d) => (rand = d));
  function validateForm() {
    console.log("submit");
  }

  function changeLogin() {
    let changelogin = document.getElementById("changeLogin")
    
    if(changelogin.style.transform == "none") {
      changelogin.style.transform = "translateY(300px)";
    }else {
      changelogin.style.transform = "none";
    }
    
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

    <button type="submit">Login</button>
  </div>
  <div on:click={changeLogin} id="changeLogin">
    <span>Register</span>
  </div>
</form>


<style>

  :global(#loginForm) {
    position: relative;
    width: 15%;
    height: 400px;

    margin: auto;
    margin-top: 100px;

    background-color: black;
    border: 2px solid black;
    border-radius: 20px;

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    overflow: hidden;
  }

  :global(#loginContainer) {
    width: 100%;
    height: 100%;

    padding: 20px;

    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
  }

  :global(#changeLogin) {
    position: absolute;
    width: 40vw;
    height: 350px;
    bottom: 0;

    background-color: black;
    border-radius: 80% 80% 0 0;
    color: white;
    cursor: pointer;

    display: flex;
    justify-content: center;

    transform: translateY(300px);
    transition: .8s ease-in-out;
  }

  :global(#changeLogin span) {
    margin-top: 10px;
  }

</style>
