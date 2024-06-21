# Eve Online General Store Helper (GSH)
A project to identify regional markets ripe for a general store and then track store information.

- [Implementation Details](#implementation)
- [Setup](#setup)
- [Background Context](#context) (never heard of eve online?)

The program will help with the following tasks:

### Identify Markets
Track region information such as ship activity (ship kills, pod kills, pirate kills) and local availability of consumable resources (munitions, containers, boosters, repair paste).

### Regional Market Analysis
Inspect systems and stations throughout a region to find concentrated market activity. In effect, find which stations people currently buying, selling, and keeping their local base of operations.

### Source Merchandise
Cost analysis of buying finished product in large market hubs against buying raw resources and producing products myself.

### Store Accounting
Once a general store is set up and stocked, track the buy and sell orders over time to understand overall profitability and market stability.

### Buying Loot
Cost analysis of buying loot locally and selling it in major market hubs.

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
TBD

## Setup<a name="setup"></a>
### Crontab
My webserver is running the regular data pulls using cron. Add the following to the crontab:

`30 * * * * python3 <absolute path>/eve-online-general-store-helper/esi_requests/hourly_requester.py`. 

See [this tutorial](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) for more information.

### PostgreSQL
I'm using [postgresql](https://www.postgresql.org/) as the database for this project.

The db tables are set up with the python files `db_operations/geography_setup.py` and `db_operations/hourlies_setup.py`

## Background Context<a name="context"></a>
[Eve Online](https://www.eveonline.com/) is a computer spaceships game where all players are in a shared gamespace. Characters specialise into different playstyles, such doing quests fighting npc ships, large scale turf wars, hauling cargo, exploring space dungeons, piracy against other players, mining asteroids, and many others.

Almost all items (such as spaceships, bullets, probes, ship armor, cybernetic implants) in eve online are crafted by players, from raw resources collected by players. The raw resources and finished products are sold at space stations and must be bought at those same stations. Because moving large volumes of items around is both slow (because freighters are slow) and risky (because players will attack freighters for their cargo), commerce has coalesced into rougly 5 large marketplaces that are some distance from each other.

The major marketplaces are burstling trade hubs where almost any ship or item can be bought or sold for a competitive price relatively quickly. Prices are local to each market hub and set by the player selling the item rather than a price set by the game. Many players focus their gameplay on these markets; buying from one market and then selling at another, buying items when they're cheap and selling them in the same market when the price goes up, or buying raw resources to craft into finished products to sell.

Outside of these large markets, item availablity is wildly inconsistent. Basic items can be simply unavailable, sold in small quantities at outrageous prices, or be found at a huge discount compared to the main hubs. If a player is on their way to the frontier to shoot missiles at something and realizes they forgot their missiles at home, they generally have to go all the way back and pick them up or go to a major market and buy them. 

This tool is an application to identify where and what player activity is happening away from the large market hubs in an effort to set up small markets that sell those players missiles (and drones, repair paste, boxes, etc). See [implementation details](#implementation) for the specific technologies I'm using to collect, sort, and display the data.

The developers of the game have made a ton of real-time game data available through through their swagger api. This includes generalized data like how many players were killed in each solar system in the last hour, to extremely specific data like how much a specific missile costs at a specific space station at any time. Beyond that, they provide an sso system where applications can ask players to log in for character specific data, like what items they have for sale at which stations or read mail from their evemail inbox.

And why? 

Ever since I was born it's been my dream to be petite bourgeoisie.
