from gzip import FNAME
import json
import os
import time

FNAME = "remove_me_when_finished_updating_settings"

open(FNAME, "w").close()

print(f"Please operate the changes to the settings, then delete the file '{FNAME}'", flush=True)

for i in range(60 * 10):  # Leave a maximum of 10 mins
	if not os.path.exists(FNAME):
		print("Settings updated, the settings container will now quit")
		break

	time.sleep(1)
else:
	print("Settings not updated, aborting the settings container execution")
	os.delete(FNAME)
