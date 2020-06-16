// This short script adds a placeholder text to the first option in the Category select

let initialSelect = document.getElementsByTagName("option");
for (option of initialSelect) {
    if (option.value == "") {
        option.innerHTML = "None";
    }
}
