import subprocess
import os

subprocess.run( ["psql -d gshdb -f sql/hourlies.sql"], shell=True)

for report in os.listdir("csv/system_jumps"):
    command = "psql -d gshdb -c '\\copy system_jumps(date,time,system_id,ship_jumps) from csv/system_jumps/" + report + " header csv'"
    subprocess.run( [command], shell=True)

for report in os.listdir("csv/system_kills"):
    command = "psql -d gshdb -c '\\copy system_kills(date,time,system_id,ship_kills,pod_kills,npc_kills) from csv/system_kills/" + report + " header csv'"
    subprocess.run( [command], shell=True)
