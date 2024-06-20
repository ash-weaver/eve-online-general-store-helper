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
                  id int,
                name varchar(50),
     security_status numeric,
    constellation_id int
);

create or replace view geography as 
select regions.id as region_id,
regions.name as region_name,
constellations.id as constellation_id,
constellations.name as constellation_name,
systems.id as system_id,
systems.name as system_name
from regions
join constellations on regions.id = constellations.region_id 
join systems on constellations.id = systems.constellation_id;