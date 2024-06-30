# Eve Online Geography Terminal
A bunch of fun statistics about space!

- [Implementation Details](#implementation)
- [Setup](#setup)

## Implementation Details<a name="implemenation"></a>
### EVE ESI
Using python, the GSH polls the [EVE ESI](https://esi.evetech.net/ui/) for data. Some data, like geographic information needs to be checked infrequently, while other information is checked regularly, such as player activity statistics (hourly) or market data (daily).

| Request                  | Frequency |
| ------------------------ | --------- |
| /universe/system-kills/  | hourly    |
| /universe/system-jumps/  | hourly    |
| /universe/regions/       | once      |
| /universe/constellations | once      |
| /universe/systems        | once      |

The data is returned as JSON objects that are converted and stored as csv files to aid with postgresql integration.

### Number Crunching
The second part of the GSH is using a postgresql database to store and crunch the numbers.

The file `sample_sql_queries.sql` has sample sql queries as a demonstration that the database is working. 

### Website Display
Website art mockups made with [REXpaint](https://www.gridsagegames.com/rexpaint/)!

## Setup<a name="setup"></a>
### Crontab
My webserver is running the regular data pulls using cron. Add the following to the crontab:

`30 * * * * python3 <absolute path>/eve-online-general-store-helper/esi_requests/hourly_requester.py`. 

See [this tutorial](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) for more information.

### PostgreSQL
I'm using [postgresql](https://www.postgresql.org/) as the database for this project.

The db tables are set up with the python files `db_operations/geography_setup.py` and `db_operations/hourlies_setup.py`

