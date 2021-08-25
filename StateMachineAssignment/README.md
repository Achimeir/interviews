# Assignment 1: Framework implementation
## Event
Event represents an event in the system.
When events arrives to the state machine it passed to the current state and the state handle it.
An event can be a simple one that do nothing or more sophisticated. Its functionality is implemented in it's `action` function

## State
State represents a state in the state machine. when an Event is given to it by the state machine the State process it and it's status changed according to the event. The State can be in status INIT,RUNNING,FINISHED or FAIL.

## Machine
Machine represents the state machine and it handles the current State of the system. After each event the machine checks the status of the current State and change the State if needed (in most implementations the State is changed after it's status is FINISHED)

## Additional objects
### Router
Router helps the Machine to handle the routes between States and when the State needs to be changed.
The Router contains a dictionary with the State and State's status as keys and the next State as value.
If a key `(State,State_status)` doesn't exist it's mean that when the current state has this status it doesn't needs to be changed.
When a user implements a Machine he needs to describe the routes between it's States using _Machine.router.add_route()_

### PersistenceManager
PersistenceManager handles backing up and retrieving data
The system has one instance of PersistenceManager (pm) and all the Machines use it

# Assignment 2: Add tests
## Running the tests
To run the test run `python src\testStateMachine.py` when your cwd is the directory StateMachineAssignment

## Tests implementations
The implementation of the derived classes are in their Super class files (for example: dummyEvent is in Event.py)
In the test code a machine is initiated, the Machine has an *InitState* and a *CountToThreeState*. When an event of *StartEvent* arrives the Machine's State changed from 
*InitState* to *CountToThreeState*.
The *CountToThreeState* will run until it detects that the same type of Event has been fired 3 times in a row and then it will print a message and the Machine's State changed back to *InitState* because there are
no requirements for what the Machine will do with any subsequent events (if we want to Machine to continuously detects 3 consecutive Events the Machine State needs to changed back to *CountToThreeState*).

The test check three scenarios:
* regular use
* the Machine is taken offline after *StartEvent*
* the Machine doesn't get 3 consecutive Events

The output should looks like this:
```
test basic functionality:
Finish counting to Three

test functionality with persistency:
Finish counting to Three

test switching between two types of events:

```
## Logs
All the important things that happends in the program will be logged (using logging) in a log file named machine.log

# Assignment 3: support persistency
## Backup files
Inside the StateMachineAssignment directory a directory named backup will be created. When a Machine is backed up (after getting offline) a new file is created for the Machine, and when the Machine needs to retrieve the data (when the user rerun the machine) it reads from the file. The actual magic of saving and getting the Machine class data is being performed using Pickle 
