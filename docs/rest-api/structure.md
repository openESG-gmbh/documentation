# Overview

In the following sections, we will explain the fundamental structure of openESG
models.

## ReportTemplate

Report templates are the basis for reports. They define the structure and
content of a report, including the fields (FieldType).
Field types can help you match our data model to your own data model.

Endpoints:
<https://demo.openesg.de/api/v1/docs#/report-templates>

## ReportRequest

A requestor can create a report request based on a report template (via form,
CSV Upload or REST API).
A report request contains request relevant information (e.g. user and
organization who requested it) and also a reference to a report.

Endpoints:
<https://demo.openesg.de/api/v1/docs#/report-requests>

## Report

A report can optionally hold a reference to a report request. It consists of
field values (FieldValue), which itself are based on field types (FieldType).
A provider will answer a report by filling in the field values.

Besides its field values, a report can also contain metadata like the
reporting period (start and end date), progress, status and the assigned
provider (user and organization).

Endpoints:
<https://demo.openesg.de/api/v1/docs#/reports>

## FieldType

A field type defines the structure of a field in a report. It includes
information like:

- name and description
- data type (e.g., integer, decimal, short_text)
- min/max values
- units
- measurement types
- attachment

For a matching with your own data model, please refer to the `key` of a
FieldType.

## FieldValue

A field value is an instance of a field type and contains the actual data
provided by a provider in a report.
