// Activating the calendars from js library from https://www.daterangepicker.com/


// Activate the single date picker calendar
$('input[id="singledate"]').daterangepicker(
    {singleDatePicker: true,
    autoUpdateInput: true}
  );

  
// Activate the date range picker
$('input[id="daterange"]').daterangepicker();
