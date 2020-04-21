// Activating the calendars from js library from https://www.daterangepicker.com/


// Activate the single date picker calendar
$('input[name="singledate"]').daterangepicker(
    {singleDatePicker: true,}
  );

  
// Activate the date range picker
$('input[name="daterange"]').daterangepicker();
