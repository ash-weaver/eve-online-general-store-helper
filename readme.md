# Eve Online General Store Helper (GSH)
A project to identify regional markets ripe for a general store and then track store information.

The program will help with the following tasks:

### Identify Markets
Track region information such as ship activity (ship kills, pod kills, pirate kills) and local availability of consumable resources (munitions, containers, boosters, repair materials).

### Regional Market Analysis
Inspect systems and stations throughout a region to find concentrated market activity. In effect, find where are people currently buying, selling, and keeping their local base of operations.

### Source Merchandise
Cost analysis of buying finished product in large market hubs against buying raw resources and producing products myself.

### Store Accounting
Once a general store is set up and stocked, track the buy and sell orders over time to understand overall profitability and market stability.

### Buying Loot
Cost analysis of buying loot locally and selling it in major market hubs.

## Implementation Details
### EVE ESI
Using python, the GSH will poll the [EVE ESI](https://esi.evetech.net/ui/) for data. Some data, like geographic information will need to be checked infrequently, while other information will be getting polled often, such as player activity statistics (hourly) or market data (daily).

The data is returned as JSON objects that will be converted and stored as csv files to aid with postgresql integration.

### Number Crunching
The second part of the GSH is using a postgresql database to store and crunch the numbers.

### Website Display
TBD

## Setup
### Crontab
I am running the regular data pulls from my webserver using cron. For example, the /universe/system-kills/ job has the following in the crontab file: `30 * * * * p ~/general-store-helper/system_kills.py`. See [this tutorial](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) for more information.
