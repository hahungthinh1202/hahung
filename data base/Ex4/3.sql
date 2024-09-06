select game.screen_name, country.name
from game inner join airport on game.location = airport.ident
       inner join country on airport.iso_country = country.iso_country;
