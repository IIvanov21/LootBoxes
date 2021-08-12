# LootBoxes


## Contents
* [Introduction](#introduction)
    * [Objective](#objective)
    * [Proposal](#proposal)
* [Architecture](#architecture)
    * [Risk Assessment](#risk-assessment)
    * [Kanban Board](#trello-board)
    * [Test Analysis](#analysis-of-testing)
* [Infrastructure](#infrastructure)
    * [Jenkins](#jenkins) 
    * [Entity Relationship Diagram](#entity-relationship-diagram)
    * [Interaction Diagram](#interaction-diagram)
    * [Services](#services)
* [Development](#development)
    * [Front-End Design](#front-end-design)
    * [Unit Testing](#unit-testing) 
* [Footer](#footer)

## Introduction 
### Objective
The idea is to develop an application with service oriented architecture. The requirements state there should be at least 4 services.
  * Service 1(Front-End): The core service which will render the application and create the communication between the other 3 back-end services.
  * Service 2&3(Back-End): These will both generate a random "Object" each based on personal choice as a developer.
  * Service 4(Back-End): This will create an object that is based on the objects created from service 2 and 3 using pre-defined rules.
 The project needs to utilise these technologies:
  * Kanban Board: Asana or an equivalent Kanban Board
  * Version Control: Git
  * CI Server: Jenkins
  * Configuration Management: Ansible
  * Cloud server: GCP virtual machines
  * Containerisation: Docker
  * Orchestration Tool: Docker Swarm
  * Reverse Proxy: NGINX
 The final delivery of the project is a completed CI Pipeline with full documentation around the utilisation of supporting tools. The CI Pipeline needs to be able to successfully deploy the application you have created.
 ### Proposal
 The importance of the project is the CI Pipeline being able to implement and utilise each section as mentioned above with the constraints. Therefore the application itself is   fairly simple in comparison. The idea is to generate a Weapon LootBox and it will drop a weapon with a skin.
 
 #### Weapon LootBox Generator
 * Service 1(Front-End): will display the contents of the loot drop generated by the 3 services. This service will also include limited history of previous loots drops.
 * Service 2(Back-End): Returns a random weapon from a list.  
 * Service 3(Back-End): Returns a random skin for the weapon including stats for the skins such as condition, rarity and name.
 * Service 4(Back-End): Returns a Weapon combined with a skin and stats for rarity based on the skin condition, name and rarirty. 
 
## Architecture
### Risk Assessment
Risk Assement table analyses the possible risks I could encounter during the development and management of the project.
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/risk assesment.png" alt="Risk Assesment" />
All the highlighted rows were added later on during the development process after they became clear. The yellow risks are potential threat depending on how the development of the project is handled.
### Trello Board
The progress of the project is documented using Trello as it is well suited for a small scale project. The initials setup of the board looks as follows:
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/KanBanBoard.jpg" alt="KanBanBoard" />
The full access to the board is here:https://trello.com/b/3Z7wkgZu/lootboxes
The updated Trello Board:
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/KanBanBoard2.jpg" alt="KanBanBoard2" />
View the original board here: https://trello.com/b/3Z7wkgZu/lootboxes
### Analysis of Testing
To understand what testing strategy I need the first thing I needed to do is investigate different types of testing. There are multiple forms of testing which can be implemented but I need to target tests which are in the scope of the project. These forms of testing mentioned bellow allow me to summarise different types together which can be followed sequientially and allow full testing for any size project.
   * Unit testing - A way of testing the smallest piece of code that can be logically isolated in a system.
   * Integration testing - individual software modules combined and tested as a group.
   * API testing - testers validate that API connections and responses function as intended.
   * UI testing - testing of UI controls like buttons, menus and text input to ensure that the experience flow and features chosen are optimal for the user experience.
   * System testing - validate the complete and integrated software package to make sure it meets requirements.
   * White-box testing - tests several aspects of the software, such as predefined inputs and expected outputs, as well as decision branches, loops and statements in the code.
   * Black-box testing - testing against a system where the internal code, paths and infrastructure are not visible.
   * Acceptance testing - ensure that the end user can achieve the goals set in the business requirements.
   * Alpha testing - uses internal team members to evaluate the product.
   * Beta testing - a soft launch, enabling you to get feedback from real users who have no prior knowledge of the app.
   * Production testing - attempts to discover and triage user-reported defects as quickly as possible.
The table below outlines the test I will consider during the MoSCoW priority to ensure I have sufficient testing that allows to test all my code in the limited development time I have.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/Testing.png" alt="Testing" />
<br>
Given the results after gathering all the essential testing types only unit testing is essential to meet the requirements for the project. The other types of testing under Should Haves, Could Haves and Would Haves can ensure better and more robust functionality of the app but as time is critical they will only be considered at the end of the development cycle. 
After gathering ideas for testing I designed a chart which showcases all the unit-testing performed during the development process of the app. The test are presented as pseudo-code to ensure I can follow them more closely while implementing them. The chart also showcase which type of tests have been completed and have passed while testing.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/UnitTesting.png" alt="UnitTesting" />
<br>

## Infrastructure
Continous Deployment is integrated in my project through the use of Jenkins. This allows automated testing to be performed to validate changes in the codebase and ensure they are stable for deployment. Once all tests pass Jenkins continous immediate autonomous deployment to the production environment. This allows me to fully implement new features with limited down-time and upon failure prevent deployment of the broken changes. So how does Jenkins work? 
All the code for the pipeline can be found in the Jenkinsfile.
### Jenkins
When new content gets pushed on the .dev branch, Github will send a notification to Jenkins through a webhook which tells it to run the following pipeline:
#### 1. Setup
Jenkins installs all the dependecies needed to run the development environment on the VM it uses. This means dependecies such as docker, ansible, python and ensures all packages are up to date on the VM.
#### 2. Test: pytest
Unit tests outlined above are run everytime a new change is pushed. A coverage report is produced which can be viewed in the console output or .xml files which are used display the results with the help of Cobertura and JUnit plugins in Jenkins.
#### 3. Building && Pushing
Jenkins credential system is used to store login details for the Docker Hub and Databse. These credentials are used to login in DockerHub and with the help of docker-compose new images get built and pushed to the docker repository.
#### 4. Ansible
Ansible is used to handle several things for the load balancer, swarm manager and workers:
   * Copy the relavent .ssh key to each VM.
   * Install dependecies(docker,docker-compose and nginx)
   * Setting up the swarm(Initialise manager and join workers)
   * Setup/Reload NGINX with the nginx.conf file.
#### 5. Deploy
Jenkins simply compies accross the docker-compose.yaml in the swarm-manager node, SSH's into it to gain access and the runs docker stack deploy which creates all the relavent services needed.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/CDPipeline.png" alt="CDPipeline" />
<br>
### Entity Diagram
The project utilises a single Entity Relationship Diagram with only one table. The table essentially describes the delivered information to the end user. Also describing the elements in the table will allow me as a developer to confirm the type of validation I need to take in account when implementing a feature and performing testing.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/Database.png" alt="Database" />
<br>

### Interaction Diagram
The layout of the virtual machines is configured with Docker Swarm to utilise a manager with workers, additionally on top of that there is another layer created with NGINX which handles all the connections from users and balances them equally between the manager and workers.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/LoadBalancer.png" alt="LoadBalancer" />
<br>
In this diagram DockerSwarm creates a network of virtual machines that are all able to communicate between each other to provide the same service and allow users to access them. The layer that sits on top is another virtual machine which connects to all VMs created by DockerSwarm and creates a reverse-proxy to distribute traffic between VMs equally. Essentially this VM has NGINX load-balancer service running on it which directs connecting users to VM with the least connections. This extra layer also prevents the user to connect dirrectly to Swarm Manager or Worker which further increases security of the app. Also introduces further stability if one of the swarm VM dies it will automatically redirect the user to a working VM.
### Services
The services essentially connect between each through GET and POST request to provide the front-end application with the desired information based on the set requirements. The front-end service will store and get information from the Database. I essentially wasn't able to create a secure connection between the Database and for majority of development looked like this: 
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/ServicesOld.png" alt="ServicesOld" />
<br>
But realising to meet the MVP I needed a working database. Once I was able to get the database working properly I adjusted the diagram:
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/Services.png" alt="Services" />
<br>
In short for this application the front-end(service 1) will connect to the back-end services(service 2 and 3) through a GET request to gather the desired information. After that front-end service sends the responses received to back-end service 4 through a POST request to be combined and then send its response back. Now that all the information is gathered from the back-end services FRONT-END API will connect to MYSQL instance to store the information through INSERT, and then SELECT the old entries in order to be displayed as history.  

### Refactoring
The target of refactoring here is essentially to make easier the deployment process for the developer to create new swarm-workers. To create a new swarm worker the developer has to go through the hassle of adding the SSH keys every time in the new workers. In short he has to perform the following steps:
* Create new swarm-worker manually.
* Get the ssh public key from the Jenkins VM.
* Add it in the configuration settings of the new worker VM and test if the conncetion works.
To depreciate some of the steps above I have created an extra roles in Ansible. This role automatically targets the SSH key on the Jenkins VM and copies it over to the swarm worker. This feature allows to avoid the human-error of accidently copying the wrong ssh keys and lowers the chance of encoutering errors during the Configuration Stage of the pipeline.
In case of the Jenkins VM getting corrupted I have created extra scripts for setting up Jenkins, Ansible, docker and docker compose. This essentially creates safeguards in place which quickly allow the developer to deploy new Jenkins VM. In addition if there is need to generate new SSH keys due to losing the old ones. The developer can simply copy accross the new keys to each swarm manager and worker with the Ansible role mentioned above.
