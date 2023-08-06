Report templates define the structure of reports and associated data. Templates
details are available at the `/sections` actions, and not returned with the
main resource.

Reports are created based on one of the predefined templates. Available
templates may vary based on organization, they are specific to the currently
authorized organization.

```python
# Get existing report templates
template = session.get(f"{api_base}/api/report-templates/").json()["results"][0]
```

Example response:

```json
{
	"id": 1,
	"organization": null,
	"key": "esg.reporting_standard",
	"name": "ESG Reporting",
	"description": "Standard ESG Reporting",
	"catalog": {
		"id": 1,
		"key": "esg_base",
		"name": "ESG Base"
	}
}
```

### Sections

Section is a subgrouping of templates, sections are hierarchical, this
relationship is represented by the `parent` field in serialized JSON.

### Field Types

Sections do define field types, which are the definition of a fields structure
and semantics. The field type defines a technical `key`, the `metric_type` and
possible `measurements`.

### Retrieving sections and field types

```python
# Get template details
sections = session.get(
    f"{api_base}/api/report-templates/{template['id']}/sections"
).json()
```

Example response:

```json
[
	{
		"id": 1,
		"key": "esg.environment",
		"name": "Umwelt",
		"description": "Lorem Ipsum",
		"is_commentable": true,
		"multi_instance": false,
		"field_types": [],
		"parent_id": 1
	},
	{
		"id": 2,
		"key": "esg.environment.electricity",
		"name": "Stromverbrauch",
		"description": "",
		"is_commentable": true,
		"multi_instance": false,
		"field_types": [
			{
				"id": 1,
				"key": "esg.environment.electricity",
				"name": "Stromverbrauch",
				"label": "kWh",
				"metric_type": {
					"id": 4,
					"key": "electricity.amount",
					"name": "Energy",
					"datatype": "decimal",
					"units": [
						{
							"id": 2,
							"key": "electricity.kwh",
							"name": "kWH"
						}
					]
				},
				"measurements": [
					{
						"id": 2,
						"key": "estimation",
						"name": "Estimation"
					},
					{
						"id": 3,
						"key": "measurement",
						"name": "Measurement"
					}
				],
				"attachment": "optional",
				"is_commentable": true,
				"required": true
			}
		],
		"parent_id": 2
	}
]
```
