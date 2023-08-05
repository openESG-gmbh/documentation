We may choose to request a report based on the available templates. In order to submit a report request, we need to
supply company and contact information.

```python
# Create report request
request = session.post(
    f"{api_base}/api/report-requests/for-organization/",
    json={
        "report_template": template["id"],
        "company_name": "Mustermann GmbH",
        "vat_id": "DE12312312", #optional
        "scoped_external_data": {"my_customer_id": "123123"}, #optional
        "user_email": "max@mustermann.de",
        "user_first_name": "Max",
        "user_last_name": "Mustermann",
    },
).json()
print(json.dumps(request, indent=2))
```

The submitted report has a `report_request_code` and `registration_code`, the `registration_code` will be supplied to the provided
contact, to finalize the registration. It will be `null`, if the supplied contact is already registered.

By default, a registration email will be sent to the supplied contact.

```json
{
  "report_request": {
    "id": 13,
    "organization": {
      "id": 3,
      "name": "MyOrg",
      "type": "gmbh",
      "vat_id": "DE123123123",
      "court_of_registration": "München",
      "registration_no": "12345",
      "homepage": "",
      "scoped_external_data": null
    },
    "user": null,
    "status": "created",
    "approved_at": null,
    "report": 13
  },
  "report_request_code": "UmVwb3J0VHlwZToxMw==",
  "registration_code": "7LWccc7KkvzqVnHQ"
}
```

### Retrieving report data

After a request has been submitted, you may retrieve the current data via the `/details` route. We can configure webhook
callbacks, that are triggered on status changes upon request.

```json
# Retrieve report data
request = session.get(
    f"{api_base}/api/report-requests/{request['report_request']['id']}/details"
).json()
```
