/* 
 

*/



function getMonthlyExpenses(month,year) {
    // Takes two ints

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
            prepareCategData(data.expenses,data.total_spending);
            // prepareSpendSave(data.total_spending,data.total_income);


        }
        
    }).catch(function(ex) {
            displayError(ex); 
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


function displayError(error) {
    let errorDiv = document.getElementById("error-message");
    errorDiv.className = "alert alert-danger";
    errorDiv.innerHTML = error;
}

function generateCategoryColors(categories){
    // # --primary: #593196; rgb(89,49,150)
    // # --secondary: #A991D4; rgb(169,145,212)
    // # --success: #13B955; rgb(19,185,85)
    // # --info: #009CDC; rgb(0,156,220)
    // # --warning: #EFA31D; rgb(239,163,29)
    // # --danger: #FC3939; rgb(252,57,57)
    // # --light: #F9F8FC; rgb(249,248,252)
    // # --dark: #17141F; rgb(23,20,31)

}

// Prepare the data for the Spending by Category chart.
// Call the generatePieCharts function with this data
function prepareCategData(expenses,spending) {
    spending = Number(spending);
    if (spending == 0) {
        buildAlertHTML("pieSpending", "You don't have any spending to show.");

    } else {
        const colors = ['#593186','#A991D4','#13B955','#009CDC','#EFA31D','#FC3939','#F9F8FC','#17141F'];
        let categories = [];
        let sums = [];

        for (const category of Object.entries(expenses)) {

            categories.push(category[0]);
            sums.push(Number(category[1]));
        }

        // categories.push("None");
        // sums.push(0);

        console.log(categories);
        console.log(sums);

        generatePieCharts(categories,sums,colors,'pieSpending');
    }
    
}

// Prepare the data for the Spending vs Savingby Category chart.
// Call the generatePieCharts function with this data
// function prepareSpendSave(spending,income) {
//     spending = Number(spending);
//     income = Number(income);

//     if (spending == 0 && income == 0) {
//         buildAlertHTML("pieSavings", "You don't have any spending or income to show.");

//     } else {
//         const colors = ['#009CDC','#13B955'];
//         let categories = ['Spending','Savings'];
//         let savings;

//         if (income < spending) {
//             savings = 0;
//         } else {
//             savings = income - spending;
//         }
        
//         sums = [spending,savings];

//         generatePieCharts(categories,sums,colors,'pieSavings');
//     }
    

// }

function buildAlertHTML(parentPie, message) {
    console.log("triggered");
    let alertDiv = document.createElement("div");
    alertDiv.className = "alert alert-primary mt-2";
    alertDiv.role = "alert";
    alertDiv.innerHTML = message;

    let pieDiv = document.getElementById(parentPie);
    pieDiv.appendChild(alertDiv);
}


function generatePieCharts(categories,sums,backgroundColors,elementID) {
    console.log("pie chart function called");
    var options = {
        chart: {
          type: 'pie',
          width: '45%',
        },
        series: sums,
        labels: categories,
        colors: backgroundColors,
        dataLabels: {
            enabled: true,
            style: {
                fontSize: '20px',
            },
        },          
        responsive: [{
            // Size under 700px wide
            breakpoint: 700,
            options: {      
                chart: {
                    width: "100%",
                },
                dataLabels: {
                    style: {
                        fontSize: '8px',
                    },
                }, 
                legend: {
                    position: 'bottom'
                  },
            } 
        }], 
        
    }
    
    var chart = new ApexCharts(document.querySelector("#" + elementID), options);
    chart.render();
}

