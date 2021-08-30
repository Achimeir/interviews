from abc import ABC, abstractmethod
import logging


class Event(ABC):
    """Event is an abstract class that contains the event's id and data and can run `action`
    """
    event_id: int
    event_data: str

    @abstractmethod
    def __init__(self, event_id, event_data=None) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def action(self) -> None:
        pass


# Example of events

class StartEvent(Event):
    def __init__(self, event_id, event_data=None) -> None:
        self.event_id = event_id
        self.event_data = event_data

    def __str__(self) -> str:
        return f"Event number {self.event_id}, type: StartEvent"

    def action(self) -> None:
        logging.info(self)


class DummyEvent(Event):
    def __init__(self, event_id, event_data=None) -> None:
        self.event_id = event_id
        self.event_data = event_data

    def __str__(self) -> str:
        return f"Event number {self.event_id}, type: DummyEvent"

    def action(self) -> None:
        logging.info(self)


class AnotherDummyEvent(Event):
    def __init__(self, event_id, event_data=None) -> None:
        self.event_id = event_id
        self.event_data = event_data

    def __str__(self) -> str:
        return f"Event number {self.event_id}, type: AnotherDummyEvent"

    def action(self) -> None:
        logging.info(self)
