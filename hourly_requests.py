from esi_lib import request_data
import datetime
import os

# FLAGS
REQUEST_KILLS = True # /universe/system_kills/
REQUEST_JUMPS = True # /universe/system_jumps/

max_files_saved = 7*24 # keep 1 week of stats

kill_folder_location = os.path.dirname(__file__) + "/csv/system_kills/"
jump_folder_location = os.path.dirname(__file__) + "/csv/system_jumps/"
file_name = datetime.datetime.now().strftime(
    "%Y"+"-"+"%m"+"-"+"%d"+"_"+"%H"+":"+"%M"+":"+"%S")

if REQUEST_KILLS:
    # /universe/system_kills/
    # updates hourly
        # int npc_kills
        # int pod_kills
        # int ship_kills
        # int system_id
    report = request_data("/universe/system_kills/")

    if not os.path.exists(kill_folder_location):
        os.mkdir(kill_folder_location)

    file = open(kill_folder_location + file_name + ".csv", "w")
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
    files = os.listdir(kill_folder_location)
    while len(files) > max_files_saved:
        files.sort()
        os.remove(str(kill_folder_location + files.pop(0)))

if REQUEST_JUMPS:
    # /universe/system_jumps/
    # updates hourly
        # int ship_jumps
        # int system_id
    report = request_data("/universe/system_jumps/")

    if not os.path.exists(jump_folder_location):
        os.mkdir(jump_folder_location)

    file = open(jump_folder_location + file_name + ".csv", "w")
    file.write("system_id,ship_jumps\n")
    for item in report:
        file.write(
            str(item["system_id"])+","+
            str(item["ship_jumps"])+
            "\n")
    file.close()

    # remove old files
    files = os.listdir(jump_folder_location)
    while len(files) > max_files_saved:
        files.sort()
        os.remove(str(jump_folder_location + files.pop(0)))
