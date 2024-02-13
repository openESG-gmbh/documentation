# CSV Upload

To request multiple reports via the openESG platform, you can upload a CSV file
containing the required information.

## CSV format

You should add a header to the csv file, to dynamically select, which data do you
want to provide.

You can select from the following fields.

* `organization_name`
* `organization_type` (must be one of the following: `ab`, `adoer`, `ag`, `eg`, `ek`, `ek-ohg`, `gbr`, `gmbh`, `gmbh-co-kg`, `kg`, `kdoer`, `ltd`, `ohg`, `other`, `part-gmbb`, `partg`, `se`, `se-co-kg`, `sole-proprietorship`, `stiftung`, `stiftung-co-kg`, `ug`, `ug-co-kg`). Alternatively to the `key`, one can also pass the `name`, e.g. `GmbH` instead of `gmbh`  <!-- markdownlint-disable-line MD013 -->
* `organization_vat_id`
* `organization_court_of_registration`
* `organization_commercial_register_number`
* `organization_homepage`
* `organization_email`
* `organization_phone`
* `organization_address_line_1`
* `organization_address_line_2`
* `organization_house_number`
* `organization_zip_code`
* `organization_city`
* `organization_country` (must be one of the following: `AT`, `BE`, `CH`, `CZ`, `DE`, `DK`, `ES`, `FR`, `GB`, `HU`, `IT`, `LU`, `NL`, `PL`, `SE`, `TR`. Default: `DE`). Alternatively to the `code`, one can also pass the `name`, e.g. `Deutschland` instead of `DE` <!-- markdownlint-disable-line MD013 -->
* `user_email`
* `user_gender` (must be one of the following: `male`, `female`, `diverse`, `not_specified`. Default: `not_specified`) <!-- markdownlint-disable-line MD013 -->
* `user_first_name`
* `user_last_name`
* `user_phone`
* `user_locale` (must be one of the following: `de`, `en`, `fr`, `es` or ``it. Default: `de`) <!-- markdownlint-disable-line MD013 -->
* `user_department`
* `personal_message`

You have to provide at least the following fields:
`organization_name,organization_type,organization_vat_id,user_first_name,user_last_name,user_email`

The delimiter should be a comma (`,`) or a semicolon (`;`).

## Example

Here is an example with three organizations:

```csv
organization_name,organization_type,organization_vat_id,organization_email,organization_homepage,user_first_name,user_last_name,user_email
Test Customer,gmbh,DE123456789,test@customer.de,https://testcustomer.de,Max,Mustermann,max.mustermann@testcustomer.de
Test Company,ag,DE123456788,test@company.de,https://testcustomer.de,Max,Mustermann,max.mustermann@testcustomer.de
Test Company 2,ek-ohg,DE123456787,test@company2.de,https://testcomapny2.de,Jane,Doe,jane.doe@testcompany2.de
```
