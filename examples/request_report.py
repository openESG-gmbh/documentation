import json

import environ
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

env = environ.Env()
env.read_env(".env")

api_base = "http://localhost:8000"
client = BackendApplicationClient(client_id=env("CLIENT_ID"))
session = OAuth2Session(client=client)

auth = HTTPBasicAuth(env("CLIENT_ID"), env("CLIENT_SECRET"))
token = session.fetch_token(token_url=f"{api_base}/o/token/", auth=auth)

if __name__ == "__main__":
    organizations = session.get(f"{api_base}/api/organizations/").json()

    # use existing org
    org = organizations["results"][0]
    print(json.dumps(org, indent=4))

    # Get existing report templates
    template = session.get(
        f"{api_base}/api/report-templates/").json()["results"][0]
    print(json.dumps(template, indent=4))

    # Get template details
    sections = session.get(
        f"{api_base}/api/report-templates/{template['id']}/sections"
    ).json()
    print(json.dumps(sections, indent=4))

    # Create report request
    request = session.post(
        f"{api_base}/api/report-requests/for-organization/",
        json={
            "report_template": template["id"],
            "company_name": "Mustermann GmbH",
            "user_email": "max-1@mustermann.de",
            "user_first_name": "Max",
            "user_last_name": "Mustermann",
        },
    ).json()
    print(json.dumps(request, indent=2))

    # Retrieve report data
    request = session.get(
        f"{api_base}/api/report-requests/{request['report_request']['id']}/details"
    ).json()
    print(json.dumps(request, indent=2))
