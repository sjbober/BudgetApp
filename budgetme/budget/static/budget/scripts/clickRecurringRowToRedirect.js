// When the user selects a row in the list of Expenses, they will be redirected to the Expense detail page

//  Add event listeners to each row in the table
let row = document.getElementsByClassName("click");
for (let i =0; i < row.length; i++) {
  row[i].addEventListener("click",redirect);

}

// If a row is clicked, redirect the user
function redirect(evt) {
  let pk = evt.target.parentElement.id;
  window.location = "/budget/expenses/recurring/" + pk;

}