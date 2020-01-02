import boto3
def lambda_handler(event, context):
    region = event.get('region')
    instances = event.get('instances')
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print ' started your instances: ' + str(instances)