# ADM

<strong>Advance Data Management Project

Proof of Concept for Resume Analyzer</strong> 


Our research into the technology has led us from basic hadoop mapreduce programs in java to more sophisticated implementations
of mapreduce such as MongoDB. It is one of the most popular NoSQL database available for storing unstructured data and is 
powerful enough to implement mapreduce programs on its own. It stores unstructured data in JSON/BSON (format similar to JSON)
and also provides the capability to query this data. The nature of our app which brings several applicants together with 
recruiters necessitates our application to be able to process unstructured data and be scalable, MongoDB lends itself readily
to the cause. Further research into MongoDB revealed that, its own implementation of the mapreduce algorithm can directly perform 
data transformations on the data which will help speed up the consolidation of data.

Python allows you to get to a first-draft prototype much more quickly, which is one reason why many organizations are now building
prototypes using Python .Integration of MongoDB and python can be done seamlessly using the PyMongo driver.  We have used the python
bottle web framework for developing the web application.Bottle is a fast, simple and lightweight WSGI micro web-framework for python.

<strong>Installation Instructions:</strong>

1) Install MongoDB and load data: 
Download and Install MongoDB https://www.mongodb.org/downloads#production

2)Start a MongoDB instance by starting the mongod daemon. (the data will be populated by the python script)

3)Install Python:
Download and install Python: https://www.python.org/downloads/

4)Open command prompt and execute the python file under the following path: \ADM\Resume_Parser.py
The User Interface will be launched from the default browser.

5) python libraries

pyMongo - pip install pymongo

bottle  - pip install bottle

## Team Members (alphabetical)

Atif Tahir , Abeer Katiyal , Nivedhan Manavalan , Kirthan Vasudevan

## License

    Copyright 2015 Team -  Data Aggies

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

