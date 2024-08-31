select airport.name as "airport name"
from airport
where airport.type = 'large_airport' and iso_country = 'FR';