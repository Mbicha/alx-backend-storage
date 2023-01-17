# :Kenya: 0x01. NoSQL


## Resources

- NoSQL Databases Exaplained - https://riak.com/resources/nosql-databases/

- What is NoSQL? - https://www.youtube.com/watch?v=qUV2j3XBRHc&ab_channel=Guru99

- MongoDB with Python Crash Course - Tutorial for Beginners - https://www.youtube.com/watch?v=E-1xI85Zog8&ab_channel=freeCodeCamp.org

- MongoDB Tutorial 2 : Insert, Update, Remove, Query - https://www.youtube.com/watch?v=CB9G5Dvv-EE&t=4s&ab_channel=DerekBanas

- Aggregation - https://www.mongodb.com/docs/manual/aggregation/

- Introduction to MongoDB and Python - https://realpython.com/introduction-to-mongodb-and-python/

- Mongo Shell Methods - https://www.mongodb.com/docs/manual/reference/method/

## MongoDB Command File

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- Your code should not be executed when imported (by using if __name__ == "__main__":)

## Install MongoDB 4.2 in Ubuntu 18.04
- $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
- $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
- $ sudo apt-get update
- $ sudo apt-get install -y mongodb-org
- $ service mongod start/stop/restart/status

## Install pymongo
- pip3 install pymongo

## Contributing
- Charles Mbithi - ALX Student

## Versioning
For my learning of backend web dev in ALX School

## Authors

---Charles Mbithi mbithicharlse@gmail.com

## Files

| **Files**                                     | **Description** *                                             |
| --------------------------------------------- | ------------------------------------------------------------- |
|[0-list_databases](./0-list_databases)        | List all databases in MongoDB      |
|[1-use_or_create_database](./1-use_or_create_database)| Create MongoDB database    |
|[2-insert](./2-insert)| Inserts a single document into a collection in mongodb     |
|[3-all](./3-all)|List all entries in a collection.|
|[4-match](./4-match)| Find match|
|[5-count](./5-count)| Count documents|
|[6-update](./6-update)| Update matched|
|[7-delete](./7-delete)| Delete matched|
|[8-all.py](./8-all.py)| List all database|
|[9-insert_school.py](./9-insert_school.py)| Insert some values into the document.|
|[10-update_topics.py](./10-update_topics.py)| Update topics.|
