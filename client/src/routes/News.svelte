<script>
    import Header from "../components/header.svelte";
    import Footer from "../components/footer.svelte";
    import Carousel from "svelte-carousel";
    import { onMount } from "svelte";

    let carousel;
    let logged = false;
    let username = localStorage.getItem("userLoginned");
    if ((username === null || username === "null") === false) logged = true;
    let bgColor;
    let color;
    let news;
    let imagesBase64Array = [];
    onMount(() => {
        let qr_code = window.location.pathname; // dump leading '/'
        console.log("qr_code: ", qr_code);
    });
    async function getData() {
        let res = await fetch("./getData", {
            method: "POST",
        });
        res = await res.json();
        bgColor = res.theme.mainBackground;
        color = res.theme.mainColor;
        res.blocks.forEach((el) => {
            if (el.type === "news") {
                news = el.newsItems;
            }
        });
        console.log(news);

        if (news[0].newsPhoto !== "") {
            imagesBase64Array = news[0].newsPhoto.split(".");
        }
        console.log(imagesBase64Array);
        return res;
    }
    let data = getData();
    console.log(params);
</script>

{#await data}
    Loading...
{:then data}
    <div
        class="main-page-container"
        style="background-color: {bgColor};color:{color};"
    >
        <Header
            navbarType={data.blocks[0].navbarType}
            navbarItems={data.blocks[0].navbarItems}
            background={data.theme.secondBackground}
            color={data.theme.secondColor}
            color2={data.theme.mainColor}
            isLogged={logged}
        />
        <div style="padding: 60px;" />

        <div class="container">
            <h2>{news[0].newsTitle}</h2>
            <h5>{news[0].newsCategory}</h5>
            <article>{news[0].newsText}</article>
            <Carousel
                bind:this={carousel}
                let:showPrevPage
                let:showNextPage
                autoplay={false}
                duration={800}
            >
                <div
                    slot="prev"
                    on:click={showPrevPage}
                    class="custom-arrow custom-arrow-prev"
                >
                    <i class="fa fa-angle-left" style="font-size:60px" />
                </div>
                {#if imagesBase64Array.length > 0}
                    {#each imagesBase64Array as item, i}
                        <!-- <div
                    class="slider"
                    style="background-image: url({item.sliderPhoto});"
                >
                    <p>{item.sliderText}</p>
                </div> -->
                        <div class="slider">
                            <img
                                class="img"
                                src={imagesBase64Array[i]}
                                alt=""
                            />
                        </div>
                    {/each}
                {:else}
                    <div>There are no pictures in gallery</div>{/if}
                <div
                    slot="next"
                    on:click={showNextPage}
                    class="custom-arrow custom-arrow-next"
                >
                    <i class="fa fa-angle-right" style="font-size:60px" />
                </div>
            </Carousel>
        </div>

        <Footer
            footerItems={data.blocks[data.blocks.length - 1].footerItems}
            copyrights={data.blocks[data.blocks.length - 1].footerText}
        />
    </div>
{/await}

<style>
    .slider {
        width: 100%;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all ease 1s;
    }
    .img {
        height: 500px;
    }
    .custom-arrow {
        width: 40px;
        position: absolute;
        top: 0;
        bottom: 0;
        z-index: 1;
        transition: opacity 150ms ease;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        -webkit-tap-highlight-color: transparent;
    }
    .custom-arrow-next {
        right: 0;
    }
</style>
