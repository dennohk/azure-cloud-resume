//Azure Fuction endpoint
const functionUrl ="https://azureresumeapi.azurewebsites.net";

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