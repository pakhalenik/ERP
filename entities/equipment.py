class Equipment:
    def __init__(self, equipment_id, name, capacity):
        self.equipment_id = equipment_id  # Unique ID for the equipment
        self.name = name                  # Name of the equipment (e.g., Oven, Mixer)
        self.capacity = capacity          # Maximum capacity (e.g., trays or dozens of cookies)
        self.in_use = False               # Whether the equipment is currently in use
        self.current_task = None          # Task currently being processed

    def use(self, task):
        """Mark the equipment as in use with a specific task."""
        if not self.in_use:
            self.in_use = True
            self.current_task = task
            print(f"{self.name} is now in use for: {task}")
        else:
            print(f"{self.name} is already busy with: {self.current_task}")

    def release(self):
        """Release the equipment after completing the task."""
        if self.in_use:
            print(f"{self.name} completed: {self.current_task}")
            self.in_use = False
            self.current_task = None
        else:
            print(f"{self.name} is not currently in use.")

    def is_available(self):
        """Check if the equipment is available."""
        return not self.in_use

    def __str__(self):
        return (
            f"Equipment {self.equipment_id} - {self.name} | "
            f"Capacity: {self.capacity} | "
            f"Status: {'In Use' if self.in_use else 'Available'}"
        )
