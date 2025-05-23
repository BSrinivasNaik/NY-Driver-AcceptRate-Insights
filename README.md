# Driver AcceptRate Insights

## Tech Stack
- **Frontend**: React.js with Bootstrap for styling
- **Data Visualization**: Recharts for interactive charts
- **Data Processing**: Python scripts for data analysis and conversion

## Summary of Analysis
This project analyzes the conversion rates of search tries to driver quotes in a ride-sharing service. It visualizes data across different dimensions such as hour of day, distance, fare, and pickup distance. The analysis helps identify patterns and insights that can improve driver acceptance rates and optimize service efficiency. 

## Vibe- Tried CursorAI for Quick Data Visualisation and Analysis:
Data: Chennai Auto DAR Analysis for yesterday
[Highlighted Learnings Below]
(1) Data Retrieval: Fetched Data using direct CKH CLI
(2) Data Pre-processing: Cleaning + Understanding Data with Python scripts
- Cleaning = GMT to IST conversion, etc
- Why Understanding Data as a pre-exercise?
   - Working with Cursor AI in past week, i felt that its quick at creating file structure and full-stack code(HTML + CSS + React.js/Python Server, React Native based apps)
   - But its bad at understanding Data Context. Hence, an initial data understanding exercise alongside AI helped for context setting. [LEARNING]
- Converted csv data to json for React app to smoothly integrate
(3) Core React App:
- Cursor AI generally creates files with bad referencing of variables and libraries => Gets itself into circular referencing, duplicate referencing, etc. Fixing this with some initial commands helps in quickly moving Frwd. [LEARNING]
- Giving it direction of the analysis i am looking for, helped CursorAI make clean and readable React Components accordingly: eg- dimentional Analysis on Hourly, Distance, Fare, PickupDistance [LEARNING]
(4) Best Part is, Cursor AI gave me suggestions for further potential hypothesis and insights by itself: [:raised_hands: to AI team-mate]
- Key Insights You Can Derive
   - Time periods when driver availability is low (low conversion rates)
   - Trip distances that drivers prefer or avoid
   - Fare ranges that attract more driver quotes
   - Pickup distance thresholds beyond which driver acceptance drops
   - Overall patterns in search try to quote conversion
(5) Making this initial dashboard along with Data Fetching, Cleaning and iterative prompting to setup Webapp from scratch took ~1.5 hrs, but now adding data for more days, other stages of funnel (RAR, BCR, Overall CVR is super easy and scalable. [LEARNING]
- Data Insights derived:
   - From the Visualisations it is clear insight that- all throughout the the day-time: trip distance was high and stable, but pickup distance went up during peak periods.
   - Despite higher demand for low-distance trips, DAR for high base-fare searches was higher, indicating a slight demand-supply mismatch. Here, greater adoption of Tip, Driver Addn & Dynamic Pricing can help.
PS: Meme credits go to  Supermeme.ai :grimacing: 