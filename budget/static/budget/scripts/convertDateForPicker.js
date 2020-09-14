// If the date has not already been converted, convert it to the proper format for the date picker library. Then, call the function to activate the picker

window.addEventListener("load", convertDate);

function convertDate() {
    let date = document.getElementById("datepicker").value;

    if (date.indexOf('-') != -1) {
        dateList = date.split('-');
        let newDate = dateList[1] + '/' + dateList[2] + '/' +  dateList[0];
        document.getElementById("datepicker").value = newDate;

        // Once date has been converted, activate date picker
        activatePicker();

    } else {
        activatePicker();
    }
    
}