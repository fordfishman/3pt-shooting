# Projecting NBA 3PT Shooting

NBA 3pt shooting is a vital aspect of any NBA team's offense. Besides the obvious advantage of giving your team more points than a 2pt shot, 3pt shots allow teams to stretch the floor. With several high-percentage shooters around the perimeter, there is more room on the interior for players with the ball to operate and find efficient shots. The best rim protectors, like Rudy Gobert, must decide between leaving open deadly shooters or abandoning the interior, or paint, where they provide the most value.

With 3pt shooting being so valuable, being able to predict shooting development from year to year is quite important. Shooting performance from year to year can vary greatly, however. Understanding the factors that can predict a player's shooting in the next season would be quite beneficial for constructing a team. Contract decisions in free-agency, extension talks, or trade negotiations would greatly benefit from the knowledge that a player is likely to perform better, or perhaps worse, in the upcoming season. 

 ## Data

 This data was acquired from [Basketball Reference](https://www.basketball-reference.com/) using [basketball_reference_scraper](https://github.com/vishaalagartha/basketball_reference_scraper). This scraper allows access to individual player statistics, including advanced stats, in various forms. For this analysis, I take advantage of player stats in the following forms: advanced, per 100 possessions, and season totals. The per possession data is particularly important, as it normalizes player stats so that players of various roles and minute totals can be compared on a more even playing field.

 One modification made to the aformentioned scraper involves importing player names. The base scraper has issues with accented letters from certain sources. To make sure some name get imported, the function `remove_accents()` attempts to match the name to names from a source that imports names more cleanly. However, the original matching algorithm often finds the incorrect match, often picking a seemingly random name from the roster. My modified function greatly reduces the probability of mismatches. 

 This analysis uses Basketball Reference data from all 30 teams from the 2009-2010 to the 2020-2021 season, retrieving advanced, per 100 possession, and season total stats. The scraper takes quite a bit of time to run to retrieve all of the desired data, potentially over an hour. The raw data was stored as in the `data/` directory in three .csv files: `allplayer_poss.csv`, `allplayer_adv.csv`, and `allplayer_tot.csv`.

 ## Preprocessing

Once the data has been read in, the data must be treated in order to be used for analysis. Several columns are removed that contain no data, as are features that are present across the three data frames. The data frames are then combined, and features with the same names but with different meanings are renamed. Primarily this includes the per 100 possession features, the season totals of which are present in the totals data frame.

The largest preprocessing hurdle is accounting for players who were members of multiple teams in a given season. This can occur if a player was traded, or if their contracted was waived, and they were re-signed to a different team. For each team a player was on in a given season, the scraper returns one row of data. Given that I want each player in a given year to have a single row, this is problematic. 

Every player-season combination that is listed more than once in the data frame was combined to be a single row. The season total statistics were simply added together across the various samples for each listing. For per possession stats, as data on the total number of possessions was unavailable, the final per possession stats were calculated as a weighted average of the games played for each team that season. 

As the targets for this analysis are the next season's 3pt percentage, I wanted to remove any player seasons with fewer than 100 3pt attempts, as more attempts are needed for the percentage to stabilize. For the player seasons remaining, I checked to see the upcoming season for that player had also met the 100 3pt attempts criterion. If it did, then the upcoming season's 3pt percentage was then added as the target feature. 

## Data Visualization

<br>

### Feature Distributions

The target feature is displayed here as a proportion, though it will still be referred to as a percentage by convention. You can see it is approximately normally distributed. The mean of the distribution is at 0.361, and it has a standard deviation of 0.0418.

![Figure 1](figs/target_dist.png)

<br>

The distributions of each of the features was also visualized. A few were selected here to show. Some features are normally distributed, such as FG%, which is the percentage of field goals attempted that were successfully made. Others exhibit skew, such as FGA or field goal attempts, the total number of shot attempts in a season. A number of skewed features also contain both positive and negative values, the example being OBPM, or offensive box plus-minus, a metric trying to ascertain player offensive value.

<br>

![Figure 2](figs/untrans_dists.png)

<br>

For this reason, the features were treated with cube root transformation. This allows more automated transformation, as log transforming data with negative values requires adding some constant to all values. Below, the effect of the transformations on the non-normal variables FGA and OBPM are displayed. FGA is relatively normal now. OBPM has less skew, but the shape of the distribution is still not entirely normal. To see all of the untransformed and transformed distributions, please view `code/python/analysis/visualize.ipynb`.

<br>

![Figure 3](figs/trans_dists.png)

<br>

![Figure 4](figs/target_corr.png)

<br>

![Figure 5](figs/corrplot.png)

<br>

 

## Analysis