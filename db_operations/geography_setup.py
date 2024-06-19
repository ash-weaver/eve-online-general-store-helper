import subprocess

subprocess.run( ["psql -d gshdb -f sql/geography.sql"], shell=True)
subprocess.run( [
    "psql -d gshdb -c '\\copy regions(id, name) from csv/geography/regions.csv header csv'"
], shell=True)
subprocess.run( [
    "psql -d gshdb -c '\\copy constellations(id, name, region_id) from csv/geography/constellations.csv header csv'"
], shell=True)
subprocess.run( [
    "psql -d gshdb -c '\\copy systems(id, name, security_status, constellation_id) from csv/geography/systems.csv header csv'"
], shell=True)