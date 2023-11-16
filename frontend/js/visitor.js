//Azure Fuction endpoint
const functionUrl ="";

//Get request to Azure endpoint
function updateVisitorCount() {
    fetch(functionUrl).then((response) => response.json())
    .then((count) => {
        document.getElementById(webcounter).textContent = count;
    })
    .catch((error) =>{
        console.log("Error: " + error);
    });
};
updateVisitorCount()