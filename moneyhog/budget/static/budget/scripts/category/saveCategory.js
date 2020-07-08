


function saveCategory(event) {

    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();

        var myData = {
            hello: 1
        };
        
        // "/api/v1/endpoint/5/"
        fetch("{% url 'budget:categories' %}", {
            method: "put",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify(myData)
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log("Data is ok", data);
        }).catch(function(ex) {
            console.log("parsing failed", ex);
        });


      }


}