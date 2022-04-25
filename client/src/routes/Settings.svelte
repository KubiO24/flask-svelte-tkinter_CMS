<script>
  let username, permissionLevel, permission;

  username = localStorage.getItem("userLoginned");
  if (username == null || username == "null")
    document.location.href = "/#/Login";

  permissionLevel = "0";
  getPermission();

  async function getPermission() {
    const res = await fetch("./getPermission", {
      method: "POST",
      body: username,
    });

    permissionLevel = await res.text();

    if (permissionLevel == 0) {
      permission = "User";
    } else if (permissionLevel == 1) {
      permission = "Privileged User";
    } else if (permissionLevel == 2) {
      permission = "Admin";
    }
  }

  function logout() {
    localStorage.setItem("userLoginned", null);
    document.location.href = "/#/Login";
  }

  function preview() {
    document.location.href = "/";
  }
</script>

<div class="settingsBox">
  <div class="nav flex-row">
    <div class="data flex-row">
      <div id="username">Username: <b>{username}</b></div>
      <div id="permission">Permission: <b>{permission}</b></div>
    </div>

    <div class="control flex-row">
      <button on:click={preview}>Go to page</button>
      <button on:click={logout}>Logout</button>
    </div>
  </div>

  <div class="flex-row">
    <div class="menu">
      <div>Themes</div>
      <div>Block Order</div>
      <div>Slider</div>
    </div>
    <div class="settings">43</div>
  </div>
</div>

<style>
  .settingsBox {
    width: 60%;

    margin: auto;
    margin-top: 100px;

    box-shadow: 0 0 20px 4px rgba(0, 0, 0, 0.25);
    /* box-shadow: 0 0 20px 4px rgba(255, 75, 43, 0.25); */
    border: 2px solid #ff4b2b;
    border-radius: 15px;

    overflow: hidden;
  }

  .nav {
    flex-wrap: wrap;
    justify-content: center;
    padding: 10px 10px;
    background-color: #ebebeb;
    border-bottom: 2px solid #ff4b2b;
  }

  .data {
    width: 50%;
    min-width: 200px;
    justify-content: left;
  }

  .data div {
    margin: 0px 20px;
  }

  .control {
    width: 50%;
    min-width: 200px;
    justify-content: right;
  }

  .control button {
    padding: 5px 10px;
    margin: 0px 10px;
  }

  .flex-row {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .menu {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: left;

    background-color: #ebebeb;
  }

  .menu div {
    margin: 20px 10px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s ease-in-out;
  }

  .menu div:hover {
    color: #ff4b2b;
    transform: scale(1.1);
    transition: all 0.2s ease-in-out;
  }

  .settings {
    width: 100%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
