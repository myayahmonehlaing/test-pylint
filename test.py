import requests

url = "https://qcapp.optculture.com/subscriber/updateContactsOPT.mqrm"
headers = {
    "Content-Type": "application/json"
}

data = {
"header":{
"requestId":"123",
"requestDate":"2014-06-16 12:12:12",
"contactSource":"Store",
"contactList":"POS",
"sourceType":"store"
},
"customer":{
"customerId":"765875978834001",
"instanceId":"",
"membershipNumber":"",
"firstName":"Kiran",
"lastName":"OCtest",
"phone":"345436767",
"emailAddress":"kiranOCtest@maildrop.cc",
"addressLine1":"Road no #12",
"addressLine2":"",
"city":"Hyderabad",
"state":"AP",
"postal":"",
"country":"India",
"birthday":"",
"anniversary":"",
"gender":"",
"password":"",
"homeStore":"12",
"creationDate":"2024-12-19 12:12:12",
"UDF1":"xyz",
"UDF2":"home",
"UDF3":"123",
"UDF4":"route",
"UDF5":"",
"UDF6":"",
"UDF7":"",
"UDF8":"",
"UDF9":"",
"UDF10":"",
"UDF12":"",
"UDF13":"",
"UDF14":"",
"UDF15":"xyz1",
"loyalty":{
"enrollCustomer":"Y",
"mobileAppPreferences":{
"language":"English",
"pushNotifications":"True"
},
"fingerprintValidation":"false",
"password":""
},
"suppress":{
"email":{
"isTrue":"Y",
"reason":"Bounce",
"timestamp":"2024-12-19 12:12:12"
},
"phone":{
"isTrue":"N",
"reason":"",
"timestamp":"2024-12-19 12:12:12"
}
}
},
"user":{
    "userName": "QC_ToriTravel",
    "organizationId": "12345678",
    "token": "HYP5CF2F2QDRWPVY",
"sessionID":""
}
}




response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)


