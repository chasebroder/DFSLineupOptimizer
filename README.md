# DFSLineupOptimizer

This project uses the pydfs library to generate lineups for Daily Fantasy Sports (DFS) contests. Currently, it uses fantasy points per game (FPPG) against the player's assigned salary to determine value for each player. FPPG is calculated using DraftKings Sportsbooks odds supplied by their public API. 

## How to Run

Make sure you have at least Python 3.6 installed on your machine. Run "python optimizer.py" from your Terminal. Make sure you include a salary CSV (can download from DraftKings/FanDuel/Yahoo website) and put it in the top-level folder of the project. The project will print the generated lineups in the Terminal and also generate a CSV that is uploadable directly to the chosen site.  Make other in-code changes as necessary in the optimizer.py file, such as website and slate. This currently only supports the NBA Classic slate but will become more configurable in the future. 

See `requirements.txt` for a list of Python dependencies to run this project; these can be installed in your Terminal using the "pip" command.

## TODO
 
* Set up a command-line run configuration to set customizable options (ex. player salary file, site, etc.)
* Import injury data
* Implement supervised learning algorithm to compare projected lineups against actual top-scoring lineups and adjust as necessary
* Organize file structure: was having a tough time with __init.py__
* Adapt for other sports: ex. NHL, NFL
* Look into IndexOutOfRange error that pops up occasionally for outcome = offer.get("outcomes")[0]
* Make a "weighted average" strategy that incorporates the projected points from 2+ existing strategies as a weighted average (or see if this functionality is built into the pydfs library)
* Vegas lines juice
* Import ownership projections (Awesomeo?)
