window.onload = (event) => {
    console.log("Goodbye world")
    const locationButton = document.getElementById("dragon")
    const catalogSection = document.getElementById("catalog-section")
    async function handleLocationButton(){
        const resp = await fetch("http://127.0.0.1:8000/api/wishlist")
        //Array of objects
        const jsonResp = await resp.json()
        jsonResp["books"].forEach(book => {
            let newCatalogEntry = document.createElement("div")
            newCatalogEntry.classList.add("catalog-entry")
            newCatalogEntry.innerText = "Title is: " + book["title"] + "\nAuthor: " + book["author"]
            catalogSection.appendChild(newCatalogEntry)
            console.log("Title is: " + book["title"])
        });
        
    }
    locationButton.addEventListener("click", handleLocationButton)
}