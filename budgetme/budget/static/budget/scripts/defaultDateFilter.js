// The JS date picker library adds a default date if none is given; however, if the user does not click inside of the input and selects "Save Search", that default date is not sent to the server. Creating a function to add a default date that will be sent to the server in case the user selects "Save Search" without clicking inside the date field, assuming the default date will be given


window.addEventListener("load", addTodaysDate);

function addTodaysDate() {
    // Input for single date picker
    let singleDate = document.getElementById("singledate");

    // Get today's date
    let todayFullDate = new Date();

    let year = todayFullDate.getFullYear();

    let month = todayFullDate.getMonth() + 1;

    // If the month is one digit, add a leading zero
    if (month.toString().length == 1) {
        month = "0" + month;
    }

    let day = todayFullDate.getDate();

    // If the day is one digit, add a leading zero
    if (day.toString().length == 1) {
        day = "0" + day;
    }

    // JS libray expected date format: mm/dd/yyyy
    let today = month + "/" + day + "/" + year;

    // Set the default value for single date picker to today's date
    // singleDate.value = today;
    singleDate.value = "mm/dd/yyyy"
}