from ash_esi_lib import request_data
import datetime
import os

# FLAGS
REQUEST_UPDATES = True

max_files_saved = 7*24 # keep 1 week of stats (assuming hourly pulls)

file_location = "csv/system_kills/"
file_name = datetime.datetime.now().strftime(
    "%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+":"+"%M"+":"+"%S")

if REQUEST_UPDATES:
    # /universe/system_kills/
    # updates hourly
        # int npc_kills
        # int pod_kills
        # int ship_kills
        # int system_id
    report = request_data("/universe/system_kills/")

    file = open(file_location + file_name + ".csv", "w")
    file.write("system_id,ship_kills,pod_kills,npc_kills\n")
    for item in report:
        file.write(
            str(item["system_id"])+","+
            str(item["ship_kills"])+","+
            str(item["pod_kills"])+","+
            str(item["npc_kills"])+
            "\n")
    file.close()

# remove old files
files = os.listdir(file_location)
while len(files) > max_files_saved:
    files.sort()
    os.remove(str(file_location + files.pop(0)))