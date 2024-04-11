
# EBS Snapshot Cost Optimizer

Taking snapshots of your instance or EBS is crucial for managing important data effectively.

AWS snapshots offer several benefits like data backup, disaster recovery, and simplifying data management tasks.

They provide a way to create point-in-time copies of your volumes or instances, allowing you to easily revert to previous states when needed, which minimizes downtime and facilitates tasks like data migration and testing.

However, it's essential to be mindful of costs, as having too many snapshots can lead to unexpected expenses. 
To avoid this, it's helpful to automate the process of identifying snapshots that are not actively in use or are redundant. This can help in optimizing costs and staying within budget while still ensuring that necessary backups are in place.


## AWS Service and Tech Used

Terraform \
Ec2 Instances and Snapshots\
EventBridge - Rate Scheduler\
IAM Policy and Roles
## Steps to perform
1. Clone this repo.
2. Make sure you have AWS account and terraform installed. 
3. I have not provided credentials in this , you can use aws configure command or give a credentials file in terraform to configure/connect aws account.
4. Make sure you have a S3 bucket in your account , configure backend.tf accordingly.
4. After everything is setup, run the following commands
```bash
1. terraform init
2. terraform plan
3.terraform apply
//If you want to delete your infra
4. terraform destroy 
```

## Architecture

![App Screenshot](https://github.com/rahulpatel13/EBS_COST_OPTIMIZER/blob/main/cost_optimizer.png)

