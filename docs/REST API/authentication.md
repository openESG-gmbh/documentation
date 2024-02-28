# Authentication

You'll need your registered oAuth application's `client_id` and `client_secret`.
Then you can get an access token by sending a request to `POST /o/token/`.

## Example (cURL)

```bash
curl -u '<client_id>:<client_secret>' \
     -X POST -H "Content-Type: application/x-www-form-urlencoded" \
     "https://demo.openesg.de/o/token/" \
     -d "grant_type=client_credentials"
```

This gives you the access token, which is valid for 1 hours.

```json
{
    "access_token": "sbKAFfq1btNSorhZBLBxmuaoArrBrY",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write"
}
```

## Example (Python)

```python
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

API_BASE = "https://demo.openesg.de"

client = BackendApplicationClient(client_id=env("CLIENT_ID"))
session = OAuth2Session(client=client)

auth = HTTPBasicAuth(env("CLIENT_ID"), env("CLIENT_SECRET"))
token = session.fetch_token(token_url=f"{API_BASE}/o/token/", auth=auth)
```

## Example (Postman)

Create a new Postman Collection by importing the downloaded Open API 3.1 schema
JSON file. Then add the following `Pre-request Script` in the root of the
`Collection`:

```js
const tokenUrl = 'https://demo.openesg.de/o/token/';

const clientId = '<client-id>';
const clientSecret = '<client-secret>';

const getTokenRequest = {
  method: 'POST',
  url: tokenUrl,
  body: {
      mode: 'formdata',
      formdata: [
          { key: 'grant_type', value: 'client_credentials' },
          { key: 'client_id', value: clientId },
          { key: 'client_secret', value: clientSecret }
      ]
  }
};

pm.sendRequest(getTokenRequest, (err, response) => {
  const jsonResponse = response.json();
  const newAccessToken = jsonResponse.access_token;

  pm.variables.set('access_token', newAccessToken);
});
```

Now in the `Authorization` tab, set

* `Type` to `Bearer Token` and
* `Token` to `{{access_token}}`

All Endpoints should then use the authorization type `Inherit auth from parent`.
