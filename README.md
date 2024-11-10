# int6_miniproject10
[![CI](https://github.com/nogibjj/int6_miniproject10/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/int6_miniproject10/actions/workflows/ci.yml)

### File Structure
```
int6_miniproject10
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/ci.yml
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── data
│   └── Nutrition.csv
├── main.py
├── mylib
│   ├── __init__.py
│   ├── __pycache__
│   └── lib.py
├── requirements.txt
├── nutrition_analysis.md
├── spark-warehouse
└── test_main.py
```
This repo contains work for mini-project 10. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make test`, `make format`, `make lint`. The dataset was sourced from the [fivethirtyeight github](https://github.com/fivethirtyeight/data/blob/master/nutrition-studies/raw_anonymized_data.csv) and details individuals' health and nutrition information.

Some important components:

* `Makefile`

* `Dockerfile`

* A base set of libraries for devops and web

* `githubactions` 

## Purpose of project
The purpose of this project is to use PySpark to perform data processing on a large dataset while demonstrating querying and data transformation techniques.
## Important Functions in lib.py
* `extract()`: extracts data from github URL, processes it, and saves it as a CSV under the data folder
* `load_data()`: loads the CSV into a PySpark dataframe
* `transform_data()`: counts total healthy vs unhealthy food consumption and summarizes health condition to return a new summarized dataframe
* `query()`: returns a PySpark dataframe based on a given query

These functions are tested in test_main.py. To make sure github actions is working properly, I use a Makefile to test various parts of my code. 

## Preparation
1. Open codespaces 
2. Wait for container to be built and virtual environment to be activated with requirements.txt installed 

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test code `make test`

<img width="600" alt="passing test cases image" src=pass_test.png>


## Outputs
Query outputs can be seen in `nutrition_analysis.md`. Visit [HERE](nutrition_analysis.md).