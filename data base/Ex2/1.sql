update game
set co2_consumed = co2_consumed + 500, location = (
    select airport.ident
    from airport
    where name = 'Nottingham Airport'
    )
where screen_name = 'Vesa';

select * from game;
