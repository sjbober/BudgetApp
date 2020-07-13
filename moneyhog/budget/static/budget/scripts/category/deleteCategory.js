

// let addButton = document.getElementById("add-category-btn");

//
let deleteForms = document.getElementsByClassName("delete-form");

for (let i = 0; i < deleteForms.length; i++) {
    deleteForms[i].addEventListener("submit",function(event) {
        event.preventDefault();
        let cat_name = event.submitter.id.slice(6,-3);
        // console.log(cat_id);
        deleteCategory(cat_name);
    });
}

// Initiate a fetch call to create a category
function deleteCategory(name) {

    let theData = {
        'name': name,
        'purpose': 'delete',
    }

    fetch("", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json;charset=utf-8"
        },
        body: JSON.stringify(theData)
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data['result'] == "error") { // the category was not created successfully
            displayDeleteError(name);

        } else if (data['result'] == "success") { // a category was created successfully     
            closeFormModal("delete" + name);  
            deleteCategoryRow(name);

        }
        

        
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

} 


// Close the category delete modal
function closeFormModal(id) {
    $('#' + id).modal('toggle')

}

// Add the category row to the UI using the given
// category name
function deleteCategoryRow(name) {
    let catList = document.getElementById("category-list");
    let categ = document.getElementById(name);
    catList.removeChild(categ);
    if (catList.children.length == 1) {
        addNoCategText();
    }
}

//  Remove the instruction text intended for when
//  there are no categories.
function addNoCategText() {
    let noCatText = document.getElementById("no-categ");
    noCatText.innerHTML = `
    <p class="text-center title-med mb-3">You don't have any categories right now. Click the "New" button to create some!</p>
    <h3 class="imp title-sm"><i class="fas fa-question-circle"></i> What is a category?</h3>
    <p class="">Categories are ways for you to organize your spending to see where most of your money is going. Rent/Mortgage, Groceries, Eating Out, Electric Bill and Phone are some examples of categories you might create to track your spending.</p>
    `;
}



// Display any errors in the dialog box itself
function displayDeleteError(name) {
    let id = "delete-error-" + name
    let errorLocation = document.getElementById(id);
    errorLocation.className = "alert alert-danger";
    errorLocation.innerHTML = "An error occurred while trying to delete this category. Please try again later.";
}


// Get a fresh cookie for a form submit
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}