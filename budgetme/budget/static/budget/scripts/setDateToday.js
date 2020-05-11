// Upon clicking "Today", the date field will get auto populated with today's date. This is currently used for the New Expense form
let date = document.getElementById("datepicker");
let todayButton = document.getElementById("today");

todayButton.addEventListener("click",addTodaysDate)

function addTodaysDate() {
    let todayFullDate = new Date();

    let year = todayFullDate.getFullYear();

    let month = todayFullDate.getMonth() + 1;
    // console.log(month.length);
    
    if (month.toString().length == 1) {
        // console.log("month is 1 digit");
        month = "0" + month;
        // console.log(month);
    }

    let day = todayFullDate.getDate();
    if (day.toString().length == 1) {
        day = "0" + day;
    }

    // let today = year + "-" + month + "-" + day;
    let today = month + "/" + day + "/" + year;

    date.value = today;

}
