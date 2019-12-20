import boto3
import json

# Boto clients
ec2 = boto3.client('ec2')

# Get all instances in a running state
instances = ec2.describe_instance_status(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running'
            ]
        }
    ],
    DryRun=False
)

result = []
for instance in instances['InstanceStatuses']:
    result.append(instance['InstanceId'])

# Stop all instances in a running state
stop = ec2.stop_instances(
    InstanceIds=result,
    Hibernate=False,
    DryRun=False,
    Force=False
)
