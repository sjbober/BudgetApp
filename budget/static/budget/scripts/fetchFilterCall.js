// Tried using this to make a fetch call to filter the expenses list. Wasn't working, so now I am using a URL, but saving this in case I come back to try this again..

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  // var csrftoken = getCookie('csrftoken');
  // console.log(csrftoken)
  // let url = "{% url 'budget:expense_list' %}";

  let dateFilterButton = document.getElementById("submit-date-filter");
  // console.log(dateFilterButton);
  // dateFilterButton.addEventListener("click", filterExpensesDate);

  function filterExpensesDate() {
    let url = "{% url 'budget:expense_list' %}";
    var csrftoken = getCookie('csrftoken');
      // console.log("working")
    let newForm = new FormData();
    let startDate = document.getElementById("start-date").value;
    let endDate = document.getElementById("end-date").value;
    console.log(startDate)
    console.log(typeof startDate);
    newForm.append("name", "date-filter");
    newForm.append("startdate", startDate);
    newForm.append("enddate", endDate);
    // for (var key of newForm.entries()) {
    // console.log(key[0] + ', ' + key[1])
    // }   

    const options = {
        method: 'POST',
        body: newForm,
        headers: {
          "X-CSRFToken": csrftoken,
        }
    };

    delete options.headers['Content-Type'];

    fetch(url, options)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            // console.log(data['path'])
            // return call_OCR(data['path']);
        }).catch(err => {
            console.log('Error: ', err)
        })

    // return call_OCR(data.get('path'));

      
  }