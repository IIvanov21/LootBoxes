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
    * [Docker Swarm](#docker-swarm)
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
## Infrastructure

### Entity Diagram
The project utilises a single Entity Relationship Diagram with only one table. The table essentially describes the delivered information to the end user. Also describing the elements in the table will allow me as a developer to confirm the type of validation I need to take in account when implementing a feature and performing testing.
<br>
<img src="https://github.com/IIvanov21/LootBoxes/blob/main/images/Database.png" alt="Database" />
<br>
