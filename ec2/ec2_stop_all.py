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

for i in instances['InstanceStatuses']:
    print('Instance Id: ' + i['InstanceId'] + ' is located in ' + i['AvailabilityZone'] + ' and it\'s currently ' + i['InstanceState'].get('Name') + '.')

    if i['InstanceState'].get('Name') == 'running' == 'running':
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

        print('All instances listed has been stopped.')
else:
    print('No instances to stop at this time.')
