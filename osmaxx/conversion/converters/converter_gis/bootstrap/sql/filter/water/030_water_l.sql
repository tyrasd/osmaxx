INSERT INTO osmaxx.water_l
  SELECT osm_id as osm_id,
    osm_timestamp as lastchange,
    CASE
     WHEN osm_id<0 THEN 'R' -- Relation
     ELSE 'W'               -- Way
     END AS geomtype,
    ST_Multi(way) AS geom,
-- Classifying different Water Bodies --
    case
     when waterway in ('river','stream','canal','drain') then waterway
     when man_made is not null then man_made
     else 'waterway'
    end as type,

    name as name,
    "name:en" as name_en,
    "name:fr" as name_fr,
    "name:es" as name_es,
    "name:de" as name_de,
    int_name as name_int,
    case
        when name is not null AND name = osml10n_translit(name) then name
        when "name:en" is not null then "name:en"
        when "name:fr" is not null then "name:fr"
        when "name:es" is not null then "name:es"
        when "name:de" is not null then "name:de"
        when int_name is not null then osml10n_translit(int_name)
        when name is not null then osml10n_translit(name)
        else NULL
    end as label,
    cast(tags as text) as tags,
    cast_to_float_null_if_failed(width) as width,
-- Checks for Bridges --
    case
    when bridge in ('yes') then TRUE
    else FALSE
    end as bridge,
-- Checks for Tunnels --
    case
    when tunnel in ('yes') then TRUE
    else FALSE
    end as tunnel

     FROM osm_line
     WHERE waterway is not null or man_made in ('pier');
