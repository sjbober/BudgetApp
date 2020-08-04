

// let this_month_expenses = "{{ exp_by_categ }}";

window.addEventListener("load",getMonthlyExpenses('',''));

// come back to this later
// Initiate a fetch call to create a category
function getMonthlyExpenses(month,year) {

    let theData = {
        'month': month,
        'year': year,
    }

    fetch("", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json;charset=utf-8"
        },
        body: JSON.stringify(theData)
    }).then(function(response) {
        return response.json();
    }).then(function(data) {

        if (data.result == 'error') { // there was an error, display it
            displayError(data.error); 

        } else { // no errors
            console.log(data);
            prepareData(data.expenses);
            // let categories, sums, colors = prepareData(data.expenses);
            // console.log(categories,sums,colors);
            // generatePieCharts(categories,sums,colors);

        }
        
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

} 

// Get cookie for a form submit
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function prepareData(expenses) {
    let categories = [];
    let sums = [];
    let backgroundColors = [];
    let borderColors = [];

    for (const category of Object.entries(expenses)) {
        categories.push(category[0]);
        sums.push(category[1]);
        console.log(category[0]);
        console.log(category[1]);
        // console.log(category.RBG_colors);
        // Generate random color, and corresponding darker color (for border)
        let randomColors = generateRandomRGB();

        let color = 'rgba(' + randomColors[0] + ', ' + randomColors[1] + ', ' + randomColors[2] + ', ' + .2 + ')';
        backgroundColors.push(color);
        let darkerColor = 'rgba(' + randomColors[0] + ', ' + randomColors[1] + ', ' + randomColors[2] + ', ' + 1 + ')';
        borderColors.push(darkerColor);
    }

    generatePieCharts(categories,sums,backgroundColors);


}

function generateRandomNumber(max) {
    return Math.floor(Math.random() * max);
}


function generateRandomRGB() {
    let red = generateRandomNumber(256);
    let green = generateRandomNumber(256);
    let blue = generateRandomNumber(256);

    return [red, green, blue]
}


// generatePieCharts()
function generatePieCharts(categories,sums,backgroundColors,borderColors) {
    let ctx = document.getElementById('myChart').getContext('2d');

    let myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: categories,
            datasets: [{
                // label: '# of Votes',
                data: sums,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                borderWidth: 1
            }]
        }
    });
}

// function generatePieCharts() {
//     let ctx = document.getElementById('myChart').getContext('2d');

//     let myChart = new Chart(ctx, {
//         type: 'pie',
//         data: {
//             labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//             datasets: [{
//                 // label: '# of Votes',
//                 data: [12, 19, 3, 5, 2, 3],
//                 backgroundColor: [
//                     'rgba(255, 99, 132, 0.2)',
//                     'rgba(54, 162, 235, 0.2)',
//                     'rgba(255, 206, 86, 0.2)',
//                     'rgba(75, 192, 192, 0.2)',
//                     'rgba(153, 102, 255, 0.2)',
//                     'rgba(255, 159, 64, 0.2)'
//                 ],
//                 borderColor: [
//                     'rgba(255, 99, 132, 1)',
//                     'rgba(54, 162, 235, 1)',
//                     'rgba(255, 206, 86, 1)',
//                     'rgba(75, 192, 192, 1)',
//                     'rgba(153, 102, 255, 1)',
//                     'rgba(255, 159, 64, 1)'
//                 ],
//                 borderWidth: 1
//             }]
//         }
//     });
// }