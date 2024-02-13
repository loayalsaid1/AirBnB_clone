# Airbnb Command Interpreter

## Description
The Airbnb Command Interpreter is a Python-based command-line tool designed to emulate the backend functionality of the Airbnb project. It allows users to interact with and manage various objects such as users, places, bookings, and reviews through a simple command-line interface.

## Command Interpreter
The command interpreter provides a set of commands to interact with the system. These commands include creating, showing, updating, and deleting objects, as well as retrieving information about objects and performing various operations.

### Starting the Command Interpreter
1. Run the `python console.py` script using Python 3.

Example:
### Using the Command Interpreter
Once the command interpreter is running, you can enter commands to interact with the system. Commands are entered in the format `<command> <arguments>`. Here are some basic commands you can use:

- `create <class name>`: Create a new instance of the specified class.
- `show <class name> <id>`: Show details of a specific instance.
- `destroy <class name> <id>`: Delete an instance by ID.
- `update <class name> <id> <attribute> <value>`: Update an attribute of an instance.
- `all [<class name>]`: Show all instances or instances of a specific class.
- `quit`: Exit the command interpreter.

### Examples
1. Create a new user:

2. Show details of a user with ID `1234`:

3. Update the name of a user with ID `1234`:


4. Show all instances of the User class:

5. Exit the command interpreter:
