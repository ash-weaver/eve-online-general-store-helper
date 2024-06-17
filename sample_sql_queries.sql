-- show all systems, organized by constellation and region
select regions.name as regions, 
constellations.name as constellations,
systems.name as systems
from regions 
join constellations on regions.id = constellations.region_id 
join systems on constellations.id = systems.constellation_id;

-- average system security by region
select regions.name as region, 
count(systems) as system_count, 
round(avg(systems.security_status),2) as avg_system_security
from regions
join constellations on regions.id = constellations.region_id 
join systems on constellations.id = systems.constellation_id
group by regions.name
order by avg_system_security desc;

-- average system security by region but with the completely lawless regions removed (i will get killed by roving enforcers)
select regions.name as region, 
count(systems) as system_count, 
round(avg(systems.security_status),2) as avg_system_security
from regions
join constellations on regions.id = constellations.region_id 
join systems on constellations.id = systems.constellation_id
group by regions.name
having avg(systems.security_status) > -0.5
order by avg_system_security desc;