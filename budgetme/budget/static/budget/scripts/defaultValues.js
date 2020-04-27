// Defaulting the appropriate search fields

window.addEventListener("load", defaultValues);

function defaultValues() {
    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");
    let rangeCheckbox = document.getElementById("use-range");
    // let allDatesCheck = "{{ all_dates }}";
    // let hasReceipt = "{{ has_receipt }}";
    // console.log(typeof allDatesCheck)
    if (allDatesCheck == "" || allDatesCheck == "True") {
        document.getElementById("all-dates").checked = true;

        singleInput.disabled = true;
        rangeInput.disabled = true;
        rangeCheckbox.disabled = true;
    }

    // if (allDatesCheck != False) {
    //     document.getElementById("all-dates").checked = true;
    // }

    if (!hasReceipt) {
        document.getElementById("id_has_receipt_0").checked = true;
    }
  }
