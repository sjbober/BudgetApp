// When the user toggles the "date range?" checkbox, the input and label will toggle between a single date picker and a date range picker

let rangeCheckbox = document.getElementById("use-range");
rangeCheckbox.addEventListener("change",changeDateInput);
window.addEventListener("load",changeDateInput);

function changeDateInput() {
    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");

    if (rangeCheckbox.checked == true) {
        // Remove single date input
        singleInput.className = "d-none";
        rangeInput.className = "form-control w-50";

    } else if (rangeCheckbox.checked == false) {
        // If the checkbox is being unchecked, revert to original state with a single date picker
        rangeInput.className = "d-none";
        singleInput.className = "form-control w-50";

    }

}

