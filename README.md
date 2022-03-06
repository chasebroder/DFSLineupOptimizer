# DFSLineupOptimizer

This project uses the pydfs library to generate lineups for Daily Fantasy Sports (DFS) contests. Currently, it uses fantasy points per game against the player's assigned salary to determine value for each player.

## How to Run
Make sure you have at least Python 3.6 installed on your machine. Run "python dk_salaries.csv" from your Terminal, using the 
supplied CSV. If you'd like to use your own CSV, add it to this folder or reference the file path in code. Make other in-code
changes as necessary, such as website and slate. 

## TODO

* Explore options that library provides to calculate more accurate values for players (ex. using player projections, matchups, trends, etc)
* Set up a command-line run configuration to set customizable options (ex. player salary file, site, etc.)
* Figure out how to filter out injured players (player.is_injured doesn't seem to supply valid data)
* Make custom Fantasy Points Strategy (some way to factor in matchup, projected points, and other factors that current implementations do not)
* Implement supervised learning algorithm to compare projected lineups against actual top-scoring lineups and adjust as necessary