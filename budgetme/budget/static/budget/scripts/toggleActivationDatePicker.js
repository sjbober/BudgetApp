// When the user unchecks the "all dates" checkbox, the inputs and date range checkbox will be activated, and when the user re-checks the checkbox, those elements will be disbled

let allDatesCheckbox = document.getElementById("all-dates");
allDatesCheckbox.addEventListener("change", toggleDatePicker)

function toggleDatePicker() {
    console.log("changed")

    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");
    let rangeCheckbox = document.getElementById("use-range");

    if (allDatesCheckbox.checked) {
        singleInput.disabled = true;
        rangeInput.disabled = true;
        rangeCheckbox.disabled = true;

    } else if ( !allDatesCheckbox.checked) {
        singleInput.disabled = false;
        rangeInput.disabled = false;
        rangeCheckbox.disabled = false;

    } 

}

