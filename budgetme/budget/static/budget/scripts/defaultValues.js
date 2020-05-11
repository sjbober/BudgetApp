// Defaulting the appropriate search fields

window.addEventListener("load", defaultValues);

function defaultValues() {
    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");
    let rangeCheckbox = document.getElementById("use-range");
    // let allDatesCheck = "{{ all_dates }}";
    // let hasReceipt = "{{ has_receipt }}";

    if (allDatesCheck == "" || allDatesCheck == "True") {
        console.log(allDatesCheck);
        document.getElementById("all-dates").checked = true;

        singleInput.disabled = true;
        rangeInput.disabled = true;
        rangeCheckbox.disabled = true;
    }

    if (!hasReceipt) {
        document.getElementById("id_has_receipt_0").checked = true;
    }
  }
