select game.screen_name, airport.name
from game inner join airport on game.location = airport.ident;