drop table if exists system_kills;
drop table if exists system_jumps;

create table system_kills (
          id serial,
         date date,
         time time,
    system_id int,
    ship_kills int,
    pod_kills int,
    npc_kills int
);

create table system_jumps (
          id serial,
         date date,
         time time,
    system_id int,
    ship_jumps int
);
