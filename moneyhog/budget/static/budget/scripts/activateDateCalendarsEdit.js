// Activating the calendars from js library from https://www.daterangepicker.com/

// Activate the date picker calendar
function activatePicker() {
    $('input[id="datepicker"]').daterangepicker(
        {singleDatePicker: true,
        autoUpdateInput: true}
        );
}