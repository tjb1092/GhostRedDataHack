## Inspiration

Our Application attempts to utilize several technologies to query, analyze and visualize data from an industrial virtual network in order to try and find predictors for device failure. After performing some data exploration in Tableau, we were able to notice strong correlations between high CPU usage and disk throughputs as well as network throughput. Our hypothesis was that CPU and memory utilization relative to allocated values would be good predictors of abnormal operating conditions. Since the dataset did not contain any information about actual incidents that we could use to train a supervised model, we decided that this was a good way to located any over or under-utilized devices that could be further studied. 

## What it does

In order to test our hypothesis, multiple linear regression was used via Python’s Scikit-learn regression library and Pandas DataFrame structures to format the time-series data. The data was supplied by a given Sqlite3 database, which was queried by Python using SQL to join the relational schema together. 

We decided to group regression tests by “business” operation because we assumed that similar businesses have similar traffic and disk throughput requirements. 

Using the generated correlation coefficients, we used the normalized predictors of CPU and memory usage to generate an average “Health Score” per device. This data would be used as a thresholding filter to alert the end-user to investigate into a potentially over-utilized machine.
Health Score metrics per device and average health score per business were to be pushed up to a UI Bootstrap Front-End so that end-users could easily see and investigate into the data. This UI was developed using the open-source Light Bootstrap Admin Dashboard template as a baseline. The CSS, Javascript, and HTML were changed dramatically from this starting point in order to create the desired visualizations of our data. It allows users to identify businesses that have abnormally large amounts of “at risk” devices so that they can be investigated. The second feature would allow the user to drill down to the device level to inspect the performance metrics feeding into our predictive model to decide if more resources should be allocated to that node.

## Challenges We ran into
Attempts were made at constructing a Django webserver to act as a Back-End interface between our Python analytics and UI, but lack of time and experience in this area prevented this link of the data pipeline from being completed. 
## Accomplishments that I'm proud of

Two members (Jacob and John) of our team were able to completely teach themselves python and use it to perform our data analytics. 

Tony was able to create a great looking visualization from little experience. 
