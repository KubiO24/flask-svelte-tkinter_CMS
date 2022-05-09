<script>
    import Header from "../components/header.svelte";
    import Footer from "../components/footer.svelte";
    import Blocks from "../components/settings/blocks.svelte";

    let logged = false;
    let username = localStorage.getItem("userLoginned");
    if ((username === null || username === "null") === false) logged = true;
    let bgColor;
    let color;
    let news;
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
        return res;
    }
    let data = getData();
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
        </div>

        <Footer
            footerItems={data.blocks[data.blocks.length - 1].footerItems}
            copyrights={data.blocks[data.blocks.length - 1].footerText}
        />
    </div>
{/await}
