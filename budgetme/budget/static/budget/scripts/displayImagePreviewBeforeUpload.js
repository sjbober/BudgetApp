// Displays the image to be uploaded 

let uploadReceiptButton = document.getElementById("receipt");
uploadReceiptButton.addEventListener("change", showImage);

function showImage(file) {

    // preview.classList.add("mb-2");
    // console.log('triggered')
    if (uploadReceiptButton.files && uploadReceiptButton.files[0]) {
        let previewDiv = document.getElementById("receipt-preview");
        let fileSpan = document.getElementById("receipt-file");
        fileSpan.className = "mb-2 flex just-center";
        var reader = new FileReader();

        reader.onload = function(e) {
            fileSpan.innerHTML = "";
            let img = document.createElement('img');
            img.id = "receipt-image";
            img.src = e.target.result;
            img.className = "w-75";
            img.alt = uploadReceiptButton.files[0].name;
            fileSpan.appendChild(img);

            // document.getElementById("receipt-image").src = e.target.result;
            // document.getElementById("receipt-image").className = "w-100";
        }

        reader.readAsDataURL(uploadReceiptButton.files[0]);
    }

}

{/* <img id="receipt-image" src="#" alt="New Receipt"  class="w-50 d-none" /> */}