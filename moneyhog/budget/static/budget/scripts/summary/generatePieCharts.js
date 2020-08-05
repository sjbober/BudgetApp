

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
            console.log(data.expenses,data.colors);
            prepareData(data.expenses,data.colors);
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

function prepareData(expenses,colors) {
    let categories = [];
    let sums = [];
    let backgroundColors = [];
    let borderColors = [];

    let i = 0;
    for (const category of Object.entries(expenses)) {

        categories.push(category[0]);
        sums.push(category[1]);

        // Generate colors
        let pos = i % colors.length;
        let r = colors[pos][0] + Math.floor(i/colors.length);
        let g = colors[pos][1];
        let b = colors[pos][2];
        let a_fill = .2;
        let a_border = 1;

        // Fill color
        let color = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + a_fill + ')';
        backgroundColors.push(color);

        // Border color
        let darkerColor = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + a_border + ')';
        borderColors.push(darkerColor);

        console.log(color);
        console.log(darkerColor);
        i++;
    }

    generatePieCharts(categories,sums,backgroundColors,borderColors);


}


function generatePieCharts(categories,sums,backgroundColors,borderColors) {
    let ctx = document.getElementById('byCateg').getContext('2d');

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