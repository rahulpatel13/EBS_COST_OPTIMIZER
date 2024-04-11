import boto3

def lambda_handler(event, context):
   
    ec2 = boto3.client('ec2')
    
    response = ec2.describe_snapshots(OwnerIds=['self'])
    
    instances_status = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()
    
    for reservation  in instances_status['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
     
    
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        

        if not volume_id:
            print('Do Not get the volume')
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f'Deleted EBS Snapshot {snapshot_id} as it is not attached any volumes')
            
        else : 
            
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f'Deleted EBS Snapshot {snapshot_id} as it is attached to the volume {volume_id} but EC2 is not running')

            except ec2.exceptions.ClientError as e:    
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f'Deleted EBS Snapshot {snapshot_id} as its associated volume did not found')