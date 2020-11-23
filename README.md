# Surfs_Up

## Overview of the analysis: Explain the purpose of this analysis.
  After using precipitation, location, and other data points related to the islands of Hawaii and their weather we determined Oahu was the best location for W Avy to open his surf and ice cream shop. W Avy wanted to be completely sure his business would be sustainable year round so he asked us to compare weather data for  middle of summer and mid winter seasons to make sure the weather to contribute to the demand for ice cream at his surf shop would be year round. 




## Results:
For the results section we will cover the tools we use for the analyais, how we used the tools and what we discovered through our analysis.

### Tools we would use:
- SQLAlchemy - to access the data and perform queries for our data.
- Jupyter Notebook 
- Pandas and Numpy

![Dependencies](https://github.com/austink24/Surfs_Up/blob/main/Dependencies.png)

### How we did it:
**First:** we had to connect to the datasource containing all the weather data from stations located at numerous locations around the islands of Hawaii. **Second:** we then needed to filter our data to only contain data for the two time frames we wanted to compare, for this example we chose the month of June and that month of December. **Next:** After querying and filtering the data we extracted it to a dataframe so we could run analysis on it. **Finaly:** once we had our data filtered down to just what we needed and extracted into a dataframe we would run summary statistics, showing us the number of samples taken, the Highest temperature, Lowest tempuraturee and the average temperature using python module Numpy. 

#### June Query with filter:
![Filter](https://github.com/austink24/Surfs_Up/blob/main/Filter1.png)

### What we discovered:
We discovered the weather only varies only slighty throughout the year and they temperature is ideal for ice cream sales and surfing year round.

![Weather](https://github.com/austink24/Surfs_Up/blob/main/JUNE_DEC.png)


## Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
So through our analysis of the filtered weather data we have confirmed that the Island od Oahu is the ideal spot for W Avy to open his Ice Cream and Surf Shop. The weather is warm and tropical year round, the average temperature only varying about 3 degress from the peek summer months to the winter month of December. 

### Additional Recommend Queries:

**1st** I would recommend running a query  for the warmest months of the year, this would give use target months for when we could anticpate more sales of ice cream.

**2nd** I woud recommend queying the data to determing the months with the highest precipitations as these months would have limited sales for Ice Cream regardless of the temperatures. 



