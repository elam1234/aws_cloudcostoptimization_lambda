"  CLOUD COST OPTIMIZATION PROJECT IN AWS  "

USING AWS SERVERLESS LAMBDA FUNCTION TO FIND STALE RESOURCES AND DELETE THOSE RESOURCES TO OPTIMISE THE CLOUD COST EFFICIENTLY

INTRODUCTION :
Hello everyone, I Elamparithi M, am a DevOps engineer, I am very passionate about doing innovative projects in DevOps and the cloud. I have done a very essential project in the public cloud world, do think why people move on to the cloud?  they have two primary reasons, those would eliminate the management overhead, and cost-effectiveness as well, if they don't use resources efficiently, in this case, the solution of cloud computing is not worth to them, so we have to efficiently manage our resources in the cloud, in this, my project demonstrates how I was following the approach to optimizing the cost in AWS.

PROJECT EXPLANATION :
The project involved leveraging AWS Lambda's serverless architecture and event-driven nature to automate the identification and removal of stale resources. By utilizing Python scripts with Boto3, Lambda functions were developed to perform the necessary checks and actions. Key components of the project included enhancing Lambda role's execution permissions, extending Lambda's execution time, and setting up event triggers through AWS CloudWatch.

PROJECT HIGH-LEVEL STEPS :
Creation of Lambda Function: Develop Lambda functions using Python and Boto3 to identify stale resources.
Grant EC2 and Snapshot IAM Role Permissions to Lambda: Ensure Lambda has the necessary permissions for EC2 and snapshot interactions.
Writing Python Code Using Boto3: Write scripts to interact with AWS services for identifying and removing stale resources.
Extending Lambda Execution Timing: Increase Lambda's execution time to handle longer processing tasks.
Integration of Lambda with AWS CloudWatch to Trigger: Set up CloudWatch events to trigger Lambda functions at specified intervals for continuous monitoring.
Testing: Simulate stale resources by creating EC2 instances with attached volumes, then verify Lambda's automatic detection and deletion of associated snapshots.

PROBLEM I FACED :
IAM Permission Configuration:
Description: Configure IAM permissions for Lambda to access EC2 instances and snapshots securely.
Solution: Review IAM policies and roles, and test permissions to ensure necessary access without compromising security.
Lambda Execution Timing:
Description: Lambda functions timeout before completing resource tasks due to insufficient execution time.
Solution: Extend Lambda function timeout duration to allow effective execution of resource management tasks.
GITHUB LINK:  https://github.com/elam1234/aws_cloudcostoptimization_lambda.git

CONCLUSION :
After completing this project, I learned lambda from a DevOps engineer point of view, lambda is a pivotal service for doing cloud cost management efficiently, and now I feel proficient in Python boto3(aws sdk ) through this project I was explaining my approach for stale resource deletion using lambda if you want to know more details about this project please go through my LinkedIn post  : https://www.linkedin.com/posts/elamparithi-m-72288625a_cloudcostoptimization-awslambda-boto3-activity-7171463731753762816-ONWf?utm_source=share&utm_medium=member_desktop

