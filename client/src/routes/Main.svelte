<script>
    import Header from "../components/header.svelte";
    import NewsContainer from "../components/NewsContainer.svelte";
    import Footer from "../components/footer.svelte";

    let showSlider = true;
    let showNews = true;
    let someSec = true;

    const newsContent = [
        {
            title: "Special title treatment",
            info: "With supporting text below as a natural lead-in to additional content.",
        },
        {
            title: "Special title treatment",
            info: "With supporting text below as a natural lead-in to additional content.",
        },
        {
            title: "Special title treatment",
            info: "With supporting text below as a natural lead-in to additional content.",
        },
    ];
</script>

<Header />

{#if showSlider}
    <div class="slider">
        <p>Slider</p>
    </div>
{/if}
{#if showNews}
    <div class="newsContainer">
        {#each newsContent as item, i}
            <NewsContainer number={i} title={item.title} content={item.info} />
        {/each}
    </div>
{/if}

{#if someSec}
    <div class="some-sec-container">
        <div class="someSec">
            <div class="left">
                <div>
                    <h2>First featurette heading.</h2>
                    <h3>It will blow your mind</h3>
                </div>
                <div>
                    Some great placeholder content for the first featurette
                    here. Imagine some exciting prose here.
                </div>
            </div>
            <div class="right">
                <div>500 x 500</div>
            </div>
        </div>
    </div>
{/if}

<Footer />

<style>
    .slider {
        width: 100%;
        height: 500px;
        background-color: grey;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .slider p {
        font-size: 100px;
        margin: 0;
        padding: 0;
    }
    .newsContainer {
        width: 100%;
        margin: 30px 0;
        height: auto;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        flex-direction: row;
    }
    .someSec {
        width: 80%;
        min-width: 320px;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .right div {
        width: 500px;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: grey;
        font-size: 50px;
    }
    .some-sec-container {
        width: 100%;
        display: flex;
        justify-content: space-around;
    }
</style>
