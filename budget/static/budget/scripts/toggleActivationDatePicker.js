// Toggling between "all", "single", and "range" radio boxes will disable/activate
// the appropriate date picker 

let all = document.getElementById("id_date_choice_0");
let single = document.getElementById("id_date_choice_1");
let range = document.getElementById("id_date_choice_2");

all.addEventListener("click",toggleDatePicker);
single.addEventListener("click",toggleDatePicker);
range.addEventListener("click",toggleDatePicker);

function toggleDatePicker() {

    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");

    if (all.checked) {
        singleInput.disabled = true;
        rangeInput.disabled = true;

    } else if (single.checked) {
        singleInput.disabled = false;
        rangeInput.disabled = false;

        rangeInput.className = "d-none";
        singleInput.className = "form-control w-50";

    } else if (range.checked) {
        singleInput.disabled = false;
        rangeInput.disabled = false;

        singleInput.className = "d-none";
        rangeInput.className = "form-control w-50";
    }

}

