"""The testing module provides variables that can be used in development, 
and helps us identify variables that need to be replaced
by real variables before pushing to staging or production."""

import time
import random

broker = 'localhost'

# Good Client ID naming convention required in staging or production.
# For testing while in development use these Client IDs:
client1 = 'test-droplet-id' # + str(uuid.uuid4())
client2 = 'test-calculator-id'
client3 = 'test-printer-id'

# For testing while in development use random number generators:
random_val = str(random.randint(1,100))
random_timer = time.sleep(random.randint(1,30))