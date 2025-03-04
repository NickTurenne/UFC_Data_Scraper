import requests as rq
import json
from bs4 import BeautifulSoup as bs

# DESC: Retrieve fight info from a matchup from ufcstats.com
# Preconditions: Valid link to matchup
# Postconditions: 2D array of fighter stats, element 1 corresponding to the first fighter
def GetFighterStats(link:str):
    r = rq.get(link)
    soup = bs(r.text, 'html.parser')
    fighterInfo = soup.find('table', {'class' : 'b-fight-details__table'})
    rows = fighterInfo.find('tr').find_all('a')
    names = []
    for row in rows:
        names.append(row.text.strip())

    statsRows = soup.find_all('tr', {'class' : 'b-fight-details__table-row-preview'})
    infoFighter1 = []
    infoFighter1.append(names[0])
    infoFighter2 = []
    infoFighter2.append(names[1])
    for i in range(15):
        subRows = statsRows[i].find_all('p', {'class' : 'b-fight-details__table-text'})
        infoFighter1.append(subRows[1].text.strip())
        infoFighter2.append(subRows[2].text.strip())
    return [infoFighter1, infoFighter2]

# DESC: Retrieve list of all fight info for main matchups in upcoming UFC events from ufcstats.com
# Preconditions: internet connection
# Postconditions: an array contiaining the fight title, and then all matchup fighter details
def GetEventMatchupDetails():
    # 1. Get the link to most recent event from ufcstats.com
    r = rq.get('http://ufcstats.com/statistics/events/upcoming')
    soup = bs(r.text, 'html.parser')
    rows = soup.find('table', {'class' : 'b-statistics__table-events'}).find('tbody').find_all('tr')
    top = rows[1]
    link = top.find('td').find('a').get('href')

    # 2. Get the fighter matchup links from the main event (will probably want this to be for all fights)
    r = rq.get(link)
    soup = bs(r.text, 'html.parser')
    title = soup.find('span', {'class' : 'b-content__title-highlight'}).text.strip()
    rowsTest = soup.find('table', {'class' : 'b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table'}).find('tbody').find_all('tr')
    matchupLinks = []
    for row in rowsTest:
        subRows = row.find_all('td')
        matchupLinks.append(subRows[4].find('a').get('data-link'))

    eventInfo = [title]
    for link in matchupLinks:
        eventInfo.append(GetFighterStats(link))

    return eventInfo

def main():
    info = GetEventMatchupDetails()
    with open("eventInfo.json", "w") as file:
        json.dump(info, file)

if __name__ == "__main__":
    main()