// Displays the image to be uploaded 

/* 
 

*/

let uploadReceiptButton = document.getElementById("receipt");
uploadReceiptButton.addEventListener("change", showImage);

function showImage(file) {

    if (uploadReceiptButton.files && uploadReceiptButton.files[0]) {
        let filePlaceholder = document.getElementById("receipt-file");
        filePlaceholder.innerHTML = "";
        var reader = new FileReader();
        
        reader.onload = function(e) {
            let fileSpan = document.createElement("span");
            fileSpan.id = "file-and-del";
            fileSpan.className = "mb-2 flex just-center align-start w-75"
            // Create the image
            let img = document.createElement('img');
            img.id = "receipt-image";
            img.src = e.target.result;
            img.className = "w-100";
            img.alt = uploadReceiptButton.files[0].name;

            // append the image to the file span
            fileSpan.appendChild(img);

            // Create the accessible span to describe the delete button
            let deleteSpan = document.createElement("span");
            deleteSpan.className = "sr-only";
            deleteSpan.innerHTML = "Remove File";

            // create the delete icon
            let deleteIcon = document.createElement("i");
            deleteIcon.className = "fas fa-times-circle fa-2x";
            deleteIcon.ariaHidden = "true";

            // Create the delete button
            let deleteButton = document.createElement('button');
            deleteButton.id = "remove-file";
            deleteButton.type = "button";
            deleteButton.className = "btn btn-outline-danger del-butn";

            // apend the icon and accessible description to the delete button
            deleteButton.appendChild(deleteSpan);
            deleteButton.appendChild(deleteIcon);

            // add the deleteFile event listener to the delete button
            deleteButton.addEventListener("click", deleteFile);

            // append the delete button to the file Span
            fileSpan.appendChild(deleteButton);

            filePlaceholder.appendChild(fileSpan);


        }

        reader.readAsDataURL(uploadReceiptButton.files[0]);

        scanReceipt(uploadReceiptButton.files[0]);
    }

}

// This script removes the File from the FileList and removes the displayed contents on the screen

let filePlaceholder = document.getElementById("receipt-file");
let delButn = document.getElementById("remove-file");
// reminder that uploadReceiptButton has been declared in an earlier script

delButn.addEventListener("click", deleteFile);

function deleteFile() {
    // Remove file from FileList
    uploadReceiptButton.value = "";

    // Remove contents of File placeholder
    filePlaceholder.innerHTML = "";
}

function scanReceipt(url) {
    fetch("https://microsoft-computer-vision3.p.rapidapi.com/generateThumbnail", {
        "method": "POST",
        "headers": {
            "x-rapidapi-host": "",
            "x-rapidapi-key": "",
            "content-type": "application/json",
            "accept": "application/json"
        },
        "body": {
            "url": ""
            // "url": "http://example.com/images/test.jpg"
        }
    })
    .then(response => {
        console.log(response);
    })
    .catch(err => {
        console.log(err);
    });
}