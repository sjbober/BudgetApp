// When the page loads, deactivate the date picker, date range picker, and date range checkbox.
// Created this function because the date range picker plugin has some interesting behavior; if the single date picker is already disabled before the page finished loading, the date picker will not work


window.addEventListener("load",deactivateDates)

function deactivateDates() {

    let singleInput = document.getElementById("singledate");
    let rangeInput = document.getElementById("daterange");
    let rangeCheckbox = document.getElementById("use-range");

    singleInput.disabled = true;
    rangeInput.disabled = true;
    rangeCheckbox.disabled = true;



}

