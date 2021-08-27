REQUEST_FORM_DATA_BOUNDARY = "REQUEST_FORM_DATA_BOUNDARY"
FORM_DATA_STARTING_PAYLOAD = '--{0}\r\nContent-Disposition: form-data; name=\\"'.format(REQUEST_FORM_DATA_BOUNDARY)
FORM_DATA_MIDDLE_PAYLOAD = '\"\r\n\r\n'
FORM_DATA_ENDING_PAYLOAD = '--{0}--'.format(REQUEST_FORM_DATA_BOUNDARY)
REQUEST_CUSTOM_HEADER = {
    'content-type': "multipart/form-data; boundary={}".format(REQUEST_FORM_DATA_BOUNDARY),
    'Content-Type': "",
    'cache-control': "no-cache"
}

def generate_form_data_payload(username,password):
    kwargs={
        'username':username,
        'password':password
    }
    payload = ''
    for key, value in kwargs.items():
        payload += '{0}{1}{2}{3}\r\n'.format(FORM_DATA_STARTING_PAYLOAD, key, FORM_DATA_MIDDLE_PAYLOAD, value)
    payload += FORM_DATA_ENDING_PAYLOAD
    return payload

# Pass your input as kwargs to the function
# Example:

# import requests

# API_URL = "www.example.com/verifyuser

# kwargs = {'ChannelId': channel_id,
#     'ReferenceNumber': reference_number,
#     'AccountNumber': account_numbers,
#     'Cnic': cnic,
#     'MobileNumber': mobile_number,
#     'Otp': otp}

# generate payload to be sent as form-data
# request_data = generate_form_data_payload(kwargs)
# response = requests.post(API_URL, headers=REQUEST_CUSTOM_HEADER, data=request_data)