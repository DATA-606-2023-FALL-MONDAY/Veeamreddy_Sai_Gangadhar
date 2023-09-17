## 1. Title and Author

**Project Title:** Retail Business Data Analytics using Machine Learning Algorithms

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:** Sai Gangadhar Veeramreddy

**GitHub:** https://github.com/SaiGangadharVeeramreddy

**LinkedIn:** https://www.linkedin.com/in/sai-gangadhar-veeramreddy-160511168/ 

**PowerPoint presentation file:**

**Link to your YouTube video:** 

## 2. Background

**What is the Project about?**

This project is all about using data to help retail businesses make better decisions. The primary objective of this project is to offer a comprehensive understanding of the retail landscape, enabling businesses to make data-driven decisions that enhance their operations, boost profitability, and ultimately enrich the customer experience. By doing this, we can discover important trends and patterns that can help stores improve their operations, make more money, and give customers a better shopping experience. In the end, the goal is to give retailers the tools they need to succeed in a competitive market by using data in smart ways. 

**Why does it matter?**

It matters because it can make stores more successful and customers happier. When stores use data to make decisions, they can sell things better and not waste money on stuff people don't want. This helps stores stay in business and keep prices reasonable. It also means shoppers can find what they need and maybe even get good deals. So, using data is like a win-win for stores and customers—it helps everyone.

**What are your research questions?**

- **Sales Prediction:**
Can we use the information about store location, temperature, fuel prices, and special holiday weeks to predict how much a store will sell in a given week? This could help stores plan better.

- **Markdown Impact Analysis:**
Do discounts and promotional markdowns have a big effect on sales? We can investigate if offering discounts during certain weeks leads to increased sales.

- **Store Clustering:**
Can we group similar stores together based on their sales history and the features like location and economic conditions? This might help stores understand their competition and market better.

- **Holiday Sales Assessment:**
Does having a special holiday week significantly change sales patterns? We can examine if stores should prepare differently for these weeks in terms of stocking and staffing.

## 3. Data 

**Describe the datasets you are using to answer your research questions:**
The data is about a retail business that occurred in 45 different stores from 2010 to 2013. There are three separate CSV files in the dataset, each containing information about sales, store features, and store details. When we combine these datasets by matching shared columns, we create a final dataset. This final dataset allows us to analyze sales in relation to factors like store location, holidays, and store size. 

**Data sources:**
The data set is available at https://www.kaggle.com/datasets/manjeetsingh/retaildataset?select=stores+data-set.csv


### Features dataset

**Data Size:** 587 kb

**Data shape:** 8190 rows * 12 Columns

**Time Period:** 2010 to 2013

**What does each rwo represent?**
Each row of the dataset represents the details of prices of fuel, markdown1, markdown2, markdown3, markdown4, markdown5 for a particular date and its temperature along with consumer price index, unemployement. Along with these details it is also has information stating weather that particular date falls into any holiday week.

**Data dictionary:**

- **Store**

   - Data type : Numerical
   
   - Defition : the Store Number
   
   - Potential values : 1 to 45
   
- **Date**

   - Data type : Timestamp
   
   - Defition : the date
   
   - Potential values : xx/xx/20(10-13)
   
- **Temperature**

   - Data type : Numerical
   
   - Defition : Average temperature in the store region
   
   - Potential values : -7.29 F to 101.95 F

- **Fuel Price**

   - Data type : Numerical
   
   - Defition : Average temperature in the store region
   
   - Potential values : 2.472 per galon to 4.468 per galon
   
- **Markdown1** , **Markdown2** , **Markdwon3** , **Markdown4** , **Markdown5**

   - Data type : Numerical
   
   - Defition : promotional markdowns
   
   - Potential values : only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA
   
- **CPI**

   - Data type : Numerical
   
   - Defition : the coustmer price Index
   
   - Potential values : 126.064 to 228.976 with missing values marked as NA

- **Unemployment**

   - Data type : Numerical
   
   - Defition : the unemployement rate
   
   - Potential values : 3.684 to 14.313 with missing values marked as NA
   
- **Isholiday**

   - Data type : Boolean
   
   - Defition : whether the week is a special holiday week
   
   - Potential values : True / False
   

### Sales dataset

**Data Size:** 12.65 mb

**Data shape:** 4,21,571 rows * 5 Columns

**Time Period:** 2010 to 2013

**What does each rwo represent?**

Each row of the dataset represents the details of weekly sales at each store with respect to different departments. Along with these details, it is also has information stating weather that particular date falls into any holiday week.

**Data dictionary:**

- **Store**

   - Data type : Numerical
   
   - Defition : the Store Number
   
   - Potential values : 1 to 45
   
- **Dept**

   - Data type : Numerical
   
   - Defition : the department Number
   
   - Potential values : 1 to 99

- **Date**

   - Data type : Timestamp
   
   - Defition : the date
   
   - Potential values : xx/xx/20(10-13)

- **weekly_Sales**

   - Data type : Numerical
   
   - Defition : sales for the given department in the given store
   
   - Potential values : -863 to 1,96,810.42
   
- **Isholiday**

   - Data type : Boolean
   
   - Defition : whether the week is a special holiday week
   
   - Potential values : True / False
   

### Stores dataset

**Data Size:** 1 kb

**Data shape:** 45 rows * 3 Columns

**Time Period:** 2010 to 2013

**What does each rwo represent?**
Each row of the dataset represents the details of each store with its type and size of the store.

**Data dictionary:**

- **Store**

   - Data type : Numerical
   
   - Defition : the Store Number
   
   - Potential values : 1 to 45
   
- **type**

   - Data type : Categorical
   
   - Defition : the type of the store
   
   - Potential values : A / B / C

- **Size**

   - Data type : Numerical
   
   - Defition : the size of the store
   
   - Potential values : 34,875 sq.ft to 2,19,622
   
**Which variable/column will be your target/label in your ML model?**
- Store Number
- Isholiday
- Temperature
- Fuel_Price
- CPI
- Unemployment rate
- type of store
- size of store

**Which variables/columns may be selected as features/predictors for your ML models?**
- Weekly_Sales
- Departmental_Sales
