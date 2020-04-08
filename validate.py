import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException


# create an instance of the API class
api_instance = cloudmersive_validate_api_client.DomainApi()
domain = 'cloudmersive.com' # str | Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes.

# Configure API key authorization: Apikey

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '0acd1416-c3d7-4031-b177-07a498332cb1'

try:
    # Validate a domain name
    api_response = api_instance.domain_check(domain)
    print(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_check: %s\n" % e)