# Eve Online General Store Helper (GSH)
A project to identify regional markets ripe for a general store and then track store information.

The program will help with the following tasks:

### Identify Markets
Track region information such as ship activity (ship kills, pod kills, pirate kills) and local availability of consumable resources (munitions, containers, boosters, repair materials).

### Regional Market Analysis
Inspect systems and stations throughout a region to find concentrated market activity. In effect, find which stations people currently buying, selling, and keeping their local base of operations.

### Source Merchandise
Cost analysis of buying finished product in large market hubs against buying raw resources and producing products myself.

### Store Accounting
Once a general store is set up and stocked, track the buy and sell orders over time to understand overall profitability and market stability.

### Buying Loot
Cost analysis of buying loot locally and selling it in major market hubs.

## Implementation Details
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

### Website Display
TBD

## Setup
### Crontab
My webserver is running the regular data pulls using cron. Add the following to the crontab:

`30 * * * * python3 <absolute path>/eve-online-general-store-helper/hourly_requests.py`. 

See [this tutorial](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) for more information.

### PostgreSQL
I'm using [postgresql](https://www.postgresql.org/) as the database for this project.

The geography db tables are set up with `psql -d <db name> -f geography_setup.psql` command from project root.

The file `sample_sql_queries.sql` has sample sql queries as a demonstration that the database is working. 

## Context
Eve online is an online spaceships game. All players are moving around and fighting and scheming in a shared universe. Eve online is different than most games in that basically every item (ships, guns, bullets, boxes, drugs, starbases) is manufactured by players from raw materials collected by other players. It is somewhat laborious to travel long distances and moving large volumes of items is a specialized skill, so several large marketplaces have developed over time. These markets are very competitive with high volume and low margins for merchants.

This tool is designed to find where players are doing activities far from the major marketplaces, so that I can sell them bullets and ships right on location (at a markup). 
