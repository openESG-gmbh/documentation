# Organizations

All data in the system is related to an organization. Organizations can be
related, you are able to create a new organization, and will be able to add
new reports to that newly created organization.

```python
organizations = session.get(f"{api_base}/api/organizations/").json()["results"]

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
    # create a new organization, which will be linked to our organization
    # with an authorization grant, that can be revoked by the organization
    org_id = session.post(
        f"{api_base}/api/organizations/",
        {
            "name": "Test Client",
            "type": "gmbh",
            "vat_id": "DE356190424",
            "court_of_registration": "Frankfurt am Main",
            "registration_no": "123123",
            "homepage": "http://foo.bar",
        },
    ).json()["id"]
    print(f"Organization {org_id} created")
```
