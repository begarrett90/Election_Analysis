# Election_Analysis

## Project Overview
Complete an election audit for a recent local congressional election in Colorado. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calulate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 
6. Calculate the voter turnout for each county.
7. Caluclate the percenter of votes from each county.
8. Determine the county with the highest voter turnout.

## Resource
Data Source: election_results.csv

Software: Python, Visual Studio Code

## Summary
The analysis of the election shows that:
### Total Votes:
- There were 369,711 votes cast in the election
### Candidate Breakdown:
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The results were:
  - Charles Casper Stockham received 23% of the cote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.
### County Breakdown:
- Jefferson County had 38,855 voters which casted 10.5% of the votes.
- Denver County had 306,055 voters which casted 82.8% of the votes.
- Arapahoe County had 24,801 voters which casted 6.7% of the votes.
- **Denver** had the largest county turnout. 

### Complete Breakdown:
<img width="246" alt="2022-06-18" src="https://user-images.githubusercontent.com/105942622/174449370-96cc9aab-d42a-4ae9-a91a-eebfa3745765.png">

## Election Audit Summary:
In the future this script can be used for future elections to automatically:
- find candidate names
- find counties
- count votes and percentages for candidates and counties
- delcare a winner for the election
- show turnout percentages for the counties. 

The ability to see the turnout percentages for counties will provide infomation that will allow campaigns to focus on areas that did not have a high turnout volume to try and capture the votes of those areas. An area to further develop this code would be to breakdown the candidate performance within each county. 

This script not only has the capability to handle local congressional elections, but other elections on a larger scale including national elections, with thw minor adjustments of "counties" to "states" to accurately represent the data. 
