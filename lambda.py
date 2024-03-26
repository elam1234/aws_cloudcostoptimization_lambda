import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')

    # Get information about running EC2 instances
    response_instances = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])

    # Get all EBS snapshots owned by the current account
    response_snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])

    # Extract the IDs of active instances
    active_instance_ids = set()
    for reservation in response_instances['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Extract the IDs of volumes attached to active instances
    active_volume_ids = set()
    for reservation in response_instances['Reservations']:
        for instance in reservation['Instances']:
            for block_device in instance.get('BlockDeviceMappings', []):
                active_volume_ids.add(block_device['Ebs']['VolumeId'])

    # Check if there are any snapshots owned by the current account
    if 'Snapshots' in response_snapshots:
        # Iterate over each snapshot
        for snapshot in response_snapshots['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')

            print(f"Checking snapshot {snapshot_id}...")
            # Check if the snapshot is not associated with any active instance's volume
            if not volume_id or volume_id not in active_volume_ids:
                print(f"Snapshot {snapshot_id} is not associated with any active instance's volume.")
                # Delete the snapshot and print a message
                ec2_client.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id} successfully.")
            else:
                print(f"Snapshot {snapshot_id} is associated with an active instance's volume, skipping deletion.")
    else:
        print("No EBS snapshots found in your account.")
