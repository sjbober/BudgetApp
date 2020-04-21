// When the user toggles the "date range?" checkbox, the input and label will toggle between a single date picker and a date range picker

let rangeCheckbox = document.getElementById("use-range");
// console.log(rangeCheckbox)
rangeCheckbox.addEventListener("change",changeDateInput);
// console.log(rangeCheckbox);
function changeDateInput() {
    console.log("changed")
    // console.log(rangeCheckbox.prop("checked"))
    let singleLabel = document.getElementById("singledate-label");
    let singleInput = document.getElementById("singledate");
    let rangeLabel = document.getElementById("daterange-label");
    let rangeInput = document.getElementById("daterange");

    if (rangeCheckbox.checked == true) {
        console.log("is checked");
        // Remove single date label and input
        singleLabel.className = "d-none";
        singleInput.className = "d-none";
        // singleInput.value = "";

        rangeLabel.className = "imp";
        rangeInput.className = "form-control w-50";

    } else if (rangeCheckbox.checked == false) {
        // If the checkbox is being unchecked, revert to original state with a single date picker
        console.log("is not checked");
        rangeLabel.className = "d-none";
        rangeInput.className = "d-none";
        // rangeInput.value = "";

        singleLabel.className = "imp";
        singleInput.className = "form-control w-50";

    } else {
        console.log("neither checked or unchecked...")
    }

}

