# Mark-and-SpencersRetail-Analytic-Project

Retail Analytics Dataset Creation – Marks & Spencer–Style Synthetic Data

Author: Sohail Shaik 

Date:  09/08/2025 6:54 pm 

Role: Data Analyst / Data Engineer
 
Executive Summary
Modern retail analytics demands the ability to work with large, complex, and interconnected datasets that reflect real-world business operations. However, proprietary retail data is often inaccessible due to confidentiality restrictions.
To bridge this gap, I designed and engineered a realistic, large-scale synthetic dataset modelled after the data structures and reporting needs of major UK retailers, particularly Marks & Spencer.
This dataset is not a random assortment of numbers — it was strategically modelled to simulate actual retail workflows, transactions, inventory movements, and customer behaviour patterns. It provides an end-to-end playground for data analysis, business intelligence, and advanced analytics.
The project showcases my ability to:
•	Design relational data models from scratch.
•	Engineer and automate dataset generation using Python.
•	Simulate business logic and realistic operational constraints.
•	Create a dataset that supports realistic analytics for decision-making.
 
Project Objectives
1.	Replicate Real Retail Complexity – Create a multi-table dataset that reflects the depth of actual retail operations, from products to customers to store inventory.
2.	Enable Advanced Analytics Practice – Design a dataset large enough for meaningful statistical analysis, BI dashboards, and SQL queries.
3.	Demonstrate Technical Capability – Showcase proficiency in Python, pandas, Faker, and relational modeling to potential employers.
4.	Maintain Ethical Transparency – Ensure all data is 100% synthetic, protecting privacy while retaining business realism.
 
Dataset Overview
The final dataset consists of eight interrelated CSV files, designed in 3NF (Third Normal Form) to reflect typical retail database structures.
Table Name	Rows	Description
products.csv	1,000	Product catalog with SKU, category, subcategory, and price.
customers.csv	10,000	Customer demographics including name, gender, location, and loyalty tier.
stores.csv	25	Store list with location and region details.
transactions.csv	13,000	High-level transaction data with timestamps, customer ID, and store ID.
transaction_line_items.csv	~130,000	Detailed product-level purchase data for each transaction.
returns.csv	~2,000	Returned items with reason codes and dates.
inventory_snapshots_30days.csv	750,000+	Daily stock levels per product per store over a 30-day period.
reviews.csv	5,000+	Customer product reviews and star ratings.
summary_counts.csv	1	Metadata summarizing dataset size.
 
Code & Methodology
The dataset was generated using Python 3.10 and the following libraries:
•	pandas – Data manipulation and CSV export.
•	numpy – Randomized numerical distributions.
•	faker – Realistic fake customer, location, and text generation.
•	random – Simulating purchase frequencies, basket sizes, and return probabilities.
•	datetime – Generating realistic transaction timelines.
Step-by-Step Process
1.	Schema Design
Defined entities and relationships:
o	Customers → Transactions → Transaction Items → Products
o	Stores → Inventory Snapshots
o	Products → Reviews / Returns
2.	Master Data Generation
o	Created products.csv with realistic category hierarchies (e.g., Clothing > Men’s Shirts).
o	Generated customers.csv with demographic spread and loyalty tiers.
o	Assigned 25 UK store locations.
3.	Transaction Simulation
o	Distributed purchases across a one-year period.
o	Applied random basket sizes (1–10 items) per transaction.
o	Linked customers to stores to mimic regional purchasing behavior.
4.	Inventory Simulation
o	Set starting stock levels per product per store.
o	Decremented stock based on simulated purchases and replenishments.
o	Created daily inventory snapshots for 30 days.
5.	Returns & Reviews
o	Randomly selected ~15% of transactions for returns, weighted by product type.
o	Generated short review texts and ratings using sentiment-weighted randomness.
6.	Export & Validation
o	Saved each table to CSV.
o	Checked for relational integrity (no orphan foreign keys).
o	Ensured data realism (e.g., no negative prices, valid dates).
 
Example Analytics Applications
This dataset supports a wide range of retail analytics tasks:
•	Sales Performance Analysis – Store-by-store revenue tracking.
•	Customer Segmentation – RFM scoring and loyalty program targeting.
•	Market Basket Analysis – Product bundling and cross-sell opportunities.
•	Inventory Optimisation – Stockout prediction and replenishment planning.
•	Return Rate Analysis – Identifying problematic products.
•	Sentiment Analysis – Linking customer reviews to purchase behaviour.
 
Skills Demonstrated
•	Data Modelling: Translating business processes into normalised relational tables.
•	Data Engineering: Automating dataset generation with Python and Faker.
•	Analytical Thinking: Embedding realistic business rules into synthetic data.
•	Data Quality Assurance: Implementing validation checks for logical consistency.
•	Communication: Documenting process and explaining technical work clearly.
 
Key Takeaways
This project demonstrates the ability to work independently from data creation to an analysis-ready format, simulating real-world scenarios that analysts encounter in the retail sector.
It’s not just about making charts — it’s about understanding the business process, designing the right data structure, and delivering a usable, realistic dataset for decision-making.

https://sdmntprnortheu.oaiusercontent.com/files/00000000-3f18-61f4-b947-733475d5c569/raw?se=2025-08-09T19%3A04%3A14Z&sp=r&sv=2024-08-04&sr=b&scid=9b0e9c2b-6e4a-5f1d-94ef-38022bce6c73&skoid=b32d65cd-c8f1-46fb-90df-c208671889d4&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-08-09T16%3A50%3A28Z&ske=2025-08-10T16%3A50%3A28Z&sks=b&skv=2024-08-04&sig=HtYjJhxpIWv5EkiX%2BLi21mEn7Y0BMTUmZlAQ%2BtxTRBc%3D<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3d31b04e-7235-4f61-ab42-9c752c1bc7b1" />


