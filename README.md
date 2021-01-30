# Data Analytics Projects

A portfolio of various projects I've worked on for fun! Written in Python. 

## Machine Learning

- #### **Applied Machine Learning on Public Real Estate in Singapore**
  - **Link:** [Github](timeseries/forecasting_household_electricity_SARIMA.ipynb) [nbviewer](https://nbviewer.jupyter.org/github/zachary-tang/Data-Analytics-Projects/blob/main/timeseries/forecasting_household_electricity_SARIMA.ipynb)
  - **Description:** Trained and compared machine learning models to predict house prices. Examined the price premium effect of geographical features
  - **Date Uploaded:** 29/01/2021
  - **Data Sources:**
    - Data.gov.sg: [Resale Flat Prices](https://data.gov.sg/dataset/resale-flat-prices), [Location of Parks](https://data.gov.sg/dataset/parks), [Location of Child Care Centres](https://data.gov.sg/dataset/listing-of-centres), [List of Community Clubs](https://data.gov.sg/dataset/community-clubs), [Location of Government Hawkers](https://data.gov.sg/dataset/list-of-government-markets-hawker-centres), [Location of NEA Licensed Food Stalls](https://data.gov.sg/dataset/list-of-nea-licensed-eating-establishments-with-grades-demerit-points-and-suspension-history), [Location of Supermarkets](https://data.gov.sg/dataset/listing-of-licensed-supermarkets)
    - APIs: [OneMap API](https://docs.onemap.sg), [LTA DataMall](https://datamall.lta.gov.sg/content/datamall/en.html)
    - Healthhub: [List of Facilities](https://www.healthhub.sg/directory/clinics-and-polyclinics)
    - Wikipedia: [List of MRT Stations](https://en.wikipedia.org/wiki/List_of_Singapore_MRT_stations), [List of Bus Stations](https://en.wikipedia.org/wiki/List_of_bus_stations_in_Singapore), [List of Shopping Centres](https://en.wikipedia.org/wiki/List_of_shopping_malls_in_Singapore), [List of Primary Schools](https://en.wikipedia.org/wiki/List_of_primary_schools_in_Singapore), [List of Secondary Schools](https://en.wikipedia.org/wiki/List_of_primary_schools_in_Singapore), [List of Junior Colleges](https://en.wikipedia.org/wiki/Category:Junior_colleges_in_Singapore)

## Time Series Analysis

- #### **Forecasting Household Electricity Consumption in Singapore with SARIMA**
  - **Link:** [Github](timeseries/forecasting_household_electricity_SARIMA.ipynb) [nbviewer](https://nbviewer.jupyter.org/github/zachary-tang/Data-Analytics-Projects/blob/main/timeseries/forecasting_household_electricity_SARIMA.ipynb)
  - **Description:** Fitted a SARIMA model to forecast monthly household electricity consumption in Singapore
  - **Date Uploaded:** 10/01/2021
  - **Data Source:** [Total Household Electricity Consumption by Dwelling Type](https://data.gov.sg/dataset/total-household-electricity-consumption-by-dwelling-type)

## Webscrapers
  
- #### **Shopee Search and Reviews Webscraper**
  - **Link:** [Github](webscrapers/webscraper_shopee_search_and_reviews.ipynb) [nbviewer](https://nbviewer.jupyter.org/github/zachary-tang/Data-Analytics-Projects/blob/main/webscrapers/webscraper_shopee_search_and_reviews.ipynb)
  - **Description:** Scrapes the search results of a user specified search term in Shopee. **Optional:** loop through each listing in search results to pull additional information about the seller, the product and customer reviews.
  - **Date Uploaded:** 13/01/2021
  - **Scrape Variables:** ``product_name``, ``urls``, ``prices_lowest``, ``prices_highest``, ``discounts``, ``sold_per_month``, ``preferred``, ``country_ship``, ``ad``, ``num_sold``, ``num_ratings``, ``num_fav``, ``num_stock``, ``seller_name``, ``seller_url``, ``seller_products``, ``seller_ratings``, ``seller_response``, ``seller_response_time``, ``seller_joined``, ``seller_follower``, ``product_cat``, ``product_desc``, ``date``, ``username``, ``comment``, ``variation``
  - **Output:** .csv
  - **Data Source:** [shopee.sg](https://www.shopee.sg)
  
- #### **Shopee Reviews Webscraper**
  - **Link:** [Github](webscrapers/webscraper_shopee_reviews.ipynb) [nbviewer](https://nbviewer.jupyter.org/github/zachary-tang/Data-Analytics-Projects/blob/main/webscrapers/webscraper_shopee_reviews.ipynb)
  - **Description:** Scrapes reviews off a certain listing in Shopee
  - **Date Uploaded:** 10/01/2021
  - **Scrape Variables:** ``date``, ``username``, ``comment``, ``variation``
  - **Output:** .csv
  - **Data Source:** [shopee.sg](https://www.shopee.sg)
  
## Contact Information

- [Email](mailto:zacharytangjiaying@gmail.com)
- [Linkedin](https://www.linkedin.com/in/zacharytang/)
