# Submitting a report

Reports are the entities, that group submitted field values into a logical
collection, they are created from a template, using the
`/reports/from-template` action.

```python
# Create report from template
report = session.post(
    f"{api_base}/api/reports/from-template/",
    json={"template": template["id"], "organization": org_id},
).json()
```

Meta-data on the meaning of the different report fields is provided by the
report templates sections. For every field value there is a corresponding type
definition within the template sections.

Example response:

```json
{
    "id": 14,
    "template": 1,
    "status": "requested",
    "progress": 0,
    "submitted_at": null,
    "organization": {
        "id": 9,
        "name": "Test Client",
        "...": "..."
    },
    "field_values": [
        {
            "id": 261,
            "organization": 9,
            "value": null,
            "value_complex": null,
            "comment": "",
            "measurement": null,
            "attachment": null,
            "instance_id": 1,
            "valid": false,
            "required": true,
            "section": 3,
            "field_type": 1
        },
        {
            "id": 262,
            "organization": 9,
            "value": null,
            "value_complex": null,
            "comment": "",
            "measurement": null,
            "attachment": null,
            "instance_id": 1,
            "valid": false,
            "required": true,
            "section": 4,
            "field_type": 2
        }
    ]
}
```

Here we create a 'helper' structure, to look up meta-data for each field type id:

```python
# Make meta data accessible on 'field_type_id'
field_types = {}
for section in sections:
    for field_type in section["field_types"]:
        field_types[field_type["id"]] = field_type
```

In order to update report values the `PATCH` method is supplied with any field
values that need updates.

```python
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
```

In this example, we were setting field values with dummy data based on field
type definitions.
