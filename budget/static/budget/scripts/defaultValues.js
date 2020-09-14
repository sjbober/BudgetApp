// Defaulting the appropriate search fields

window.addEventListener("load", defaultValues);

function defaultValues() {
    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");

    // Reminders of template variables:
    // let hasReceipt = "{{ has_receipt }}";
    // let dateChoice = "{{ date_choice }}";

    // Activating/disabling the date picker based on the selected value of the 
    // radio buttons, taking into account search results
    // console.log(dateChoice);
    if (dateChoice == "" || dateChoice == "All") {
        document.getElementById("id_date_choice_0").checked = true;
        singleInput.disabled = true;
        rangeInput.disabled = true;

    } else if (dateChoice == "single-date") {
        singleInput.disabled = false;
        rangeInput.disabled = false;

        rangeInput.className = "d-none";
        singleInput.className = "form-control w-50";

    } else if (dateChoice == "date-range") {
        singleInput.disabled = false;
        rangeInput.disabled = false;

        singleInput.className = "d-none";
        rangeInput.className = "form-control w-50";
    }


    if (!hasReceipt) {
        document.getElementById("id_has_receipt_0").checked = true;
    }
  }
