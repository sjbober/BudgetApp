

let addButton = document.getElementById("add-category-btn");


let catForm = document.getElementById("cat-form");
catForm.addEventListener("submit",function(event) {
    event.preventDefault();
    saveCategory();
});


function addCategoryRow(name) {
    let catList = document.getElementById("category-list");
    let newHTML = `  
                <li class="list-group-item flex align-center just-betw">
                    <div class="flex align-center">
                        <button type="button" class="btn btn-outline-primary title-med mr-3 imp"><i class="fas fa-pen"></i> <span class="button-words">Edit</span></button>
                        <span class="title-xl">` + name + `</span>
                    </div>
                    
                    <button type="button" class="btn btn-outline-danger title-sm imp" data-toggle="modal" data-target="#delete` + value + `"><i class="fas fa-trash-alt"></i> <span class="button-words">Delete</span></button>

                    <div id="delete` + name + `" class="modal" tabindex="-1" role="dialog">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="title-xl imp">Delete Category</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body flex just-center">
                                    <p class="title-xl">Are you sure you want to delete your ` + name + ` category?</p>
                                </div>
                                <div class="modal-footer flex just-around">
                                    <form action="#" method="POST" class="inline-form" enctype="application/x-www-form-urlencoded"> 
                                        <button type="submit" class="btn btn-danger imp">Yes, delete it</button>
                                    </form>
                                    <button type="button" class="btn btn-primary imp" data-dismiss="modal">No, cancel</button>
                                </div>
                            </div>
                        </div>
                    </div>

                </li>          
                `;
                
        catList.innerHTML = newHTML + catList.innerHTML;

}









function saveCategory() {
    let value = document.getElementById("categoryName").value;

    let theData = {
        'name': value,
    }

    fetch("create-category/", {
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
        console.log("Data is ok", data);
        if (data.hasOwnProperty("error")) {
            displayError(data.error);

        } else {
            removeError();
            removeInputText();
            closeDialogBox();
            addCategoryRow(data.category_name);

        }
        

        
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

} // end function

function closeDialogBox() {
    $('#addCategory').modal('toggle')

}

function displayError(message) {
    let errorLocation = document.getElementById("error-message");
    errorLocation.className = "alert alert-danger";
    errorLocation.innerHTML = message;
}

function removeError() {
    let errorLocation = document.getElementById("error-message");
    errorLocation.className = "";
    errorLocation.innerHTML = "";
}

function removeInputText() {
    let inputBox = document.getElementById("categoryName");
    inputBox.value = "";
}

// Get a fresh cookie for this form submit
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