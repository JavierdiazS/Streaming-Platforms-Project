Scalable ETL Pipeline with MySQL, FastAPI, and Docker for Multimedia Streaming Data
==============================

<p align="center">
    <img src="https://i.pinimg.com/originals/8b/d1/f6/8bd1f6a1422ab4c90063a322debbca29.jpg" width="242" style="display:inline-block;">
    <img src="https://user-images.githubusercontent.com/109487557/206548137-d8c71b68-61e7-4c41-a6e1-131935d0c0f6.png" width="480" style="display:inline-block;">
</p>

Development of a scalable ETL pipeline using MySQL, FastAPI, and Docker to process, store, and expose data from streaming platforms like Netflix, Disney+, Amazon Prime, and Hulu. This project optimizes the data flow, enabling efficient queries and providing dynamic endpoints for real-time analysis.

## Table of Contents

- [Executive Summary](#id1)
- [Project Organization](#id2)
- [Installation Guide](#id3)
- [References](#referencias)
- [License](#licencia)

## Executive Summary<a name="id1"></a>

This project focuses on building a robust and scalable ETL pipeline, designed to integrate and process data from multiple streaming services. By using Docker for containerization, MySQL as the relational database, and FastAPI for creating endpoints, it ensures an efficient data flow from ingestion to exposure. The goal is not only to store and organize the data but also to provide a flexible solution for real-time analysis and queries, adapting to the needs of a production environment.

### Project Stages

* **Environment Setup with Conda:** Configuring a Conda environment to isolate dependencies and avoid conflicts between libraries. 
* **ETL Process Development:** Implementing the data transformation and cleaning process. Using SQLAlchemy to connect to a MySQL database and manage interactions with the tables.
* **REST API Creation:** Developing endpoints to query and manipulate the processed data.
* **Docker Containerization:** Creating a Docker image that encapsulates the FastAPI application, ensuring it can be consistently deployed in any environment.

### Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Static Badge](https://img.shields.io/badge/Docker-brightgreen?style=for-the-badge&logo=docker&logoColor=white&color=blue)


### Keywords

Pipeline, ETL, SQLAlchemy, FastAPI, Docker, Data Engineer.

## Project Organization<a name="id2"></a>

    ├── data
    │   └── raw                   <- The original and immutable data.
    │
    ├── notebooks                 <- Jupyter notebook with the code.
    │   └── ETL.ipynb             <- ETL files.
    │
    ├── src                       <- Project code.
    │   ├── Api                   
    │   │   ├── app               <- Contains the FastAPI application code.
    │   │   │   ├── config         
    │   │   │   │   └── db.py     <- Configure the connection to the MySQL database using SQLAlchemy.
    │   │   │   ├── model        
    │   │   │   │   └── user.py   <- Define the tables in the database using SQLAlchemy.
    │   │   │   ├── router        
    │   │   │   │   └── router.py <- Define API endpoints using FastAPI.
    │   │   │   └── main.py       <- FastAPI main file.
    │   │   ├── dockerfile        <- Defines the environment in which the FastAPI application will run.
    │   │   └── requirements.txt  <- Lists the Python dependencies required to run the FastAPI application.
    │   │                            
    │   └── DataBase              
    │       ├── querys.sql        <- Database Queries (As a test).
    │       └── stream_db.sql     <- Database Creation.
    │
    ├── .gitignore                <- File to specify which files or directories should be ignored by Git and not tracked.
    │                                
    │ 
    ├── environment.yml           <- The requirements file to reproduce the analysis environment.
    │
    ├── LICENSE
    │ 
    └── README.md                 <- README for developers using this project.

## Installation Guide<a name="id3"></a>

1. Clone the Repository
    
        git clone https://github.com/JavierdiazS/Streaming-Platforms-Project.git
        cd Streaming-Platforms-Project

2. Create and Activate a Conda Environment
    
        conda env create -f environment.yml
        conda activate your_env

3. Create the database and tables with 'stream_db.sql'

4. Run the ETL Process and connect to the database in the Notebook 'ETL.ipynb'

5. Create the Docker Image for the API

        cd ./src/Api
        docker build -t etlimg .

6. Run the FastAPI Docker Container

        docker run -d --name etlcontainer -p 80:80 etlimg

7. Enter localhost to test endpoints

        http://localhost/docs#/

## References<a name="referencias"></a>

Bansal, S. (2021, November). Disney+ Movies and TV Shows, Version 2. Retrieved August 10, 2024 from https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows.

Bansal, S. (2021, November). Amazon Prime Movies and TV Shows, Version 1. Retrieved August 10, 2024 from https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows.

Bansal, S. (2021, November). Hulu Movies and TV Shows, Version 1. Retrieved August 10, 2024 from https://www.kaggle.com/datasets/shivamb/hulu-movies-and-tv-shows.

Bansal, S. (2021, November). Netflix Movies and TV Shows, Version 5. Retrieved August 10, 2024 from https://www.kaggle.com/datasets/shivamb/netflix-shows.

## License<a name="licencia"></a>

It's published under the MIT license. See the [LICENSE](/LICENSE) file for more details.
