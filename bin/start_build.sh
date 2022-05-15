#!/bin/bash
ids=`aws --profile for-all-codebuild-project-in-hoamon-info-AWS codebuild start-build --project-name cp-files-to-AWS-s3-bucket-www-hoamon-info | jq ".build.id"`
# aws --profile for-all-codebuild-project-in-hoamon-info-AWS codebuild batch-get-builds --ids $(sed 's/"//g' <<< $ids) | jq ".builds[].buildStatus"
