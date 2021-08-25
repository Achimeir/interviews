from components.Event import DummyEvent, StartEvent, AnotherDummyEvent
from components.State import CountToThreeState, InitState, StateStatus
from components.Machine import Machine
import logging


class EventCounter():
    """create unique id for every event
    """
    counter = 0

    def count(self) -> int:
        self.counter += 1
        return self.counter


def main():
    logging.basicConfig(filename="machine.log", filemode="w", level=logging.DEBUG)

    # create machine with an InitSate as the first state
    machine = Machine(1, InitState())

    # add routes between the InitState and CountToThreeState (when one is finished the other on starts)
    machine.router.add_route(InitState, StateStatus.FINISH, CountToThreeState)
    machine.router.add_route(CountToThreeState, StateStatus.FINISH, InitState)

    print("test basic functionality:")

    # handle a StartEvent to move to the CountToThreeState
    machine.handle_event(StartEvent(event_counter.count()))

    # handle three consecutive DummyEvents
    for i in range(3):
        machine.handle_event(DummyEvent(event_counter.count()))

    print("\ntest functionality with persistency:")
    
    # the machine goes offline after startEvent
    machine.handle_event(StartEvent(event_counter.count()))
    machine.get_offline()

    # simulate delete of the current state on the machine
    machine.current_state = None

    # technician rerun the machine
    machine.run(rerun=True)

    # the machine works exactly as expected
    for i in range(3):
        machine.handle_event(DummyEvent(event_counter.count()))

    print("\ntest switching between two types of events:")

    # Get a StartEvent
    machine.handle_event(StartEvent(event_counter.count()))

    # handle switching Events (nothing will be printed)
    for i in range(3):
        machine.handle_event(DummyEvent(event_counter.count()))
        machine.handle_event(AnotherDummyEvent(event_counter.count()))


if __name__ == '__main__':
    event_counter = EventCounter()
    main()
