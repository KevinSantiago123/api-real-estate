# Api Real Estate.

This microservice allows you to list the real estate of the company.

### Features.

- Users can consult the properties with the states: "pre_sale", "for_sale" and "sold".
- Users can filter these properties by: Year Built, City, State.
- Users can apply multiple filters on the same query.
- Users can see the following property information: Address, City, State, Sale Price and Description.

### Dependencies.

- Python 3.
- Install libraries from the requirements.txt file.
- virtual environment to run locally.
- database MySql.

### Installation.

###### Paso1. Clone the project https://github.com/KevinSantiago123/api-real-estate.git from git bash
###### Paso2. Create a virtual environment, activate it, and install the dependencies from the requirements.txt file
###### Paso3. Add file sent by mail '.env' in the root of the project and if necessary modify credentials
###### Paso4. Run *run.bat* located in the root of the project if the operating system is windows

Note: In case the operating system is Ios or Linux, configure the file in the **/server/envs.py** path by uncommenting the global variables used for those operating systems and commenting out the global variables for Windows. After executing run.sh that is in the root of the project.

### Implementation

I am going to approach the test starting by analyzing the tables already created in the database and their records, then investigate how to create the microservice without using a framework.

Start with the configuration of the web server, develop the queries in the workbench, develop the service that allows you to first list all the real estate, then make the filters, improve the quality standards a bit, code the tests and test. Correct if necessary.

## 11.Extend the model for Likes functionality.

#### See image by clicking on the link below
https://unilibrebog-my.sharepoint.com/:i:/g/personal/kevins-castanedat_unilibre_edu_co/Eal-ztnhCghKoj3PuYsmbekBNN9d2qDdGS57_S_3K3SvhA?e=nFnxB3

3 new entities are proposed:
- Users, which helps us store the information of new users of the platform.
- Like_History, registers the id of the property and the id of the users with which we can identify the history of likes of the users to the specific property.
- Cities, it is important to identify users interested in selling and buying where they live in order to analyze where I find potential Habi customers.
Now it is proposed to modify the property entity to add the city id, which gives us a standardization of the city and to be able to analyze the potential clients that live in a certain place and are interested in finding a certain destination.

## Bonus point 2. Improvements in the model

#### See image by clicking on the link below
https://unilibrebog-my.sharepoint.com/:i:/g/personal/kevins-castanedat_unilibre_edu_co/EcojsB-6GHtNo50DdwaAkrMBOLZniTeZswceN7O9ZR9Iag?e=sQN9lX

Future improvements focused on the science of where are proposed to answer future business questions such as where are my customers, what could be a new city to enter, number of rural and urban properties in different countries. All these questions and others could be answered with the proposed new entities, accompanied by new microservices and new front-end templates.

As for improving speed with the current proposal, I think it is acceptable.
