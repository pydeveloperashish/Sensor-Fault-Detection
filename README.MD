### Problem Statement

The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 

In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

## Tech Stack Used

1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?

Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections

![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)

## Project Archietecture

![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)

## Deployment Archietecture

![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)

### Step 1: Clone the repository

```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable

```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```

### Step 5 - Run the application server

```bash
python app.py
```

### Step 6. Train application

```bash
http://localhost:8080/train

```

### Step 7. Prediction application

```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build -t sensor . 

```

3. Run the Docker image

```
docker run -d -e AWS_ACCESS_KEY_ID="${{ secrets.AWS_ACCESS_KEY_ID }}" -e AWS_SECRET_ACCESS_KEY="${{ secrets.AWS_SECRET_ACCESS_KEY }}" -e AWS_DEFAULT_REGION="${{ secrets.AWS_DEFAULT_REGION }}" -e MONGODB_URL="${{ secrets.MONGODB_URL }}" -p 8080:8080 sensor
```



![Screenshot from 2022-11-25 18-43-41](https://user-images.githubusercontent.com/59412013/203995120-6cffc710-f6d9-4ae0-b300-46a250376c45.png)
![Screenshot from 2022-11-25 18-50-29](https://user-images.githubusercontent.com/59412013/203995123-98f638ae-5bdb-4166-884e-81f74dc08ef1.png)
![Screenshot from 2022-11-25 18-48-00](https://user-images.githubusercontent.com/59412013/203995128-6e85b1a0-1684-4582-8b6a-6c22932674bc.png)
![Screenshot from 2022-11-25 18-47-54](https://user-images.githubusercontent.com/59412013/203995130-e54bf9f7-248a-4845-911c-5eeac97541d2.png)
![Screenshot from 2022-11-25 18-45-52](https://user-images.githubusercontent.com/59412013/203995133-b2bc60c8-dcf5-4ba2-a3d3-50224d667636.png)
![Screenshot from 2022-11-25 18-45-31](https://user-images.githubusercontent.com/59412013/203995134-d7c66826-5553-4fd3-b898-40cab15e154e.png)
![Screenshot from 2022-11-25 18-45-27](https://user-images.githubusercontent.com/59412013/203995137-f541e710-0840-44d3-af9a-e256f5b2181b.png)
![Screenshot from 2022-11-25 18-45-17](https://user-images.githubusercontent.com/59412013/203995139-ab931d2a-82c2-45e5-9d57-7f509a8bb300.png)
![Screenshot from 2022-11-25 18-44-43](https://user-images.githubusercontent.com/59412013/203995143-c85f1a75-6a1f-457e-a53d-db30c017fcfc.png)
![Screenshot from 2022-11-25 18-44-30](https://user-images.githubusercontent.com/59412013/203995147-4cb08a13-6298-47a4-a321-f13b56997e0f.png)
![Screenshot from 2022-11-25 18-44-21](https://user-images.githubusercontent.com/59412013/203995151-413ec0c8-2056-403e-9554-4ba460b042f6.png)
![Screenshot from 2022-11-25 18-43-55](https://user-images.githubusercontent.com/59412013/203995152-9b69c7fa-9f44-40b4-be71-8d1214110208.png)
