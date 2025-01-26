class Worker:
    def __init__(self, worker_id, name):
        self.worker_id = worker_id   # Unique ID for the worker
        self.name = name            # Worker’s name
        self.current_task = None    # Task the worker is currently handling
        self.total_tasks_completed = 0  # Count of completed tasks

    def assign_task(self, task):
        """Assign a task to the worker."""
        if self.current_task is None:
            self.current_task = task
            print(f"Worker {self.name} is now handling: {task}")
        else:
            print(f"Worker {self.name} is already busy with: {self.current_task}")

    def complete_task(self):
        """Mark the current task as completed."""
        if self.current_task is not None:
            print(f"Worker {self.name} completed: {self.current_task}")
            self.current_task = None
            self.total_tasks_completed += 1
        else:
            print(f"Worker {self.name} has no task to complete.")

    def is_available(self):
        """Check if the worker is available for a new task."""
        return self.current_task is None

    def __str__(self):
        return (
            f"Worker {self.worker_id} - {self.name} | "
            f"Current Task: {self.current_task or 'None'} | "
            f"Tasks Completed: {self.total_tasks_completed}"
        )
