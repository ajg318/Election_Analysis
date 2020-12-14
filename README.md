# Election_Analysis


## Overview of Project

### Purpose

The purpose of this code is to compile and display the election results. The raw data of the election is held in a csv and consisted of the Ballot ID, County, and Candidate the vote is for. This code is able to how many votes were for each candidate and county. 

## Election Audit

* There were 369,711 total votes in this election
* The breakdown of the votes by county is the following:
    * Jefferson - 38,555 votes (10.5%)
    * Denver - 306,055 votes (82.8%)
    * Arapahoe - 24,801 votes (6.7%)
* Denver had the most votes of the counties
* The breakdown of votes for each candidate are:
    * Charles Casper Stockham - 85,213 votes (23.0%)
    * Diana DeGette: 272,892 votes (73.8%)
    Raymon Anthony Doane: 11,606 votes (3.1%)
Diana DeGette had the most votes and won with 272,892 votes and 73.8%

The full breakdown is below:

![ElectionBreakdown](https://github.com/ajg318/Election_Analysis/tree/main/resources/terminaloutput.png)

    
    ### Analysis of Outcomes Based on Launch Date

### Election Audit Summary

The script can work on any election because it finds the candidates within the csv and makes them into the array (it is not hardcoded):

```
 for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

```

The code can find all the candidates, as long they are in the third column. The code can be modified to see which column "Candidate" is in the header, use that index, then loop through that column.

Another modification is being able to read the csv anywhere and not just locally. This will allow for easier access to the votes.

### Challenges and Difficulties Encountered

## Results


