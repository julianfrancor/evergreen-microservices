# EverGreen Platform Management Project

## Introduction

This project focuses on developing an application for managing the EverGreen company's platform. EverGreen specializes in managing AgroChains through advanced technologies such as IoT, Artificial Intelligence, Drones, and Sensors.

## Domain-Driven Design (DDD)

In this project, we apply the Domain-Driven Design (DDD) approach to structure the system's architecture. DDD focuses on understanding and solving complex business domain problems, allowing us to make informed design decisions and create software that effectively aligns with the company's objectives.

## Microservices

The architecture of this project is based on the microservices paradigm. Each component, such as the user service, roles, and modules, is implemented as an independent microservice. This promotes modularity, scalability, and enables agile development and deployment.

## Architecture

![Implementación Microservicios EverGreen-Arquitectura ADM](https://github.com/julianfrancor/evergreen-microservices/assets/53787841/728473b6-175d-4b2d-b8f7-0c67ccf7f4da)

## Team

- Julian Franco
- Victor Muñoz
- David Roldán

## Course: Advanced Software Architectures

This project is developed as part of the "Advanced Software Architectures" course. The aim is to acquire the necessary tools and knowledge to design and develop high-complexity software systems.

## Domain Entities

We have identified three key domain entities for this project:

1. **User:** Represents the users who interact with the EverGreen platform. Each user has roles and can access different modules.

2. **Module:** Refers to the specific functionalities and features that make up the platform. Each module has different associated access permissions.

3. **Role:** Defines the user roles or profiles, determining what actions they can perform and which modules they have access to.

These entities form the basis of the business logic and guide the structure and functionalities of our application.

## Running the Project

To run the EverGreen Platform Management Project, follow these steps:

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager)

### Setting Up the Backend

1. Navigate to the project's root directory in your terminal.

2. Create a virtual environment (optional but recommended):

  ```
  python -m venv venv
  ```
3. Activate the virtual environment (On macOS and Linux):

  ```
  source venv/bin/activate
  ```
4. Install the project dependencies using pip:
  
  ```
  pip install -r requirements.txt
  ```
5. Running the Backend

  ```
  uvicorn main:app --reload
  ```
6. Accessing the Project
  You can access the project's API by opening a web browser or using API testing tools like Postman or curl. The API endpoints and documentation can be found at http://127.0.0.1:8000/docs for interactive documentation.

7. Stopping the Server
  To stop the server, press CTRL+C in the terminal where the server is running.

---

*Note: This README provides an overview of the project and its main aspects. As the project evolves, more details and additional documentation will be added as needed.*
