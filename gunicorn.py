import os
import sys

sys.stdout = sys.stderr
bind  = "0.0.0.0:"+str(os.environ.get("PORT", "5000"))
print bind
workers = 6
timeout = 25
