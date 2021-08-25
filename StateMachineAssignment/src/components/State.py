from __future__ import annotations
from abc import ABC, abstractmethod
from .Event import Event, StartEvent
from typing import List, Tuple
from enum import Enum, auto

# Enum that represents the optional statuses of the State
class StateStatus(Enum):
    INIT = auto()
    RUNNING = auto()
    FINISH = auto()
    FAIL = auto()


class State(ABC):
    """State is an abstarct class that can handle events
    """
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def handle_event(self, new_event: Event) -> StateStatus:
        pass


class CountToThreeState(State):
    """This State count until it found three consecutive events
    """

    def __init__(self) -> None:
        self.counter: int = 0
        self.last_event_type: type = None
        self.count_goal: int = 3
        self.state_status: StateStatus = StateStatus.INIT

    def __str__(self) -> str:
        return "State: CountToThreeState"

    def handle_event(self, new_event: Event) -> State:
        """run the event's action and check if there were three consecutive events
        """
        new_event.action()
        if type(new_event) == self.last_event_type:
            self.counter += 1
        else:
            self.counter = 1
        # if the counter meets the goal (3) the State status is Finished
        if self.counter == self.count_goal:
            self.state_status = StateStatus.FINISH
            print("Finish counting to Three")
        else:
            self.state_status = StateStatus.RUNNING

        self.last_event_type = type(new_event)

        # return the status of the state
        return self.state_status


class InitState(State):
    """ This state is waiting for StartEvent to be finished
    """

    def __init__(self) -> None:
        self.state_status: StateStatus = StateStatus.INIT

    def __str__(self) -> str:
        return "State: InitState"

    def handle_event(self, new_event: Event) -> StateStatus:
        new_event.action()
        if type(new_event) == StartEvent:
            self.state_status = StateStatus.FINISH
        else:
            self.state_status = StateStatus.RUNNING
        return self.state_status
