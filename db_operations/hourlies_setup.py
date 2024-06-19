import subprocess
import os

subprocess.run( ["psql -d gshdb -f sql/hourlies.sql"], shell=True)
# print(os.listdir("csv/system_jumps"))
for report in os.listdir("csv/system_jumps"):
    command = "psql -d gshdb -c '\\copy system_jumps(date,time,system_id,ship_jumps) from csv/system_jumps/" + report + " header csv'"
    subprocess.run( [command], shell=True)