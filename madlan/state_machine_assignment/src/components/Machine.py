from __future__ import annotations
from collections import defaultdict
from .State import State, StateStatus
from .Event import Event
from .Persistence import pm
import logging


class Router:
    """Manage the routes between states in the state machine
    """

    def __init__(self) -> None:
        self.routes = defaultdict()

    def add_route(self, src_state_type: type, state_status: StateStatus, dest_state_type: type):
        """add route between state and it's status to the state that should be next
        """
        self.routes[(src_state_type, state_status)] = dest_state_type

    def remove_route(self, src_state_type: type, state_status: StateStatus):
        """ remove old routes, for the completeness of the implementation
        """
        self.routes.pop((src_state_type, state_status))

    def get_next_state(self, src_state_type: type, state_status: StateStatus):
        """ return the next state according to the current state and it's status
        """
        if (src_state_type, state_status) in self.routes.keys():
            return self.routes[(src_state_type, state_status)]
        # return None if next_state doesn't exist
        return None


class Machine:
    """The State Machine
    """

    def __init__(self, machine_id: int, init_state: State) -> None:
        self.machine_id = machine_id
        self.current_state = init_state
        self.router = Router()

    def __str__(self):
        return f"Machine {self.machine_id}, current state {self.current_state}"

    def run(self, rerun: bool = False) -> None:
        """run the state machine, allow persistency using `rerun` flag
        """
        if rerun:
            # if rerun flag is selected the machine uses the PersistenceManager (pm)
            # to retrieve the current state from the backup file
            pm.retrieve_data(self)
            logging.info(f"Rerunning {self}")
        else:
            logging.info(f"Running {self}")

    def change_state(self, new_state: type) -> None:
        """change the current state of the machine
        """
        last_state = str(self.current_state)
        self.current_state = new_state()
        logging.info(f"Change state from {last_state} to {self.current_state}")

    def handle_event(self, new_event: Event) -> None:
        """handle an event
        """
        # pass the event to the current state and get back it's status
        return_status = self.current_state.handle_event(new_event)

        # check in the router if given the current state and it's status the machine needs to change state
        new_state = self.router.get_next_state(
            type(self.current_state), return_status)
        if new_state:
            self.change_state(new_state)

    def backup(self) -> None:
        """backup the machine using the PersistenceManager
        """
        logging.info(f"Backup the data of {self}")
        pm.backup(self)

    def get_offline(self) -> None:
        """get the machine offline
        """
        logging.warning("Getting Offline")
        self.backup()
