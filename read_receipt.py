from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from pprint import pprint
# cloudmersive_validate_api_client
# Configure API key authorization: Apikey

# func(
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = '0acd1416-c3d7-4031-b177-07a498332cb1' #my api key
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
# image_file = '/path/to/file.txt' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
image_file = 'receipt.jpg'
recognition_mode = 'recognition_mode_example' # str | Optional, enable advanced recognition mode by specifying 'Advanced', enable handwriting recognition by specifying 'EnableHandwriting'.  Default is disabled. (optional)
language = 'ENG' # str | Optional, language of the input document, default is English (ENG). 
# preprocessing = 'preprocessing_example' 
# str | Optional, preprocessing mode, default is 'None'.  Possible values are None (no preprocessing of the image), and 'Advanced' (automatic image enhancement of the image before OCR is applied; this is recommended and needed to handle rotated receipts). (optional)

try:
    # Recognize a photo of a receipt, extract key business information
    api_response = api_instance.image_ocr_photo_recognize_receipt(image_file, recognition_mode=recognition_mode, language=language)
    # original: 
       # api_response = api_instance.image_ocr_photo_recognize_receipt(image_file, recognition_mode=recognition_mode, language=language, preprocessing=preprocessing)
    # pprint(api_response)
    return api_response
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_photo_recognize_receipt: %s\n" % e)
    return 