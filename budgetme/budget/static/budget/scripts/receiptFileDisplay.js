// This script (1) removes the class that hides the placeholder div, and (2) displays the name of the uploaded file

let uploadReceiptButton = document.getElementById("receipt");
let preview = document.getElementById("receipt-preview");
let previewName = document.getElementById("receipt-file");
uploadReceiptButton.addEventListener("change", showFile);

function showFile() {
    preview.classList.remove("d-none");
    // uploadReceiptButton.files[0].isValid = true;

    // previewName.classList.add("sr-only");
    previewName.innerHTML = uploadReceiptButton.files[0].name;



    // previewName.value = uploadReceiptButton.files[0].name;
    // previewName.placeholder = uploadReceiptButton.files[0].name;
    // console.log(previewName);
    // console.log(uploadReceiptButton.files);
    // console.log(uploadReceiptButton.files[0]);
    // uploadReceiptButton.files[0].isValid = false;

    // console.log(uploadReceiptButton.files[0]);

}

