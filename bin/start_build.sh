#!/bin/bash
aws --profile for-all-codebuild-project-in-hoamon-info-AWS codebuild start-build --project-name cp-files-to-AWS-s3-bucket-www-hoamon-info
