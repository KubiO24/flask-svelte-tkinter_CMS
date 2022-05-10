<script>
  import Header from "../components/header.svelte";
  import NewsContainer from "../components/NewsContainer.svelte";
  import Footer from "../components/footer.svelte";
  import Slider from "../components/slider.svelte";
  let logged = false;
  let username = localStorage.getItem("userLoginned");
  if ((username === null || username === "null") === false) logged = true;
  let bgColor;
  let color;
  async function getData() {
    let res = await fetch("./getData", {
      method: "POST",
    });
    res = await res.json();
    bgColor = res.theme.mainBackground;
    color = res.theme.mainColor;
    console.log(res);
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
    {#each data.blocks as item}
      {#if item.type === "navbar"}
        <Header
          navbarType={item.navbarType}
          navbarItems={item.navbarItems}
          background={data.theme.secondBackground}
          color={data.theme.secondColor}
          color2={data.theme.mainColor}
          isLogged={logged}
        />
        <div style="padding: 60px;" />
      {/if}

      {#if item.type === "slider"}
        <Slider data={item} />
      {/if}

      {#if item.type === "news"}
        <div class="newsContainer">
          {#each item.newsItems as news, i}
            <NewsContainer
              category={news.newsCategory}
              border={data.theme.newsBorder}
              title={news.newsTitle}
              content={news.newsText}
              img={news.newsPhoto}
            />
          {/each}
        </div>
      {/if}

      {#if item.type === "content"}
        <div class="some-sec-container">
          <div class="someSec">
            <div class="left">
              <div>
                <h2>First featurette heading.</h2>
                <h3>It will blow your mind</h3>
              </div>
              <div>
                Some great placeholder content for the first featurette here.
                Imagine some exciting prose here.
              </div>
            </div>
            <div class="right">
              <div>500 x 500</div>
            </div>
          </div>
        </div>
      {/if}
      {#if item.type === "footer"}
        <Footer footerItems={item.footerItems} copyrights={item.footerText} />
      {/if}
    {/each}
  </div>
{/await}

<style>
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
