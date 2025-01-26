# Time constants (in minutes)
MIXING_TIME = 6       # Time to mix ingredients
BAKING_TIME = 9       # Time to bake one tray of cookies
COOLING_TIME = 5      # Time to cool cookies after baking
PACKING_TIME = 2      # Time to pack one dozen cookies
PAYMENT_TIME = 1      # Time to process payment for an order

# Equipment capacities
OVEN_CAPACITY = 1     # Trays that can be baked simultaneously
MIXER_CAPACITY = 3    # Dozens of cookies that can be mixed simultaneously

# Cost-related constants
COST_PER_DOZEN = 0.60  # Cost of ingredients per dozen cookies
BOX_COST = 0.10        # Cost of one packing box

# Revenue-related constants
PRICE_PER_DOZEN = 1.50         # Selling price per dozen cookies
RUSH_ORDER_MULTIPLIER = 1.5    # Price multiplier for rush orders

# Worker-related constants
WORKER_SHIFT_DURATION = 240    # Total shift duration for a worker (in minutes)

# Scenario-related constants
EQUIPMENT_FAILURE_PROBABILITY = 0.1  # Probability of equipment failure

# Logging and debugging
LOGGING_LEVEL = "INFO"          # Logging level: DEBUG, INFO, WARNING, ERROR
ENABLE_ANALYTICS = True         # Enable analytics for performance tracking
DEBUG_MODE = False              # Enable detailed debug logs
