# 3pt-shooting
NBA 3pt shooting is a vital aspect of any NBA team's offense. Besides the obvious advantage of giving your team more points than a 2pt shot, 3pt shots allow teams to stretch the floor. With several high-percentage shooters around the perimeter, there is more room on the interior for players with the ball to operate and find efficient shots. The best rim protectors, like Rudy Gobert, must decide between leaving open deadly shooters or abandoning the interior, or paint, where they provide the most value.

With 3pt shooting being so valuable, being able to predict shooting development from year to year is quite important. Shooting performance from year to year can vary greatly, however. Understanding the factors that can predict a player's shooting in the next season would be quite beneficial for constructing a team. Contract decisions in free-agency, extension talks, or trade negotiations would greatly benefit from the knowledge that a player is likely to perform better, or perhaps worse, in the upcoming season. 

 ## Data

 This data was acquired from [Basketball Reference](https://www.basketball-reference.com/) using [basketball_reference_scraper](https://github.com/vishaalagartha/basketball_reference_scraper). This scraper allows access to individual player statistics, including advanced stats, in various forms. For this analysis, I take advantage of player stats in the following forms: advanced, per 100 possessions, and season totals. The per possession data is particularly important, as it normalizes player stats so that players of various roles and minute totals can be compared on a more even playing field.

 One modification made to the aformentioned scraper involves importing player names. The base scraper has issues with accented letters from certain sources. To make sure some name get imported, the function `remove_accents()` attempts to match the name to names from a source that imports names more cleanly. However, the original matching algorithm often finds the incorrect match, often picking a seemingly random name from the roster. My modified function greatly reduces the probability of mismatches. 

 This analysis uses Basketball Reference data from all 30 teams from the 2009-2010 to the 2020-2021 season, retrieving advanced, per 100 possession, and season total stats. The scraper takes quite a bit of time to run to retrieve all of the desired data, potentially over an hour. The raw data was stored as in the `data/` directory in three .csv files: `allplayer_poss.csv`, `allplayer_adv.csv`, and `allplayer_tot.csv`.

 ## Preprocessing



 ## Analysis