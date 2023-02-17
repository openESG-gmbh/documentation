# OpenESG API

## Retrieving access credentials

You'll need your registered oAuth applications `client_id` and `client_secret`.

```bash
curl -u '<client_id>:<client_secret>' \
     -X POST -H "Content-Type: application/x-www-form-urlencoded" \
     "https://app.dev.openesg.de/o/token/" \
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

api_base = "https://app.dev.openesg.de"
client = BackendApplicationClient(client_id=env("CLIENT_ID"))
session = OAuth2Session(client=client)

auth = HTTPBasicAuth(env("CLIENT_ID"), env("CLIENT_SECRET"))
token = session.fetch_token(token_url=f"{api_base}/o/token/", auth=auth)
```

## Organizations

All data in the system is related to an organization. Organizations can be related, you are able to create a new
organization, and will be able to
add new reports to that newly created organization.

```python
organizations = session.get(f"{api_base}/api/organizations/").json()

# create or use existing client org
if org := next(
    (
        organization
        for organization in organizations
        if organization["vat_id"] == "DE356190424"
    )
):
    # we already have an org for that vat_id, using that one
    org_id = org["id"]
    print(f"Existing org: {org_id}")
else:
    # we are creating a new organization, which will be linked to our organization with
    # an authorization grant, that can later be revoeked by the organization
    org_id = session.post(
        f"{api_base}/api/organizations/",
        {
            "name": "Test Client",
            "company_name": "Test Client",
            "company_type": "gmbh",
            "vat_id": "DE356190424",
            "court_of_registration": "Kassel",
            "registration_no": "123123",
            "homepage": "http://foo.bar",
        },
    ).json()["id"]
    print(f"Organization {org_id} created")
```

## Report Templates

Report templates define the structure of reports and associated data. Templates details are available at the `/sections`
actions, and not returned with the main resource .

Reports are created based on one of the predefined templates. Available templates may vary based on organization, they
are specific to the currently authorized organization.

```python
# Get existing report templates
template = session.get(f"{api_base}/api/report-templates/").json()[0]

# Get template details
sections = session.get(
    f"{api_base}/api/report-templates/{template['id']}/sections"
).json()
```

### Sections

Section is a subgrouping of templates, sections are hierarchical, this relationship is represented by the `parent` field
in serialized JSON.

### Field Types

Sections do define field types, which are the definition of a fields structure and semantics. The field type defines a
technical `key`, the `metric_type` and possible `measurements`.

## Report

Reports are the entities, that group submitted field values into a logical collection, they are created from a template,
using the `/from_template` action.

```python
# Create report from template
report = session.post(
    f"{api_base}/api/reports/from_template/",
    json={"template": template["id"], "organization": org_id},
).json()
```

Meta-data on the meaning of the different report fields is provided by the report templates sections.
For every field value there is a corresponding type definition within the template sections.

```python
# Make meta data accessible on 'field_type_id'
field_types = {}
for section in sections:
    for field_type in section["field_types"]:
        field_types[field_type["id"]] = field_type
```

In order to update report values the `PATCH` method is supplied with any field values, that need updates.

```python
# prepare report values
field_values_to_update = []
for field_value in report["field_values"]:
    field_value["value"] = {
        "decimal": "1.00",
        "integer": "1",
        "string": "foo",
        "text": "bar",
        "eu_econmic_activity": "12.12.12 | Fischerei",
    }[field_types[field_value["field_type"]]["metric_type"]["datatype"]]
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
```
In this example, we were setting field values with dummy data based on field type definitions.
