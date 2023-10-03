# CSV Upload

To request multiple reports via the openESG plattform, you can upload a CSV file
containing the required information.

## Default format

The default format is without a head, just the data.

```csv
organization_name,user_first_name,user_last_name,user_email,personal_message
```

Example:

```csv
Test Company GmbH,John,Doe,john.doe@testcompany.com
Test Company 2 GmbH,Jane,Doe,jane.doe@testcompany2.com,Please fill this out, Jane.
Test Firma GmbH,Max,Mustermann,max.mustermann@testfirma.de
```

## Custom format

You can add a header to the csv file, to dynamically select, which data do you
want to provide.

You can select from the following fields.

* `organization_name`
* `organization_type` (must be one of the following: `ag`, `ek-ohg`, `gbr`, `gmbh`, `gmbh-co-kg`, `part-gmbb`, `partg`, `ug`, `other`) <!-- markdownlint-disable-line MD013 -->
* `organization_vat_id`
* `organization_court_of_registration`
* `organization_registration_number`
* `organization_homepage`
* `organization_email`
* `organization_phone`
* `organization_address_line_1`
* `organization_address_line_2`
* `organization_house_number`
* `organization_zip_code`
* `organization_city`
* `organization_country` (must be one of the following: `DE`, `AT`, `CH`)
* `organization_external_data`
* `user_first_name`
* `user_last_name`
* `user_alias`
* `user_email`
* `user_locale` (must be one of the following: `de`, `en`)
* `user_department`
* `user_phone`
* `personal_message`

You have to provide at least the following fields:
`organization_name,organization_type,organization_vat_id,user_first_name,user_last_name,user_email`

Example:

```csv
organization_name,organization_type,organization_vat_id,organization_email,organization_homepage,user_first_name,user_last_name,user_email
Test Customer,gmbh,DE123456789,test@customer.de,https://testcustomer.de,Max,Mustermann,max.mustermann@testcustomer.de
Test Company,ag,DE123456788,test@company.de,https://testcustomer.de,Max,Mustermann,max.mustermann@testcustomer.de
Test Company 2,ek-ohg,DE123456787,test@company2.de,https://testcomapny2.de,Jane,Doe,jane.doe@testcompany2.de
```
