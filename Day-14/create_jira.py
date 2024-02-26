# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://user.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("email", "Apitoken")


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": { 
    "description": {
      "content": [
        {
          "content": [
            {
              "text": " My github jira ticket-2",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10006"
    },
    "project": {
      "key": "SUD"
    },
    "summary": "github issue Jira ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
