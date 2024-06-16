drop table if exists regions;
drop table if exists constellations;
drop table if exists systems;

create table regions (
	         id int,
           name varchar(50)
);

create table constellations (
             id int,
           name varchar(50),
      region_id int
);

create table systems (
           system_id int,
                name varchar(50),
     security_status float(23),
    constellation_id int
);

-- copy regions(id, name)
-- from ../csv/geography/regions.csv
-- header csv;