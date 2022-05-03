<script>
    import Carousel from "svelte-carousel";

    let carousel; // for calling methods of the carousel instance
    export let data;

    const delay = data.sliderDuration;
</script>

{#if data.sliderItems.length > 0}
    <div class="sliderMain" style="color:{data.sliderColor};">
        <Carousel
            bind:this={carousel}
            autoplay={true}
            autoplayDuration={delay}
            duration={800}
            autoplayProgressVisible={true}
            pauseOnFocus={true}
        >
            {#each data.sliderItems as item}
                <!-- <div
                    class="slider"
                    style="background-image: url({item.sliderPhoto});"
                >
                    <p>{item.sliderText}</p>
                </div> -->
                <div class="slider">
                    <p>{item.sliderText}</p>
                </div>
            {/each}
        </Carousel>
    </div>
{/if}

<style>
    .sliderMain {
        height: 500px;
        -webkit-touch-callout: none; /* iOS Safari */
        -webkit-user-select: none; /* Safari */
        -khtml-user-select: none; /* Konqueror HTML */
        -moz-user-select: none; /* Old versions of Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
        user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
    }
    .slider {
        width: 100%;
        height: 500px;
        background-color: grey;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all ease 1s;
    }
    .slider p {
        font-size: 100px;
        margin: 0;
        padding: 0;
    }
</style>
