# Twitter Tweet Streaming - Confluent Kafka
![image](https://user-images.githubusercontent.com/85284506/207523008-63721f3d-356a-44aa-b628-27bbc7f67c70.png)

## Install Confluent Kafka
Using Docker compose, we can install the entire Confluent Platform or individual components.

+ Docker version 1.11 or later is installed and running.
+ Docker Compose is installed. Docker Compose is installed by default with Docker for Mac.
+ Docker memory is allocated minimally at 8 GB. When using Docker Desktop for Mac, the default Docker memory allocation is 2 GB. You can change the default allocation to 8 GB in Docker > Preferences > Advanced.

### Run Docker Compose 
    `docker-compose up`
    
### Confluent Control Center    
Confluent Control Center is a web-based tool for managing and monitoring Apache Kafka®, 

Go to http://localhost:9021/ which is the default port that the Webserver will be listening to.

![image](https://user-images.githubusercontent.com/85284506/207524128-ad4f5931-6aac-4f2a-8695-5e1e848954f5.png)

Control Center facilitates building and monitoring production data pipelines and streaming applications.

## Twitter API

### Create APP

## Python

### Create Python Virtual Environment
    - Use `virtualenv <env_name>` on your working directory
    - Activate virtual environment with command `source /bin/activate`
    
### Install requirements dependencies on requirements.txt
   
    - `pip install -r requirements.txt`

### Change .env variable

    - `cp .env.example .env`

### Run kafka_producer.py 

    `python3 kafka_producer.py [word_to_track] [topic_ncame]` ex: `python3 kafka_producer.py Ronaldo Football`


### Check messages on kafka_consumer.py

    - `python kafka_consumer.py`
