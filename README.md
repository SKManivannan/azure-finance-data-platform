# Azure Databricks + Airflow Lakehouse Project

## Overview
This project demonstrates a **production-grade Azure Lakehouse architecture** using **Azure Databricks**, **Apache Airflow**, and **Delta Lake**.  
It supports **DEV & PROD environments** with fully automated **CI/CD pipelines**.

## Architecture
- Bronze → Silver → Gold (Medallion Architecture)
- Apache Airflow for orchestration
- Databricks job clusters for processing
- ADLS Gen2 for storage

## Key Features
- Scalable Spark-based transformations
- ACID-compliant Delta Lake tables
- Automated CI/CD deployments
- Cost-optimized job clusters
- Fault-tolerant orchestration

## Tech Stack
- Azure Databricks
- Apache Airflow
- Azure Data Lake Storage Gen2
- Delta Lake
- GitHub Actions / Azure DevOps

## Environments
- DEV: Testing & validation
- PROD: Production-scale processing

## How It Works
1. Raw data ingested into Bronze layer
2. Data cleaned and validated in Silver layer
3. Aggregated data published to Gold layer
4. Airflow orchestrates all jobs
5. CI/CD automates deployments

## Status
✅ DEV completed  
✅ PROD completed  
✅ CI/CD green  

## Author
Built as a hands-on production-style Data Engineering project.

## Document
📘 Detailed project documentation available in `/docs/Azure_Lakehouse_Project_Documentation.docx`

