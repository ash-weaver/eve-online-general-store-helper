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
