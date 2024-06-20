-- show all systems, organized by constellation and region
select region_name as region, 
constellation_name as constellation, 
system_name as system
from geography
order by region_name;

-- average system security by region
select region_name as region, 
count(systems) as system_count, 
round(avg(systems.security_status),2) as avg_system_security
from geography
join systems on systems.id = geography.system_id
group by region_name
order by avg_system_security desc;

-- average system security by region but with the completely lawless regions removed (i will get killed by roving enforcers)
select region_name as region, 
count(systems) as system_count, 
round(avg(systems.security_status),2) as avg_system_security
from geography
join systems on systems.id = geography.system_id
group by region_name
having avg(systems.security_status) > -0.5
order by avg_system_security desc;

-- system jumps
select system_id, systems.name, sum(ship_jumps) 
from system_jumps 
join systems on systems.id = system_jumps.system_id 
group by system_id, systems.name 
order by sum desc;

-- jita traffic by hour
select date, time, sum(ship_jumps) as jumps
from system_jumps
join systems on systems.id = system_jumps.system_id 
where systems.name = 'Jita'
group by systems.id,date,time;

-- most kills in all systems over full period
select systems.name, sum(ship_kills) as ship_kills, sum(pod_kills) as pods 
from system_kills
join systems on systems.id = system_kills.system_id
group by systems.name
order by ship_kills desc;

-- all kills in jita by hour with pod percentage
select date, date_trunc('hour', time) as time, 
ship_kills, 
pod_kills, 
trunc((cast(pod_kills as float)/ship_kills * 100)) as pod_percentage
from system_kills
join systems on systems.id = system_kills.system_id
where systems.name = 'Jita'
order by date,time;

-- average npc kills by region (per hour)
select region_name, 
trunc(avg(npc_kills),2) as npc_kills, 
round(avg(systems.security_status),2) as avg_system_security
from system_kills
join geography on geography.system_id = system_kills.system_id
join systems on systems.id = system_kills.system_id
group by region_name
order by npc_kills desc;
