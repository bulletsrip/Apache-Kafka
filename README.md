# Twitter Tweet Streaming - Confluent Kafka
![image](https://user-images.githubusercontent.com/85284506/207529566-ef7fb9d0-6c1a-49a2-a0b2-777a2229a92e.png)

Ingest data from Twitter API data source and publish it to a Kafka topic for consumer application to subscribe and consume messages.

## Install Confluent Kafka
Using Docker compose, we can install the entire Confluent Platform or individual components.

+ Docker version 1.11 or later is installed and running.
+ Docker Compose is installed. Docker Compose is installed by default with Docker for Mac.
+ Docker memory is allocated minimally at 8 GB. When using Docker Desktop for Mac, the default Docker memory allocation is 2 GB. You can change the default allocation to 8 GB in Docker > Preferences > Advanced.

### Run Docker Compose 
```docker
docker-compose up
```
    
### Confluent Control Center    
Confluent Control Center is a web-based tool for managing and monitoring Apache Kafka®

    Go to http://localhost:9021/ which is the default port that the Webserver will be listening to.

![image](https://user-images.githubusercontent.com/85284506/207524846-179475b7-8bf8-406a-b6ba-4523c5d88304.png)

Confluent Control Center is a web-based user interface that allows developers and operators to manage and monitor Apache Kafka clusters, including checking cluster health, observing and controlling messages, topics, and Schema Registry. It can also be used to develop and run ksqlDB queries.

 + Broker
 + Topics
 + Connect
 + KSQL
 + Consumer
 + Replicator
 + Cluster Settings

## Twitter API
First, we need to create user credentials to use Twitter API. Sign up for a developer account at Twitter Developer Portal. Sign in to developer console. Give a name to your app. We will use bearer token for credentials.

### Create App
- Go to `https://developer.twitter.com/apps`
- Create app - fill up the form
- Change the permission if neccessary (depending if you want to just read / write / execute)

### Generate Key
![image](https://user-images.githubusercontent.com/85284506/207528533-1c528b13-aa07-4a25-af0f-218a6f1d1e73.png)
![image](https://user-images.githubusercontent.com/85284506/207528573-2e9f6fb3-46ae-435c-b1aa-0624c66406a4.png)


## Python Code

### Create Python Virtual Environment
```python
python3 -m venv [env_name]
```

Activate virtual environment with command `source [env_name]/bin/activate`
    
### Install requirements dependencies on requirements.txt

```python
pip install -r requirements.txt
```

### Change .env variable

```bash
BEARER_TOKEN='Your Bearer Token'
```

### Creates a record and publishes it to the broker

```python
python[version] kafka_producer.py [word_to_track] [topic_name]
```

Example:

```python
python3 kafka_producer.py Ronaldo Football
```

### Consumes records from the topics

```python
python[version] kafka_consumer.py [topic_name]
```

Example:

```python
python3 kafka_consumer.py Football
```

![consumer producer](https://user-images.githubusercontent.com/85284506/207526966-bf0dff86-1bea-4c24-8c55-215b50504a4e.png)

