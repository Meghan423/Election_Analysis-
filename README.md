# Election_Analysis

## Project Overview Part 1: Candidate Results
A Colorado Board of Elections employee has requested the following deliverables to complete the election audit of a recent local congressional election. 

1. The total number of votes cast. 
2. A complete list of candidates who received votes.
3. The total number of votes each candidate received.
4. The percentage of votes each candidate won.
5. The winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest voter turnout.

## Resources
-Data Source: election_results.csv

-Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Audit Results
After analyzing the data, we know

**Total Votes: 369,711**

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)


**Winner: Diana DeGette**

Winning Vote Count: 272,892

Winning Percentage: 73.8%


**County Votes:**

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)


**Highest County Turnout: Denver**

County Vote Count: 306,055

County Percentage: 82.8%

## Audit Summary and Proposal for Further Use
As you can see, with our script we can pull rich insights from simple election data. Using just two insights from a csv file (county and candidate choice) we can analyze the captured data to show trends like which counties are most active in voter participation for this congressional race. This can be used for any election that captures the same data fields by simply modifying the script to point to other data set files. 

Knowing where the highest turnout is predicted to be for state elections based on past turnout will be useful not only for election commissions managing logistics but also to political groups strategizing their campaigns. We can alter the script to show similar insights between voting districts within a city or state by tweaking the script to list district votes instead of county votes. If more data is captured, for example party affiliation, we could also add to the script to break down party turnout similar to how we outlined county turnout. This would also be valuable information for any persons or entities involved in election strategy. 

