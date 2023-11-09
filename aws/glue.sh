#!/bin/bash

# create glue database technicalPortfolio is name of database
aws glue create-database --database-input "{\"Name\":\"technicalPortfolio\"}"

# create crawler, target s3, role must have privilege to access s3 and glue
aws glue create-crawler --name techinicalPortfolio --databasename techincalPortfolio --targets "{\"S3Targets\":[{\"Path\":\"s3://techinical-portfoilo\"}]}" --role AWSGlueServiceRole-11im

# start crawler
aws glue start-crawler --name techincalPortfolio
