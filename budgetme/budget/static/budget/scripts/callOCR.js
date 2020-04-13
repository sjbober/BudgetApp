<script src="https://cdn.cloudmersive.com/jsclient/cloudmersive-ocr-client.js"></script>

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
var csrftoken = getCookie('csrftoken');

let url = "{% url 'budget:read_receipt' %}";

uploadReceiptButton.addEventListener("change", readReceipt);

function readReceipt() {
    let newForm = new FormData();
    newForm.append("file", uploadReceiptButton.files[0]);
    // console.log(newForm);
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
              //code
              console.log(data)
              console.log(data['path'])
              return call_OCR(data['path']);
          }).catch(err => {
              console.log('Error: ', err)
          })

    // return call_OCR(data.get('path'));

    
}

uploadReceiptButton.addEventListener("change", call_OCR);

function call_OCR(filePath) {
    
    // var fs = require('fs');
    var defaultClient = cloudmersiveOcrApiClient.ApiClient.instance;
        
    // Configure API key authorization: Apikey
    var Apikey = defaultClient.authentications['Apikey'];
    Apikey.apiKey = "04d1a7be-c9d1-4d93-8ec4-e7545c2a570a"
    
    var api = new cloudmersiveOcrApiClient.ImageOcrApi()
    
    // var imageFile = fs.readFileSync("C:\\temp\\page.png"); // {File} Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
    
    // var imageFile = fs.readFileSync(filePath);
    var reader = new FileReader();
    var image_file = reader.readAsDataURL(uploadReceiptButton.files[0]);

    
    var callback = function(error, data, response) {
        if (error) {
            console.error(error);
        } else {
            console.log('API called successfully. Returned data: ' + data);
        }
    };
    // api.imageOcrPost(Buffer.from(pageBytes.buffer), callback);
    api.imageOcrPost(1024, callback);
}

