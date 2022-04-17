<script>
  function validateForm() {
    console.log("submit");
  }

  function changeLogin() {
    let registerForm = document.getElementById("registerForm")
    
    registerForm.style.transform = "translateY(280px)";

    registerForm.ontransitionend = () => {
        document.location.href = "/#/Login";
    };
    
  }
</script>



<div id="loginBox">
    <form on:click={changeLogin} id="loginForm" >
        <h2>Log In</h2>

        <div>
            <label for="uname"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="uname" required />
        </div>
    
        <div>
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required />
        </div>
    
        <button id="loginButton" type="submit">Log In</button>
    </form>
    
    <form id="registerForm" on:submit|preventDefault={validateForm} method="post" >
        <h2>Sign Up</h2>

        <div>
            <label for="uname"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="uname" required />
        </div>
    
        <div>
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required />
        </div>
    
        <button type="submit">Sign Up</button>
    </form>   
</div>



<style>
    #loginForm {
        cursor: pointer
    }

    #registerForm {
        cursor: auto;
    }
</style>
