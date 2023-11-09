#!/bin/bash

# execute query and store result in s3
aws athena start-query-execution --query-string "select count(*) from field_field6" --query-execution-context Database=technicalportfolio --result-configuration OutputLocation=s3://technical-portfoilo-query-result

# download the query result from s3
mkdir query-result
aws s3 sync s3://technical-portfoilo-query-result ../data/query-result
