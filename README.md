<p align="center">
  <img width="461" height="340" alt="ETL Pipeline Diagram" src="https://github.com/user-attachments/assets/495d5540-5f6c-4cad-8e11-a7b3039fa0c2" />
</p>

# ETLLoadPipelineNotification

A fully automated, event-driven ETL (Extract, Transform, Load) pipeline built using core AWS services: **S3, Lambda, Glue, EventBridge, SNS, and CloudWatch**.

## 🚀 Project Overview
This repository demonstrates how to set up a **serverless ETL workflow** on AWS.  
The pipeline is triggered when data is uploaded to S3, processed with AWS Glue, and monitored through email notifications and logging.

### Automated Workflow
1. **Data Ingestion**: Upload a CSV file to the `extract/` folder in an S3 bucket.  
2. **Event Trigger**: S3 invokes a Lambda function when a CSV file is uploaded.  
3. **ETL Processing**: Lambda starts a Glue job to transform data (e.g., drop duplicates) and load it into the `load/` folder in S3.  
4. **Event Tracking**: Glue job status (success/failure) is sent to EventBridge.  
5. **Notification**: EventBridge forwards events to SNS, which emails subscribers.  
6. **Monitoring**: CloudWatch logs provide visibility for auditing and troubleshooting.  

## 🛠️ AWS Services Used
- **Amazon S3** → Source & destination for data files  
- **AWS Lambda** → Orchestrates the workflow & triggers Glue jobs  
- **AWS Glue** → ETL job execution (visual editor or Python script)  
- **Amazon EventBridge** → Tracks and routes job status events  
- **Amazon SNS** → Sends success/failure notifications via email  
- **Amazon CloudWatch** → Centralized logging and monitoring  


## 💡 Key Features
- **Event-driven automation** → Upload a file to start the pipeline  
- **Flexible ETL** → custom Python scripts  
- **Real-time alerts** → Email notifications on job completion or failure  
- **Comprehensive monitoring** → Integrated CloudWatch logs  
