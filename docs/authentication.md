## Retrieving access credentials

You'll need your registered oAuth applications `client_id` and `client_secret`.

```bash
curl -u '<client_id>:<client_secret>' \
     -X POST -H "Content-Type: application/x-www-form-urlencoded" \
     "https://demo.openesg.de/o/token/" \
     -d "grant_type=client_credentials"
```

This gives us the access token.

```json
{
  "access_token": "sbKAFfq1btNSorhZBLBxmuaoArrBrY",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write"
}
```

Example (Python):

```python
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

api_base = "https://demo.openesg.de"
client = BackendApplicationClient(client_id=env("CLIENT_ID"))
session = OAuth2Session(client=client)

auth = HTTPBasicAuth(env("CLIENT_ID"), env("CLIENT_SECRET"))
token = session.fetch_token(token_url=f"{api_base}/o/token/", auth=auth)
```
