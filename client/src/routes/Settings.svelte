<script>
    let username, permissionLevel, permission;

    username = localStorage.getItem("userLoginned");
    if(username == null) document.location.href = "/#/Login";

    permissionLevel = "0";
    getPermission();

    async function getPermission() {
        const res = await fetch('./getPermission', {
            method: 'POST',
            body: username
        })

        permissionLevel = await res.text()

        if(permissionLevel == 0) {
            permission = "User";
        }else if(permissionLevel == 1) {
            permission = "Privileged User";
        }else if(permissionLevel == 2) {
            permission = "Admin";
        }
    }

    
    
</script>
    <div class="settingsBox">
        <div class="nav flex-row-between">
            <div class="data flex-row-between">
                <div id="username">Username: <b>{username}</b></div>
                <div id="permission">Type: <b>{permission}</b></div>
            </div>

            <div class="control flex-row-between">
                <button>Preview</button>
                <button>Logout</button>
            </div>
        </div>
        <div class="content">content</div>  
    </div>


<style>
    .settingsBox {
        width: 80%;

        margin: auto;
        margin-top: 100px;

        border: 2px solid #FF4B2B;
        border-radius: 15px;

        overflow: hidden;
    }

    .nav {
        padding: 10px 20px;
        background-color: #ebebeb;
        flex-wrap: wrap;
    }

    .data {
        width: 20%;
        min-width: 150px;
    }

    .data div {
        margin: 0px 20px;
    }

    .control {
        width: 15%;
        min-width: 150px;
    }

    .control button {
        padding: 5px 10px;
        margin: 0px 10px;
    }

    .flex-row-between {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
</style>