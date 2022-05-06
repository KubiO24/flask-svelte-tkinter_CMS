<script>
    import Header from "../components/header.svelte";
    import Footer from "../components/footer.svelte";
    import Blocks from "../components/settings/blocks.svelte";
    const newsObj = {
        title: "Title",
        description: "Lorem ipmsum",
        category: "Category",
        gallery: [
            {
                sliderPhoto: "../static/xyz1.jpg",
                sliderText: "Teskt1 na sliderze",
            },
            {
                sliderPhoto: "../static/xyz2.jpg",
                sliderText: "Teskt2 na sliderze",
            },
            {
                sliderPhoto: "../static/xyz2.jpg",
                sliderText: "Teskt3 na sliderze",
            },
            {
                sliderPhoto: "../static/xyz2.jpg",
                sliderText: "Teskt4 na sliderze",
            },
            {
                sliderPhoto: "../static/xyz2.jpg",
                sliderText: "Teskt5 na sliderze",
            },
        ],
    };

    let logged = false;
    let username = localStorage.getItem("userLoginned");
    if ((username === null || username === "null") === false) logged = true;
    let bgColor;
    let color;
    async function getData() {
        let URL = "./data.json";
        let res = await fetch(URL);
        res = await res.json();
        bgColor = res.theme.mainBackground;
        color = res.theme.mainColor;
        res["news"] = [newsObj];
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
        {#each data.news as item}{/each}
        <Footer copyrights={data.blocks[data.blocks.length - 1].footerText} />
    </div>
{/await}
