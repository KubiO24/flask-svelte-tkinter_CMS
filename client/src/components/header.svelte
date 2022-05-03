<script>
    export let navbarType;
    export let navbarItems;
    export let background;
    export let color;

    let active = false;
</script>

<header style="background-color: {background};">
    {#if navbarType !== "horizontal"}
        <div class="nav-container" style="padding: 0 20px;">Icon</div>
        <nav>
            <div class="nav-links nav-container">
                {#each navbarItems as item}
                    <a style="color: {color}" href={item.navbarLink}
                        >{item.navbarText}</a
                    >
                {/each}
            </div>
        </nav>
        <div class="links nav-container">
            <a href="/#/Login" class="linkLogin">Login</a>
            <a href="/#/Register" class="linkRegister">Register</a>
        </div>
    {:else}
        <div
            class="nav-container"
            style="padding: 0 20px; justify-content:start;"
        >
            Icon
        </div>
        <div
            class="nav-container hamburger-menu"
            style="padding: 0 20px; justify-content:end;"
        >
            {#if active}
                <i class="fa fa-bars" style="font-size:36px" />
            {:else}
                <i class="fa fa-close" style="font-size:36px" />
            {/if}
        </div>
    {/if}
</header>

<style>
    header {
        display: flex;
        justify-content: space-around;
        padding: 40px;
    }
    .nav-container {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    nav {
        width: 70%;
        max-width: 500px;
    }
    .nav-links {
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .nav-links a {
        text-decoration: none;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .linkLogin {
        padding: 5px 10px;
        margin: 0 6px;
        border-radius: 10px;
        border: 1px solid green;
        text-decoration: none;
        color: green;
    }
    .linkRegister {
        padding: 5px 10px;
        border-radius: 10px;
        border: 1px solid #4747ff;
        text-decoration: none;
        color: #4747ff;
    }
</style>
