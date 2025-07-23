# CSV Upload

To request multiple reports via the openESG platform, you can upload a CSV file
containing the required information.

## CSV format

You should add a header to the csv file, to dynamically select, which data do you
want to provide.

You can select from the following fields.

* `organization_name`
* `organization_legal_form` (must be one of the following: `ab`, `adoer`, `ag`, `eg`, `ek`, `ek-ohg`, `gbr`, `gmbh`, `gmbh-co-kg`, `kg`, `kdoer`, `ltd`, `ohg`, `other`, `part-gmbb`, `partg`, `se`, `se-co-kg`, `sole-proprietorship`, `stiftung`, `stiftung-co-kg`, `ug`, `ug-co-kg`. Default: `gmbh`). Alternatively to the `key`, one can also pass the `name`, e.g. `GmbH` instead of `gmbh`  <!-- markdownlint-disable-line MD013 -->
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
* `organization_country` (must be one of the following: `AT`, `BE`, `CH`, `CZ`, `DE`, `DK`, `ES`, `FR`, `GB`, `HU`, `IT`, `LU`, `NL`, `PL`, `SE`, `TR`. Default: `DE`. Alternatively to the `code`, one can also pass the `name`, e.g. `Deutschland` instead of `DE`) <!-- markdownlint-disable-line MD013 -->
* `user_email`
* `user_salutation` (must be one of the following: `dear_mr`, `dear_mrs`, `good_day`.) <!-- markdownlint-disable-line MD013 -->
* `user_first_name`
* `user_last_name`
* `user_phone`
* `user_locale` (must be one of the following: `en_US`, `de_DE`, `fr_FR`, `es_ES` or `it_IT`. Default: `de_DE`) <!-- markdownlint-disable-line MD013 -->
* `user_timezone` (must be one of the tz database, e.g. `Europe/Berlin`. Default: `UTC`) <!-- markdownlint-disable-line MD013 -->
* `user_department`
* `personal_message`
* `customer_identifier` (can be used to filter reports or report requests)
* `proivder_notification` (must be one of the following: `directly`, `after_esg_risk_check`, `no_notification`. Default: `directly`) <!-- markdownlint-disable-line MD013 -->
* `requestor_email` (if not provided, the upload user will be used; otherwise, it will be used to check for an existing user in the current organization. If no matching user is found, a new user in the current organization will be created.) <!-- markdownlint-disable-line MD013 -->
* `requestor_first_name`
* `requestor_last_name`

The delimiter should be a comma (`,`) or a semicolon (`;`).

## CSV upload with pre-selected Report Template

### Mandatory fields (pre-selected Report Template)

* `organization_name`
* `user_email`

### Example (pre-selected Report Template)

Here is an example with three organizations:

```csv
organization_name,organization_legal_form,organization_vat_id,organization_email,organization_homepage,user_salutation,user_first_name,user_last_name,user_email,provider_notification
Test Customer,gmbh,DE123456789,test@customer.de,https://testcustomer.de,dear_mr,Max,Mustermann,max.mustermann@testcustomer.de,directly
Test Company,ag,DE123456788,test@company.de,https://testcustomer.de,dear_mr,Max,Mustermann,max.mustermann@testcustomer.de,no_notification
Test Company 2,ek-ohg,DE123456787,test@company2.de,https://testcomapny2.de,dear_mrs,Jane,Doe,jane.doe@testcompany2.de,directly
```

## General CSV upload

The general CSV upload is based on the regular CSV upload but offers you the
option to specify a Report Template per line

### Mandatory fields (general CSV upload)

* `organization_name`
* `user_email`
* `report_template` (must be either the ID or the key of the Report Template, e.g. `123` or `vsme`) <!-- markdownlint-disable-line MD013 -->

### Example (general CSV upload)

Here is an example with three organizations:

```csv
organization_name,organization_legal_form,organization_vat_id,organization_email,organization_homepage,user_salutation,user_first_name,user_last_name,user_email,provider_notification,report_template
Test Customer,gmbh,DE123456789,test@customer.de,https://testcustomer.de,dear_mr,Max,Mustermann,max.mustermann@testcustomer.de,directly,11
Test Company,ag,DE123456788,test@company.de,https://testcustomer.de,dear_mr,Max,Mustermann,max.mustermann@testcustomer.de,no_notification,vsme
Test Company 2,ek-ohg,DE123456787,test@company2.de,https://testcomapny2.de,dear_mrs,Jane,Doe,jane.doe@testcompany2.de,directly,vsme
```
