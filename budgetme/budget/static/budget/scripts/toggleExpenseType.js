// One the New Expense screen, toggling the "recurring expense?" checkbox toggles between the one-time expense form and the recurring expense form

let typeCheck = document.getElementById("toggleType");
let oneTimeForm = document.getElementById("one-time");
let recurringForm = document.getElementById("recurring");

typeCheck.addEventListener("change", toggleExpenseType);

function toggleExpenseType() {
    console.log("change")
    if (typeCheck.checked == true) {

        oneTimeForm.className = "d-none";
        recurringForm.className = "inline-form";

    } else if (typeCheck.checked == false) {

        recurringForm.className = "d-none";
        oneTimeForm.className = "inline-form";
    }

}

