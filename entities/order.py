from datetime import datetime, timedelta

class Order:
    def __init__(self, order_id, quantity, rush=False):
        self.order_id = order_id                  # Unique ID for the order
        self.quantity = quantity                  # Quantity in dozens
        self.rush = rush                          # Whether it's a rush order
        self.completed = False                   # Whether the order is completed
        self.status = "Pending"                  # Order status: Pending, In Progress, Completed
        self.placed_time = datetime.now()        # Time when the order was placed
        self.estimated_completion_time = None    # To be calculated during the pipeline

    def calculate_priority(self):
        """Assign priority: higher priority for rush orders."""
        return 1 if self.rush else 0

    def set_status(self, status):
        """Update the order status."""
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if status in valid_statuses:
            self.status = status
        else:
            raise ValueError(f"Invalid status: {status}")

    def set_estimated_completion_time(self, time_minutes):
        """Set the estimated completion time for the order."""
        self.estimated_completion_time = self.placed_time + timedelta(minutes=time_minutes)

    def __str__(self):
        return (
            f"Order {self.order_id}: {self.quantity} dozen cookies (Rush: {self.rush}) | "
            f"Status: {self.status} | Placed at: {self.placed_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
