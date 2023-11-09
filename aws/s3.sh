#!/bin/bash

# technical-portfolio is name of bucket, change if error occurs
aws s3 mb s3://technical-portfoilo

# athena query result
aws s3 mb s3://technical-portfoilo-query-result

# make sync with local path and bucket
aws s3 sync ../data/compacted.gzip s3://technical-portfoilo