from components import Machine
from pathlib import Path
import pickle
import logging

BACKUP_DIR = Path(__file__).parent.parent.parent / "backup"


class PersistenceManager:
    """Manage the backup and the retrieval of machine's state
    """

    def __init__(self, backup_dir: Path):
        self.backup_dir = backup_dir
        if not self.backup_dir.exists():
            self.backup_dir.mkdir()

    def backup(self, machine: Machine):
        """backup the machine in a seperate file using Pickle
        """
        backup_file = self.backup_dir / str(machine.machine_id)
        if not backup_file.exists():
            backup_file.touch()

        pickle.dump(machine, backup_file.open("wb"))

    def retrieve_data(self, machine: Machine):
        """ retrieve the backed up state of the machine
        """
        machine_id = machine.machine_id
        backup_file = self.backup_dir / str(machine_id)

        if backup_file.exists():
            backup_machine = pickle.load(backup_file.open("rb"))
            # check if the loaded data is a machine object and it's the right machine (same machine_id)
            if type(backup_machine) == type(machine) and backup_machine.machine_id == machine_id:
                machine.current_state = backup_machine.current_state
            else:
                logging.error(
                    f"machine {machine_id} doesn't exist in the backup file {backup_file}")
        else:
            logging.error(
                f"couldn't retrieve machine {machine_id} from backup file {backup_file}")


pm = PersistenceManager(BACKUP_DIR)
