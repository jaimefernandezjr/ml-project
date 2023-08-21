# ML-PROJECT
A repo made using tutorial by Krish Naik as basis in order for me to familiarize deploying ML models

## Connect to remote repo
`git clone <remote-repo>`

## Create an environment
`pipenv shell`

## Make a setup.py
- this file is responsible in building the machine learning application as a package
- add e . at the end of the requirements.txt to run the setup.py automatically

## Make a src folder with an __init__.py file
- __init__.py is a file that makes Python treat the dir, which contains '__init__.py', as a package

## Add dependencies to requirements.txt
- numpy, pandas, seaborn, matplotlib, scikit-learn, catboost, xgboost, -e .

## Install the dependencies from the requirements.txt
`pip install -r requirements.txt`
- after installing the dependencies, the setup.py will be executed, building a '.egg-info' folder that contains the packages that can be used anywhere if we deploy it in PyPi

## Push the changes in the remote repo
- `git add .`
- `git commit -m ""`
- `git push -u origin main`

## Create a 'components' folder inside src
- components folder will contain modules such as data ingestion module etc.
- add __init__.py
- add data_ingestion.py
    - data ingesion module allow us to read data from diff sources
    - divides data into train and test, as well as validation data
- add data_transformation.py
- add model_trainer.py
    - here we train the model

## Create a 'pipeline' folder inside src
- add '__init__.py'
- add 'train_pipeline.py'
    - this will have all the code for the training itself
    - triggers the modules in the 'components' dir
- add 'predict_pipeline.py'

## Create 'logger.py' inside src
- here we log all of the information per execution for easy tracking and debugging
## Create 'exception.py' inside src
- here we write our own exceptions

## Create 'utils.py' inside src

## Try running 'logger.py'
- `python src/logger.py`
    - this will create a logs folder that will log all the execution

## Create 'notebook' dir
- this will contain the dataset, eda and model training jupyter notebooks
- add 'data' dir
    - add stud.csv
- add 'EDA STUDENT PERFORMANCE.ipynb'
- add 'MODEL TRAINING.ipynb'

## Complete the 'data_ingestion.py' file
