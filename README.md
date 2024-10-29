# Wine-Quality-Prediction-using-MLfLow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/bijaycd/Wine-Quality-Prediction-using-MLfLow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python==3.10 -y
```

```bash
conda activate venv/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


Run this to export as env variables:

```bash

import dagshub
dagshub.init(repo_owner='bijaycd', repo_name='Wine-Quality-Prediction-using-MLfLow', mlflow=True)

```


# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

Save the Azure password in notepad


## Run from terminal:

docker build -t mlfow.azurecr.io/winequality:latest .

docker login mlfow.azurecr.io

docker push mlfow.azurecr.io/winequality:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 



## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model