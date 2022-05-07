<!-- 
    POWODZENIA <333
    
    co do typu strony to ja bym narazie zrobił coś w tematyce fitness, siłownia bo obaj się w miare na tym znamy a co najmniej strona nie będzie taka pusta i będzie wiadomo +/- co i jak 
    
    FORMAT JSONA:
    data = {
        theme: {
            mainColor: "#ffffff", // główny kolor czcionki
            secondColor: "#ff0000", // drugi kolor czcionki
            mainBackground: "#000000", // główny kolor tła
            secondBackground: "#333333", // drugi kolor tła, nie wiem można np sekcje jakaś zrobic w tym, albo co drugą albo tytuły newsow. Ważne zeby tymi dwoma kolorami dało się ogarnąć cała kolorystyke tej strony,
            font: "Roboto" // domyślna czcionka
        },

        blocks: [ // lista bloków w kolejności od pierwszego do ostatniego
            {
                type: "navbar", // Typ bloku
                navbarType: "horizontal(normalne) / vertical(hamburger)", // Zmianę sposobu wyświetlania menu (klasyczne i inne)
                navbarItems: [
                    {
                        navbarText: "Features",   
                        navbarLink: "/#/Features"
                    },
                    {
                        navbarText: "Pricing",   
                        navbarLink: "/#/Pricing"
                    },
                    {
                        ...
                    },
                    ... 
                ]
            },

            {
                type: "slider",
                sliderDuration: 500, // Ustawienie czasu przejścia slidera w milisekundach 
                sliderColor: "white", // kolor czcionki slidera
                sliderItems: [
                    {
                        sliderPhoto: "../static/xyz1.jpg", // Ścieżka do zdjęcia slidera
                        sliderText: "Teskt1 na sliderze"
                    },
                    {
                        sliderPhoto: "../static/xyz2.jpg",
                        sliderText: "Teskt2 na sliderze"
                    },
                    ...
                ]
                
            },

            {
                type: "news",
                newsItems: [
                    {
                        newsCategory: "Kategoria artykułu",
                        newsTitle: "Tytuł artykułu", // Zrobie tak, że nie będzie można dać dwóch takich samych tytułów, więc później jak się wejdzie w artukuł to będzie można pobierać jego komentarze z serwera po tytule
                        newsText: "Opis artykułu",
                        newsPhoto: "Ścieżka do zdjęcia artykułu" // W sumie to nie wiem czy musi być zdjęcie, ale chyba lepiej będzie z, ale jak nie chcesz to możesz to wyjebać, tylko powiedz mi to żeby nie robił tego w ustawieniach
                    },
                    {
                        newsCategory: "Advice",
                        newsTitle: "Best protein flavours 2022",
                        newsText: "Jakis tam opis, to pozniej mozna wymyslec",
                        newsPhoto: "Ścieżka do zdjęcia artykułu"
                    },
                    ...
                ]
                
            },

            {
                type: "footer",
                footerText: "Jakub Kowal - Igor Świerczyński CMS 2022",
            }
        ]
    }

 -->
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
        <div
          style="padding: 60px
;"
        />
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
        <Footer copyrights={item.footerText} />
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
