# UFC Fighter Matchup Scraper 
A Python-based web scraper that extracts fighter statistics for main card matchups from UFCStats.com for upcoming events for comparison and analysis.
This project utilizes the BeautifulSoup library to scrape fight matchup info for the next upcoming UFC event. 

# Instructions
1. Run the UFC_next_event_scraper.py to generate the json file with all the event and fighter info.
2. Run the Event_Data_Visualizer.py to generate the visualized fight data for the main matchup (You can also add an integer argument to the main to index other fights, starting at index 1 for the main event)

# Libraries
- BeautifulSoup
- requests
- json
- sys
- pandas
- matplotlib
