select regions.name as regions, 
constellations.name as constellations,
systems.name as systems
from regions 
join constellations on regions.id = constellations.region_id 
join systems on constellations.id = systems.constellation_id;
