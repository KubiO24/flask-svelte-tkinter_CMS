<script>
    export let data;

    const slides = [];
    const delay = data.sliderDuration;
    let currentSlide = 0;
    let interval;

    data.sliderItems.forEach((item, i) => {
        slides.push("slide" + i);
    });

    window.onload = () => {
        interval = setInterval(changeSlide, delay);
    };
    const changeSlide = () => {
        const lastSlide = currentSlide;
        currentSlide++;
        if (currentSlide === slides.length) currentSlide = 0;
        console.log(lastSlide, currentSlide);

        document.getElementById(slides[lastSlide]).classList.remove("show");
        document.getElementById(slides[lastSlide]).classList.add("hide");
        document.getElementById(slides[currentSlide]).classList.remove("hide");
        document.getElementById(slides[currentSlide]).classList.add("show");
    };
</script>

{#if data.sliderItems.length > 0}
    <div class="sliderMain" style="color:{data.sliderColor};">
        {#each data.sliderItems as item, i}
            {#if i === 0}
                <div class="slider show" id={`slide${i}`}>
                    <p>{item.sliderText}</p>
                </div>
            {:else}
                <div class="slider hide" id={`slide${i}`}>
                    <p>{item.sliderText}</p>
                </div>
            {/if}
        {/each}
    </div>
{/if}

<style>
    .sliderMain {
        height: 500px;
    }
    .slider {
        position: absolute;
        width: 100%;
        height: 500px;
        background-color: grey;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all ease 1s;
    }
    .show {
        opacity: 1;
    }
    .hide {
        opacity: 0;
    }
    .slider p {
        font-size: 100px;
        margin: 0;
        padding: 0;
    }
</style>
