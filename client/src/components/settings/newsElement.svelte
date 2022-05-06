<script>
    let title, description, category, images, selectedImage, fileInput;
    title = "";
    description = "";
    category = "";
    function save() {
        console.log(title)
        if(title == "" || description == "" || category == "") {
            alert("Title or Description or Category is empty!")
            return;
        }
    }

    function loadedImage() {
        console.log(images)
        selectedImage = images[0].name;
    }

    function deleteImage() {
        if(images == undefined) return;
        if(images.length == 0) return;
        const imageArray = [...images] 
        let i = 0;
        for(let image of imageArray) {
            if(image.name == selectedImage) {
                imageArray.splice(i, 1)
            };
            i += 1;
        }
        images=imageArray;
        if(images.length != 0) selectedImage = images[0].name;      
    }
</script>

<div class="news">
    <div class="newsContent">
        <div class="newsContent2">
            <div class="newsValues">
                <input bind:value={title} type="text" placeholder="News Title">
                <textarea bind:value={description} cols="30" rows="10" placeholder="News Description"></textarea>
            </div>
            <div class="newsValues">
                <input bind:value={category} type="text" placeholder="News Category">

                <div class='galleryBox'>
                    gallery:
                    <select bind:value={selectedImage}>
                        {#if images && images[0]}
                            {#each images as image}
                                <option value={image.name}>{image.name}</option>
                            {/each}
                        {/if}
                    </select>
                    <input bind:this={fileInput} bind:files={images} on:change={loadedImage} type="file" name="img" accept="image/*" multiple style="display: none;">
                    <input class="fileInput" type="button" value="Add image to gallery" on:click={()=>fileInput.click()} style="margin-bottom: 5px;" />
                    <button on:click={deleteImage}>Delete selected from gallery</button>
                </div>
            </div>
        </div>
        
        <div class="newsContent2" style="justify-content: center;">
            <button on:click={save} class="saveButton">save</button>
        </div>  
    </div> 
</div>

<style>
    input {
        margin: 0;
    }
    .news:first-child {
        border-top: none !important;
    }

    .news {
        height: 400px;
        width: 100%;
        border-top: 2px solid #ff4b2b;
    }

    .newsContent {
        height: 100%;
        margin: 20px;
        display: flex;
        flex-direction: column;
        justify-content: left;
    }

    .newsContent2 {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .newsValues {
        width: 40%;
        height: 290px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    textarea {
        resize: none;
        margin: 0;
    }

    select {
        width: 100px;
        margin-top: 2px;
    }

    .fileInput {
        width: 100%;
    }

    .galleryBox {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .galleryBox select {
        width: 100%;
    }

    .galleryBox button {
        width: 100%;
    }

    .saveButton {
        width: 100px;
        padding: 10px 40px;
        margin-top: 30px;
        color: white;
        background-color: #FF4B2B;
        border: 1px solid #FF4B2B; 
        border-radius: 20px;
        cursor: pointer;
        transition: transform 80ms ease-in;
        display: flex;
        justify-content: center;
    }

    .saveButton:active {
        transform: scale(0.95);
    }

    .saveButton:focus {
        outline: none;
        background-color: #FF4B2B;
    }
    
</style>