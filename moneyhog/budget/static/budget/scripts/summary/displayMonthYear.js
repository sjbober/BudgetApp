
/* This code is responsible for populating the Month/Year info 
in the page title and also in the button dropdowns. 
When the page loads, this info is immediately populated with
the current month and year. When a user selects a month or year
from the dropdown, the title and buttons are populated with the
selected info.

Once the title and buttons are updated, the function to generate pie
charts based on that month/year is called 

*/

window.addEventListener("load",displayMonthYear);

let monthDropdown = document.getElementById("monthDropdown");
let yearDropdown = document.getElementById("yearDropdown");

monthDropdown.addEventListener("click",displayMonthYear);
yearDropdown.addEventListener("click",displayMonthYear);


function displayMonthYear(evt) {
    let monthButton = document.getElementById("monthDropdownButton");
    let yearButton = document.getElementById("yearDropdownButton");
    let monthTitle = document.getElementById("month");
    let yearTitle = document.getElementById("year");

    let year;
    let monthLabel;
    let month;

    removePies();
    if (evt.type == "load") {
        let today = new Date();
        monthLabel = convertMonthToString(today.getMonth());
        month = today.getMonth() + 1;
        year = today.getFullYear();
        
        monthButton.innerHTML = monthLabel;
        yearButton.innerHTML = year;
        monthTitle.innerHTML = monthLabel;
        yearTitle.innerHTML = year;

        getMonthlyExpenses(month,year);

    } else if (evt.target.parentNode.id == "monthDropdown") {
        year = Number(yearTitle.innerHTML);

        // get the newly selected month
        monthLabel = evt.target.innerHTML;
        month = convertMonthToPythonInt(monthLabel);
        // console.log();

        // change the month title/button
        monthTitle.innerHTML = monthLabel;
        monthButton.innerHTML = monthLabel;

        getMonthlyExpenses(month,year);

    } else if (evt.target.parentNode.id == "yearDropdown") {

    }
}

function convertMonthToString(month) {
    let monthString;
    switch(month) {
        case 0:
            monthString = "January";
            break;
        case 1:
            monthString = "February";
            break;
        case 2:
            monthString = "March";
            month = 3;
            break;
        case 3:
            monthString = "April";
            break;
        case 4:
            monthString = "May";
            break;
        case 5:
            monthString = "June";
            break;
        case 6:
            monthString = "July";
            break;            
        case 7:
            monthString = "August";
            break;
        case 8:
            monthString = "September";
            break;
        case 9:
            monthString = "October";
            break;
        case 10:
            monthString = "November";
            break;
        case 11:
            monthString = "December";
            break;
    }

    return monthString;
}

function convertMonthToPythonInt(monthLabel) {
    let month;
    switch(monthLabel) {
        case "January":
            month = 1;
            break;
        case "February":
            month = 2;
            break;
        case "March":
            month = 3;
            break;
        case "April":
            month = 4;
            break;
        case "May":
            month = 5;
            break;
        case "June":
            month = 6;
            break;
        case "July":
            month = 7;
            break;            
        case "August":
            month = 8;
            break;
        case "September":
            month = 9;
            break;
        case "October":
            month = 10;
            break;
        case "November":
            month = 11;
            break;
        case "December":
            month = 12;
            break;
    }
    return month;
}

function removePies() {
    console.log("remove pies");
    let spendPie = document.getElementById("pieSpending");
    // let savePie = document.getElementById("pieSavings");

    spendPie.innerHTML = "";
    // savePie.innerHTML = "";
}