select airport.name, game.screen_name
from airport left join game on airport.ident = game.location
where airport.name like '%Hels%';
