select country.name
    from country where country.iso_country in(
        select iso_country from airport where airport.name like "Satsuma%"
    );

