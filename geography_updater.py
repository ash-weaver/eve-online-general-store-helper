from ash_esi_lib import request_data

# flags
UPDATE_REGIONS = True
UPDATE_CONSTELLATIONS = False
UPDATE_SYSTEMS = False

output_location = "csv/geography/"

print("hello captain :)")

if UPDATE_REGIONS:
    print("updating region information...")
    # /universe/regions/
        # [region_id]
    # /universe/regions/id/
        # region_id, name, ?description, [constellations]
    response = request_data("/universe/regions/")
    file_regions = open(output_location + "regions.csv", "w")
    file_regions.write("region_id,name\n")
    for id in response:
        region = request_data("/universe/regions/" + str(id) + "/")
        file_regions.write(
            str(region["region_id"]) + "," +
            "'" + region["name"] + "'"
            + "\n")
    file_regions.close()

if UPDATE_CONSTELLATIONS:
    print("updating constellation information...")
    # /universe/constellations/ 
        # [constellations_id]
    # /universe/constellations/id/
        # constellation_id, name, position, region_id, [systems]
    constellations = request_data("/universe/constellations/")
    file_constellations = open(output_location + "constellations.csv", "w")
    file_constellations.write("constellation_id,name,region_id\n")
    for id in constellations:
        constellation = request_data("/universe/constellations/" + str(id) + "/")
        file_constellations.write(
            str(constellation["constellation_id"]) + "," +
            "'" + constellation["name"] + "'" + "," +
            str(constellation["region_id"]) + "," +
            "\n")
    file_constellations.close()

if UPDATE_SYSTEMS:
    print("updating system information...")
    # /universe/systems/ 
        # [system_id]
    # /universe/systems/id/
        # constellation_id
        # name
        # ?[planets]
        # position
        # ?security_class
        # security_status
        # ?star_id
        # ?stargates
        # ?stations
        # system_id
    systems = request_data("/universe/systems/")
    file_systems = open(output_location + "systems.csv", "w")
    file_systems.write("system_id,name,security_status,constellation_id\n")
    for id in systems:
        system = request_data("/universe/systems/" + str(id) + "/")
        file_systems.write(
            str(system["system_id"]) + "," +
            "'" + system["name"] + "'" + "," +
            "'" + str(system["security_status"]) + "'" + "," +
            str(system["constellation_id"]) + "," +
            "\n")
    file_systems.close()

print("all done captain :)")
