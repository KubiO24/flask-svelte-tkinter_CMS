<script>
  import Themes from "../components/settings/themes.svelte";
  import Blocks from "../components/settings/blocks.svelte";
  import UserList from "../components/settings/userList.svelte";
  import News from "../components/settings/news.svelte";

  let username,
    permissionLevel,
    permission,
    selectedSetting,
    settingProps,
    menuHeight;
  selectedSetting = Themes;

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

  function open(x) {
    switch (x) {
      case "themes":
        selectedSetting = Themes;
        settingProps = {};
        break;
      case "blocks":
        selectedSetting = Blocks;
        settingProps = {};
        break;
      case "userList":
        selectedSetting = UserList;
        settingProps = { permissionLevel: permissionLevel, username: username };
        break;
      case "news":
        selectedSetting = News;
        settingProps = {};
        break;
      default:
        console.log(`Failed to open: ${x}`);
    }
  }

  async function getData() {
    console.log("getdata");
    const res = await fetch("./getData", {
      method: "POST",
    });
  }
</script>

<div class="settingsBox">
  <div class="nav flex-row">
    <div class="data flex-row">
      <div id="username">Username: <b id="dataUsername">{username}</b></div>
      <div id="permission">Permission: <b>{permission}</b></div>
    </div>

    <div class="control flex-row">
      <a class="controlButton" href="/">Go to page</a>
      <button class="controlButton" on:click={logout}>Logout</button>
    </div>
  </div>

  <div class="flex-row">
    <div class="menu" bind:clientHeight={menuHeight}>
      <div on:click={() => open("themes")}>Themes</div>
      <div on:click={() => open("blocks")}>Blocks</div>
      <div>Slider</div>
      <div on:click={() => open("news")}>News</div>
      <div on:click={() => open("userList")}>
        {#if permissionLevel == 2}
          User List
        {:else}
          Account settings
        {/if}
      </div>
    </div>

    <div class="settings" style="height: {menuHeight}px;">
      <svelte:component this={selectedSetting} {...settingProps} />
    </div>
  </div>
</div>
<div class="saveSettings">
  <button on:click={getData}>Save Settings</button>
</div>

<style>
  .saveSettings {
    width: 100%;
    margin: 30px 0;
    display: flex;
    justify-content: center;
  }
  .saveSettings > button {
    padding: 10px 40px;
    color: white;
    background-color: #ff4b2b;
    border: 1px solid #ff4b2b;
    border-radius: 20px;
    cursor: pointer;
    transition: transform 80ms ease-in;
    margin-top: 10px;
  }
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
    min-width: 210px;
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

  .controlButton {
    margin: 0px 10px;
    padding: 5px 10px;
    background-color: #f4f4f4;
    color: #333;
    white-space: nowrap;
    user-select: none;
    text-decoration: none;
    cursor: pointer;
    border: 1px solid #ccc;
    transition: all 0.2s ease-in-out;
  }

  .controlButton:hover {
    background-color: rgb(235, 235, 235);
  }

  .flex-row {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .menu {
    height: 100%;
    min-height: 600px;

    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: left; */
    justify-content: space-evenly;

    background-color: #ebebeb;
    border-right: 2px solid #ff4b2b;
  }

  .menu div {
    margin: 20px 15px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s ease-in-out;
    font-weight: bold;
  }

  .menu div:hover {
    color: #ff4b2b;
    transform: scale(1.1);
    transition: all 0.2s ease-in-out;
  }

  .settings {
    width: 100%;
    position: relative;

    display: flex;
    justify-content: center;
    align-items: center;

    overflow-y: auto;
    overflow-x: auto;
  }
</style>
