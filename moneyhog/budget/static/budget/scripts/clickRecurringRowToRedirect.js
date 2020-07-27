// When the user selects a row in the list of Expenses, they will be redirected to the Expense detail page

//  Add event listeners to each row in the table
let row = document.getElementsByClassName("click");
for (let i =0; i < row.length; i++) {
  row[i].addEventListener("click",redirect);

}

// If a row is clicked, check if it was the
// delete button that was clicked. If it is,
// open the delete modal. If it isn't,
// redirect the user to the edit page
function redirect(evt) {
  
  if (evt.target.className == "fas fa-trash-alt") {

  } else {
    console.log(evt);
    let pk = evt.target.parentElement.id;
    window.location = "/budget/expenses/recurring/" + pk;
  }

}