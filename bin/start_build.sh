#!/bin/bash
aws --profile for-all-codebuild-project-in-hoamon-info-AWS codebuild start-build --project-name cp-files-to-AWS-s3-bucket-www-hoamon-info
# aws --profile for-all-codebuild-project-in-hoamon-info-AWS codebuild batch-get-builds --ids cp-files-to-AWS-s3-bucket-www-hoamon-info:b1edbdb9-ab30-4986-8d7e-2545401a56ef
