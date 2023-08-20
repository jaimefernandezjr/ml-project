# ml-project
A repo made using tutorial by Krish Naik as basis in order for me to familiarize deploying ML models

## Connect to remote repo
`git clone <remote-repo>`

## Create an environment
`pipenv shell`

## Make a setup.py
- this file is responsible in building the machine learning application as a package
- add e . at the end of the requirements.txt to run the setup.py automatically

## Make a src folder with an __ini__.py file

## Add dependencies to requirements.txt
`numpy, pandas, seaborn, -e ., etc`

## Install the dependencies from the requirements.txt
`pip install -r requirements.txt`
- after installing the dependencies, the setup.py will be executed, building a '.egg-info' folder that contains the packages that can be used anywhere if we deploy it in PyPi

## Push the changes in the remote repo
`git add .`
`git commit -m ""`
`git push -u origin main`

