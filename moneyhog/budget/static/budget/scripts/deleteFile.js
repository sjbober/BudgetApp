// This script removes the File from the FileList and removes the displayed contents on the screen

let filePlaceholder = document.getElementById("receipt-file");
let delButn = document.getElementById("remove-file");
// reminder that uploadReceiptButton has been declared in an earlier script
// let uploadReceiptButton = document.getElementById("receipt");


delButn.addEventListener("click", deleteFile);

function deleteFile() {
    // Remove file from FileList
    uploadReceiptButton.value = "";

    // Remove contents of File placeholder
    filePlaceholder.innerHTML = "";



}

