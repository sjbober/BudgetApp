// Initializing the amount slider

window.addEventListener("load", defaultAmount);

function defaultAmount() {
    let minInput = document.getElementById("min-amount");
    let maxInput = document.getElementById("max-amount");
    var slider = document.getElementById('slider');
    // let highestAmount = "{{ highest_amount }}";
    // let minAmount = "{{ min_amount }}";
    // let maxAmount = "{{ max_amount }}";
    console.log(highestAmount);
    let min,max;

    // Determine if the get request includes min or max values
    // If it does, use those as the starting values
    // If it doesn't, use 0 as the min amount and the highest expense amount as the max
    if (minAmount) {
        min = minAmount;
        minInput.value = minAmount;
    } else {
        min = 0;
    }

    if (maxAmount) {
        max = maxAmount;
    } else {
        // console.log(highestAmount)
        max = highestAmount;
    }
    // Initialize the slider
    noUiSlider.create(slider, {
        // start: [0, 1000],
        start: [min, max],
        connect: true,
        step: 1,
        range: {
            'min': 0,
            'max': highestAmount
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
    minInput.addEventListener('change', function () {
        slider.noUiSlider.set([this.value, null]);
    });
    
    maxInput.addEventListener('change', function () {
        slider.noUiSlider.set([null, this.value]);
    });

}