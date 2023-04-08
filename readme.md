
# What is celery 📝  
Python Celery is a distributed task queue framework for Python that allows you to run asynchronous and scheduled tasks. It is often used for processing time-consuming tasks in the background of web applications or batch processing jobs. Celery allows you to execute tasks asynchronously, which means that you can initiate a task and then continue executing other code while the task runs in the background.

Celery works based on a distributed architecture that allows for the execution of tasks asynchronously. It consists of three main components: the client, the broker, and the workers.

Celery is built on a message-passing system, where tasks are sent to a queue and then executed by a worker process. This enables tasks to be distributed across multiple worker processes, or even multiple machines, allowing for high scalability and fault tolerance.

Celery supports a range of message brokers, including RabbitMQ, Redis, and Apache Kafka, allowing you to choose the messaging system that best fits your needs. It also integrates with popular Python web frameworks like Django, Flask, and Pyramid, making it easy to use in your existing applications.

## Get Started 🚀  
To get started,  setup a redis cache,celery package for Python, 
* pip install redis
* pip install celery
* Flower-additonal pakcage to see various tasks added to celery. the redis cache system also helps to perform the same function by viewing the outp data in redis DB. Flower provides a much more user firendly view

## Notes ⚠️
* There are some compatability issues in runing celery in windows.

## General Working of celery
Celery works based on a distributed architecture that allows for the execution of tasks asynchronously. It consists of three main components: the client, the broker, and the workers.

The client is responsible for initiating tasks and sending them to the message broker. The tasks can be initiated using the Celery API, which allows you to define tasks as Python functions or methods.

The broker acts as a middleman between the client and the workers. It receives tasks from the client and queues them for processing by the workers. Celery supports several message brokers such as RabbitMQ, Redis, and Apache Kafka, among others.

The workers are responsible for executing the tasks. They receive the tasks from the broker, execute them, and return the results back to the broker. Celery supports multiple worker processes running on different machines, allowing for distributed task execution.

When a task is initiated, it is serialized and sent to the broker, which queues it for processing by a worker. The worker then retrieves the task from the broker, deserializes it, and executes it. Once the task is completed, the worker sends the result back to the broker, which then sends it back to the client.

Celery also provides several tools for monitoring and managing the execution of tasks, including a web-based dashboard and a monitoring API. These tools allow you to track the progress of tasks, monitor worker performance, and manage the task queue.



