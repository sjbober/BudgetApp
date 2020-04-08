// 

// let uploadReceiptButton = document.getElementById("receipt");
// let preview = document.getElementById("receipt-preview");
// let previewName = document.getElementById("receipt-file");
uploadReceiptButton.addEventListener("change", showImage);

function showImage(file) {
    if (uploadReceiptButton.files && uploadReceiptButton.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            document.getElementById("receipt-image").src = e.target.result;
            document.getElementById("receipt-image").className = "w-100";
        }

        reader.readAsDataURL(uploadReceiptButton.files[0]);
    }

}

