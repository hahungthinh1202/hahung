use pandemic;

drop table city;
drop table infection_deck;;
drop table infection_discard;
drop table player_current;
drop table player_own;
drop table game_current;
drop table player_card_current;
drop table event;

create table city
(
    id varchar(40) not null ,
    city_name varchar(40) default null,
    latitude double default null,
    longitude double default null,
    country_name varchar(40) default null,
    virus varchar(40) default null,
    connection varchar(40) default null,
    blue int default 0,
    violet int default 0,
    red int default 0,
    yellow int default 0,
    research_center bool default false,
    is_outbreak bool default false
);

insert into city values
    ( 1, 'San Francisco',  98,230, 'United states'   ,'blue','27 34 2 37',0,0,0,0,0,0),
    ( 2, 'Chicago'      , 199,205, 'United states'   ,'blue','1 5 3 37 38',0,0,0,0,0,0),
    ( 3, 'Montréal'     , 275,192, 'Canada'          ,'blue','2 4 6',0,0,0,0,0,0),
    ( 4, 'New York'     , 351,235, 'United states'   ,'blue','3 6 8 7',0,0,0,0,0,0),
    ( 5, 'Atlanta'      , 217,258, 'United states'   ,'blue','2 6 39',0,0,0,0,1,0),
    ( 6, 'Washington'   , 325,262, 'United states'   ,'blue','5 3 4 39',0,0,0,0,0,0),
    ( 7, 'London'       , 489,165, 'United Kingdom'  ,'blue','4 8 9 12',0,0,0,0,0,0),
    ( 8, 'Madrid'       , 482,234, 'Spain'           ,'blue','42 4 7 12 13',0,0,0,0,0,0),
    ( 9, 'Paris'        , 563,155, 'France'          ,'blue','7 12 10',0,0,0,0,0,0),
    (10, 'Helsinki'     , 620,133, 'Germany'         ,'blue','9 12 15 11',0,0,0,0,0,0),
    (11, 'Moscow'       , 658,143, 'Russia'          ,'blue','10 15 16',0,0,0,0,0,0),
    (12, 'Milan'        , 580,212, 'Italy'           ,'blue','13 8 7 9 10',0,0,0,0,0,0),
    (13, 'Algiers'      , 550,262, 'Algeria'         ,'violet','8 12 15 14',0,0,0,0,0,0),
    (14, 'Cairo'        , 645,277, 'Egypt'           ,'violet','13 15 22 24 46',0,0,0,0,0,0),
    (15, 'Istanbul'     , 638,228, 'Turkey'          ,'violet','13 10 11 16 22 14',0,0,0,0,0,0),
    (16, 'Kyiv'         , 696,194, 'Ukraine'          ,'violet','15 11 17',0,0,0,0,0,0),
    (17, 'Tehran'       , 764,202, 'Iran'            ,'violet','16 18 23 22',0,0,0,0,0,0),
    (18, 'Delhi'        , 840,259, 'India'           ,'violet','17 19 20 21 23',0,0,0,0,0,0),
    (19, 'Kolkata'      , 891,291, 'India'           ,'violet','18 20 32 31',0,0,0,0,0,0),
    (20, 'Chennai'      , 849,384, 'India'           ,'violet','21 18 19 32 35',0,0,0,0,0,0),
    (21, 'MumBai'       , 798,350, 'India'           ,'violet','20 18 23',0,0,0,0,0,0),
    (22, 'Baghdad'      , 703,258, 'Iraq'            ,'violet','23 17 15 14 24',0,0,0,0,0,0),
    (23, 'Karachi'      , 785,290, 'Pakistan'        ,'violet','24 22 17 18 21',0,0,0,0,0,0),
    (24, 'Riyadh'       , 712,305, 'Saudi Arabia'    ,'violet','14 22 23',0,0,0,0,0,0),
    (25, 'Beijing'      , 941,205, 'China'           ,'red','26 29',0,0,0,0,0,0),
    (26, 'Seoul'        , 1008,201, 'South Korea'     ,'red','25 29 27',0,0,0,0,0,0),
    (27, 'Tokyo'        , 1059,224, 'Japan'           ,'red','26 29 28 1',0,0,0,0,0,0),
    (28, 'Osaka'        , 1070,258, 'Japan'           ,'red','27 30',0,0,0,0,0,0),
    (29, 'Shanghai'     , 938,261, 'China'           ,'red','25 26 27 30 31',0,0,0,0,0,0),
    (30, 'Taipei'       , 1040,308, 'Taiwan'          ,'red','29 31 34 28',0,0,0,0,0,0),
    (31, 'Hong Kong'    , 969,304, 'Hong Kong'       ,'red','29 30 34 33 32 19',0,0,0,0,0,0),
    (32, 'Bangkok'      , 918,351, 'Thailand'        ,'red','19 31 33 35 20',0,0,0,0,0,0),
    (33, 'Ho Chi Minh'  , 958,390, 'Vietnam'         ,'red','35 32 31 34',0,0,0,0,0,0),
    (34, 'Manila'       , 1002,352, 'Philippines'     ,'red','33 31 30 36 1',0,0,0,0,0,0),
    (35, 'Jakarta'      , 905,469, 'Indonesia'       ,'red','20 32 33 36',0,0,0,0,0,0),
    (36, 'Sydney'       , 1084,565, 'Australia'       ,'red','35 34 37',0,0,0,0,0,0),
    (37, 'Los Angeles'  , 92,300, 'United states'   ,'yellow','36 1 2 38',0,0,0,0,0,0),
    (38, 'Mexico City'  , 174,329, 'Mexico'          ,'yellow','37 2 39 40 41',0,0,0,0,0,0),
    (39, 'Miami'        , 237,297, 'United states'   ,'yellow','38 5 6 40',0,0,0,0,0,0),
    (40, 'Bogotá'       , 251,390, 'Colombia'        ,'yellow','38 39 42 43 41',0,0,0,0,0,0),
    (41, 'Lima'         , 241,466, 'Peru'            ,'yellow','44 38 40',0,0,0,0,0,0),
    (42, 'Sao Paulo'    , 370,520, 'Brazil'          ,'yellow','43 40 8 45',0,0,0,0,0,0),
    (43, 'Buenos Aires' , 332,575, 'Argentina'       ,'yellow','40 42',0,0,0,0,0,0),
    (44, 'Santiago'     , 276,550, 'Chile'           ,'yellow','41',0,0,0,0,0,0),
    (45, 'Lagos'        , 519,385, 'Nigeria'         ,'yellow','42 46 48',0,0,0,0,0,0),
    (46, 'Khartoum'     , 653,354, 'Sudan'           ,'yellow','45 48 47 14',0,0,0,0,0,0),
    (47, 'Johannesburg' , 634,536, 'South Africa'    ,'yellow','48 46',0,0,0,0,0,0),
    (48, 'Kinshasa'     , 589,439, 'Congo'           ,'yellow','45 46 47',0,0,0,0,0,0);

create table player_current
(
    player_id varchar(40) not null ,
    player_name varchar(40) default null,
    city_id varchar(40)  not null,
    role varchar(40) default null,
    action_point int default 4,
    game_id varchar(40) not null
);

insert into player_current
values
    (1,'thinh',10,'medic', 4,'g1'),
    (2,'Tam',10,'scientist',4,'g1');


create table infection_deck
(
    city_id varchar(40) default null
);

create table infection_discard
(
    city_id varchar(40) default null
);

create table player_own
(
    player_id varchar(40) not null,
    card_id varchar(40) not null
);

create table player_card_current
(
    city_id varchar(40) default null
);

create table game_current
(
    game_id varchar(40) not null,
    infection_track int default 0,
    outbreak_track int default 0,
    blue bool default false,
    violet bool default false,
    red bool default false,
    yellow bool default false,
    research_center int default 1,
    player_turn int default 1
);

insert into game_current
values ('g1',0,0, FALSE,FALSE,FALSE,FALSE, 1, 1);


create table event(
    id varchar(40) not null,
    story varchar(200) default null
);

insert into event
values
    (1,'Mysterious Epidemic Sweeps Through {city_name}: Hospitals Overwhelmed as Cases Surge'),
    (2,'{city_name} on High Alert: Health Officials Scramble to Contain Fast-Spreading Virus'),
    (3,'Epidemic Outbreak at {city_name}: Thousands Infected as City Faces Unprecedented Health Crisis'),
    (4,'State of Emergency Declared at {city_name}: Local Authorities Battle Rapidly Growing Epidemic'),
    (5,'Contagion Crisis: Quarantine Enforced at {city_name} as Epidemic Spirals Out of Control'),
    (6,'Health Crisis Escalates at {city_name}: Schools, Businesses Shut Down Amid Epidemic Fears'),
    (7,'Epidemic Wreaks Havoc: Hospitals at {city_name} Reach Capacity, Urgent Response Launched'),
    (8,'Deadly Epidemic Hits {city_name}: Officials Warn of Public Health Catastrophe'),
    (9,'Massive Infection Spike: {city_name} Residents Urged to Stay Indoors as Epidemic Spreads'),
    (10,'Epidemic Forces Lockdown: {city_name} Streets Empty as Health Workers Race to Contain Virus'),
    (11,'{city_name} Paralyzed by Epidemic: Government Rushes to Deploy Emergency Resources'),
    (12,'Epidemic Surge: Experts Warn of New Wave of Infections as {city_name} Struggles to Cope'),
    (13,'Breaking: {city_name} Faces Critical Shortage of Medical Supplies Amid Epidemic Chaos'),
    (14,'Public Health in {city_name}: City Declares Martial Law to Control Epidemic Spread'),
    (15,'Epidemic Sparks Panic: Citizens Flee as Infections Multiply Across {city_name}'),
    (16,'Hospitals on the Brink: Healthcare System Crumbles Under Weight of Epidemic at {city_name}'),
    (17,'{city_name} Lockdown Enforced: Epidemic Pushes Local Authorities to Extreme Measures'),
    (18,'Contagion Spreads at {city_name}: Medical Teams Mobilized as Epidemic Claims More Lives'),
    (19,'Urgent Action Needed: Experts Warn Epidemic Could Spread Beyond {city_name} Borders'),
    (20,'Epidemic Threatens to Overwhelm {city_name}: Critical Infrastructure Under Strain');





