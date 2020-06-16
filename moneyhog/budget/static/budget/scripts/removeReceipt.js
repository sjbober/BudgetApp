// When a user is logging a new expense, they have the option to upload an image of their receipt. If they choose to remove the image, they can click the 'x' button next to the name of the picture to remove the image.

// Psuedo code:
// We need to add an event listener to the 'x' button and create a function that will remove the file. Once the button is clicked, we need to re-hide the placeholder div for the file name and remove the text from the innerHTML. We also need to get the file list and remove the file from it.

let removeFileButton = document.getElementById("remove-file");
removeFileButton.addEventListener("click", removeFile);
// let previewName = document.getElementById("receipt-file");

function removeFile() {
    // console.log('this is working so far');
    let uploadReceiptButton = document.getElementById("receipt");
    // let previewDiv = document.getElementById("receipt-preview");
    let previewName = document.getElementById("receipt-file");

    // previewDiv.classList.add("d-none");
    previewName.innerHTML = "";
    uploadReceiptButton.files[0].isValid = false;
    // console.log(uploadReceiptButton.files[0]);

}