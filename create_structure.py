import os

# Define the root directory (directly where the structure should go)
root_repo = r"C:\Users\nikhi\PycharmProjects\ERP"

# Define the folder structure
structure = [
    "config.py",
    {"entities": ["order.py", "worker.py", "equipment.py"]},
    {
        "production_steps": [
            "mixing.py",
            "baking.py",
            "packing.py",
            "cooling.py",
            "payment.py",
        ]
    },
    {
        "pipeline": [
            "pipeline.py",
            "order_queue.py",
            "task_scheduler.py",
        ]
    },
    {
        "scenarios": [
            "base_scenario.py",
            "high_demand.py",
            "equipment_failure.py",
            "rush_orders.py",
        ]
    },
    {
        "analytics": [
            "performance_metrics.py",
            "visualization.py",
        ]
    },
    {"utils": ["logger.py", "helper_functions.py"]},
    {
        "tests": [
            "test_order.py",
            "test_worker.py",
            "test_pipeline.py",
            "test_simulator.py",
            "test_scenarios.py",
            "test_analytics.py",
        ]
    },
    "simulator.py",
    "main.py",
]


def create_structure(base_path, structure):
    """
    Recursively create folders and files based on the given structure.
    """
    for item in structure:
        if isinstance(item, dict):  # If it's a subfolder, recurse
            for folder, contents in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)
        elif isinstance(item, str):  # If it's a file, create it
            file_path = os.path.join(base_path, item)
            with open(file_path, "w") as f:
                f.write("")  # Create an empty file


# Create the structure directly in the root repo
create_structure(root_repo, structure)

print(f"Folder structure created in '{root_repo}'!")
