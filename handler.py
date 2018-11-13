import boto3


def handler(event, context):
    client = boto3.client('ecs')
    response = client.run_task(
        cluster='my-luster',  # name of the cluster
        launchType='FARGATE',
        taskDefinition='my-task:1',  # replace with your task definition name and revision
        count=1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-fe******',  # replace with your public subnet or a private with NAT
                    'subnet-c3******',  # Second is optional, but good idea to have two
                    'subnet-f8******'   # Third is optional too
                ],
                'securityGroups': [
                    'sg-0522d37**********'
                ],
                'assignPublicIp': 'ENABLE'
            }
        }
    )

    return str(response)
