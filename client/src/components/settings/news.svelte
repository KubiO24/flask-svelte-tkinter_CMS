<script>
    import NewsElement from './newsElement.svelte';
</script>

<div class='newsContainer'>
    <NewsElement/>
    <NewsElement/>
    <NewsElement/>
    <NewsElement/>  
</div>

<style>
    .newsContainer {
        position: absolute;
        top: 0;

        width: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
    }

</style>