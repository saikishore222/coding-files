import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
response = sendPostRequest(URL, 'P04JMGW39QIVLEEB36BQ9FKM5E68WP9W', 'IZ1UUYAKPGRV4WXL', 'stage', 'xxxxxxxxxxxx', 'saikishore.chsk@gmail.com', 'Hello world' )
print (response.text)
