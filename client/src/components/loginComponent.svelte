<script>
    export let type;
    
    function validateLogin() {
        console.log("login submit");
    }

    async function validateRegister() {
        let formEl = document.forms.registerForm;
        let formData = new FormData(formEl);

        const res = await fetch('./register', {
			method: 'POST',
			body: JSON.stringify({
				username: formData.get('username'),
                password: formData.get('password'),
                email: formData.get('email')
            }),
            headers: {
                "content-type": "application/json"
            }
        })

        // const json = await res.json()
		// let result = JSON.stringify(json)
        const result = await res.text()
        if(result == '1') {
            console.log("Success")
        }else {
            console.log("Error")
        }
    }

    function changeType() {
        let registerForm = document.getElementById("registerForm");
        
        if(type == "login") {
            type = "register";
            
            registerForm.ontransitionend = () => {
                document.location.href = "/#/Register";
            };
        }else {
            type = "login";

            registerForm.ontransitionend = () => {
                document.location.href = "/#/Login";
            };
        }
        
    }
</script>

<div id="loginBox">
    <form id="loginForm" style={type=="register" ? 'cursor:pointer;' : undefined} on:click={type=="register" ? changeType : undefined} on:submit|preventDefault={type=="login" ? validateLogin : undefined}>
        
        <h2>Log In</h2>

        <div>
            <input
                type="text"
                placeholder="Username"
                name="username"
                required
            />
        </div>

        <div>
            <input
                type="password"
                placeholder="Password"
                name="password"
                required
            />
        </div>

        <button id="loginButton" type="submit">Log In</button>
    </form>
    <form id="registerForm" class:activeLogin={type=="login"} style={type=="login" ? 'cursor:pointer; transform: translateY(280px);' : undefined} on:click={type=="login" ? changeType : undefined} on:submit|preventDefault={type=="register" ? validateRegister : undefined}>
        <h2>Sign Up</h2>

        <div>
            <input
                type="text"
                placeholder="Username"
                name="username"
                required
            />
        </div>

        <div>
            <input
                type="text"
                placeholder="Email"
                name="email"
                required
            />
        </div>

        <div>
            <input
                type="password"
                placeholder="Password"
                name="password"
                required
            />
        </div>

        <button id="registerButton" type="submit">Sign Up</button>
    </form>
</div>

<style>

    #loginBox {
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
    
    #loginForm {
        width: 100%;
        height: 100%;
    
        padding: 20px;
    
        background-color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
    }
    
    h2 {
        user-select: none;
    }

    #loginForm h2 {
        margin-top: -30px;
        
    }
   
    button {
        padding: 10px 40px;

        border-radius: 20px;
        cursor: pointer;

        transition: transform 80ms ease-in;
    }
    
    button:active {
        transform: scale(0.95);
    }

    button:focus {
        outline: none;
    }

    #loginButton {
        margin-bottom: 50px;
    
        color: white;
        background-color: #FF4B2B;
        border: 1px solid #FF4B2B;     
    }

    #registerButton {
        color: black;
        background-color: white;
        border: 1px solid white;   
    }
    
    #registerForm {
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

     
    #registerForm h2 {
        margin-top: -10px;
    }
    
    .cursorPointer {
        cursor: pointer;
    }

    input {
        
        border-radius: 5px;
        height: 50px;
        line-height: normal;
        color: #282828;
        display: block;
        width: 100%;
        box-sizing: border-box;
        user-select: auto;
        font-size: 16px;
        padding: 0 6px;
        padding-left: 12px;
                
    }

</style>