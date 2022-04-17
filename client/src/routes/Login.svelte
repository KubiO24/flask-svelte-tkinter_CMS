<script>
// let rand = -1;
// fetch("./rand")
//     .then((d) => d.text())
//     .then((d) => (rand = d));
function validateForm() {
    console.log("submit");
}

function changeLogin() {
    let registerForm = document.getElementById("registerForm")

    registerForm.style.transform = "none";

    registerForm.ontransitionend = () => {
        document.location.href = "/#/Register";
    };

}
</script>

<div id="loginBox">
    <form id="loginForm" method="post" on:submit|preventDefault={validateForm}>
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

    <form on:click={changeLogin} id="registerForm">
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
:global(#loginBox) {
    position: relative;
    width: 300px;
    height: 400px;

    margin: auto;
    margin-top: 100px;

    background-color: black;
    border: 2px solid black;
    border-radius: 20px;
    box-shadow: 0 0 20px 4px rgba(0, 0, 0, 0.25);

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    overflow: hidden;
}

:global(#loginForm) {
    width: 100%;
    height: 100%;

    padding: 20px;

    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

:global(#loginForm h2) {
    margin-top: -30px;
}

:global(button:focus) {
    outline: none;
}

:global(#loginButton) {
    padding: 10px 40px;
    margin-bottom: 50px;

    color: white;
    background-color: #FF4B2B;
    border: 1px solid #FF4B2B;
    border-radius: 20px;
    cursor: pointer;
  
    transition: transform 80ms ease-in;
}

:global(#loginButton:active) {
    transform: scale(0.95);
}

:global(#registerForm) {
    position: absolute;
    width: 700px;
    height: 350px;
    bottom: 0;

    background: linear-gradient(to right, #FF4B2B, #FF416C);
    border-radius: 80% 80% 0 0;
    color: white;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;

    transition: .8s ease-in-out;
}

:global(#registerForm h2) {
    margin-top: -10px;
}

#registerForm {
    cursor: pointer;
    transform: translateY(280px);
}


</style>
