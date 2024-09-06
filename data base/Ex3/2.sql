select country.name as 'country name', airport.name as "airport name"
from airport join country on airport.iso_country = country.iso_country
where country.name="Finland" and scheduled_service = "yes";