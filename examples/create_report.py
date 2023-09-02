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

    # create or use existing client org
    if org := next(
        (
            organization
            for organization in organizations
            if organization["vat_id"] == "DE356190426"
        ),
        None,
    ):
        # we already have an org for that vat_id, using that one
        print(f"Existing org: {org['id']}")
        org_id = org["id"]
    else:
        # create a new organization, which will be linked to our organization
        # with an authorization grant, that can be revoked by the organization
        org = session.post(
            f"{api_base}/api/organizations/",
            {
                "name": "Test Client 123",
                "type": "gmbh",
                "vat_id": "DE356190426",
                "court_of_registration": "Kassel",
                "registration_number": "123123",
                "homepage": "http://foo.bar",
            },
        ).json()
        org_id = org["id"]
        print(f"Organization {org_id} created")

    # Get existing report templates
    template = session.get(f"{api_base}/api/report-templates/").json()[0]
    print(json.dumps(template, indent=4))

    # Get template details
    sections = session.get(
        f"{api_base}/api/report-templates/{template['id']}/sections"
    ).json()
    print(json.dumps(sections, indent=4))

    # Create report from template
    report = session.post(
        f"{api_base}/api/reports/from-template/",
        json={"template": template["id"], "organization": org_id},
    ).json()
    print(json.dumps(report, indent=4))

    # Make meta data accessible on 'field_type_id'
    field_types = {}
    for section in sections:
        for field_type in section["field_types"]:
            field_types[field_type["id"]] = field_type

    # prepare report values
    field_values_to_update = []
    for field_value in report["field_values"]:
        field_value["value"] = {
            "decimal": "1.00",
            "integer": "1",
            "string": "foo",
            "text": "bar",
            "boolean": "true",
            "eu_economic_activity": "12.12.12 | Fischerei",
            "daterange": "2020-01-01 - 2020-12-31",
        }[field_types[field_value["field_type"]]["metric_type"]["datatype"]]
        field_value["measurement"] = field_types[field_value["field_type"]][
            "measurements"
        ][0]["id"]
        field_values_to_update.append(field_value)

    # update report
    report = session.patch(
        f"{api_base}/api/reports/{report['id']}/",
        json={
            "template": template["id"],
            "organization": org_id,
            "field_values": field_values_to_update,
        },
    ).json()
    print(json.dumps(report, indent=4))
