<script>
    export let number;
    number += 1;
    export let title;
    export let content;
    console.log(number, title, content);
</script>

<div class="newsContainer">
    <div class="navContainer">News {number}</div>
    <div class="newsContent">
        <h3>{title}</h3>
        <p>{content}</p>
        <button>Go somewhere</button>
    </div>
</div>

<style>
    .newsContainer {
        max-width: 500px;
        min-width: 300px;
        width: 25%;
        display: flex;
        flex-direction: column;
        border-radius: 30px;
        overflow: hidden;
        border: 1px solid #c6e4ff;
        margin: 20px;
    }
    .navContainer {
        padding: 10px;
        background-color: #c6e4ff;
        text-align: center;
    }
    .newsContent {
        padding: 0 10px 10px 10px;
    }
</style>
