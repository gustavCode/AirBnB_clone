# 0x00. AirBnB clone

![This is source image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230212T222201Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=774e2e87d73d5367bf70e70da85fc30a02177b64e72a806b94933fd2e82c4cbc)

## Project Definition
This is the first step towards building your first full web application: the AirBnB clone. Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Command Interpreter

we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## How to start

To start your command interpreter

- Open the terminal and navigate to the project
- type ./console and you should see this prompt
	(hbnb) 

## How to use it

To use the command interpreter you can start by typing `help`.
It returns a list of documented commands. Now to see what
every command does type `help <command>`
Note: replace <command> with any commands provided

## Examples
- help quit
- create BaseModel
- show BaseModel <id>
- all BaseModel
- destroy BaseModel <id>
