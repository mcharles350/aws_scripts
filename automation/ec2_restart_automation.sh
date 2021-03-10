#!/bin/bash

echo 'Enter instance name: '
read instanceName

instanceId=$(aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=${instanceName}" \
    --query 'Reservations[*].Instances[*].{}\
    --output text) 

echo $instanceName' will begin restarting'

# Run automation task
aws ssm start-automation-execution \
    --document-name "AWS-RestartEC2Instance" \
    --parameters "InstanceId=${instanceId}"

# Status check
if 

fi