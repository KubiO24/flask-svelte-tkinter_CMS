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
          Some great placeholder content for the first featurette here. Imagine
          some exciting prose here.
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
