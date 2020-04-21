
window.addEventListener("load", defaultAmount);

function defaultAmount() {
    let minInput = document.getElementById("min-amount");
    let maxInput = document.getElementById("max-amount");
    var slider = document.getElementById('slider');

    // Initialize the slider
    noUiSlider.create(slider, {
        start: [0, 1000],
        connect: true,
        step: 1,
        range: {
            'min': 0,
            'max': 1000
        }
    });

    // Create an array of the html input values for amount
    var snapValues = [
        minInput,
        maxInput
    ];
    
    // When the slider updates, update the corresponding input values
    slider.noUiSlider.on('update', function (values, handle) {
        snapValues[handle].value = values[handle];
    });

    // When the input values change, the slider will change as well
    minInput.addEventListener('change', function (handle) {
        slider.noUiSlider.set([this.value, null]);
    });
    
    maxInput.addEventListener('change', function (handle) {
        slider.noUiSlider.set([handle, this.value]);
    });

}