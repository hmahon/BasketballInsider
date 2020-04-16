
"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function
import random
import feedparser  
import json
import boto3
import pickle
from datetime import datetime
import re
import bs4 as bs       
import requests
#import pandas_datareader.data as web   #2/17: dont think i need this



# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    
    # this is the only title that matters as of 1/10/20
    card_title = 'News Around the League'
    
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': card_title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_recent_news_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = 'News Around the League'
    
    
    NewsFeed = feedparser.parse("http://premium.rotoworld.com/rss/feed.aspx?sport=nba&ftype=news&count=12&format=rss")   
    entries = NewsFeed.entries[0:5]
    news_list = []
    for entry in entries:
        news = entry.title
        news = news.replace('OT ', 'overtime ')
        news = news.replace('Mon ', 'Monday ')
        news = news.replace('Tues ', 'Tuesday ')
        news = news.replace('Weds ', 'Wednesday ')
        news = news.replace('Thurs ', 'Thursday ')
        news = news.replace('Fri ', 'Friday ')
        news = news.replace('Sat ', 'Saturday ')
        news = news.replace('Sun ', 'Sunday ')
        news = news.replace('?', '')
        news = news.replace('Justise', 'Justice')
        news = news.replace('re-signed', 're signed')
        news = news.replace('/', ', ')
        news = news.replace('ATL ', 'Atlanta ')
        news = news.replace('BKN ', 'Brooklyn ')
        news = news.replace('BOS ', 'Boston ')
        news = news.replace('CHA ', 'Charlotte ')
        news = news.replace('CHI ', 'Chicago ')
        news = news.replace('CLE ', 'Cleveland ')
        news = news.replace('DAL ', 'Dallas ')
        news = news.replace('DEN ', 'Denver ')
        news = news.replace('DET ', 'Detroit ')
        news = news.replace('GSW ', 'Golden ')
        news = news.replace('HOU ', 'Houston ')
        news = news.replace('IND ', 'Indiana ')
        news = news.replace('LAC ', 'LA Clippers ')
        news = news.replace('LAL ', 'LA Lakers ')
        news = news.replace('MEM ', 'Memphis ')
        news = news.replace('MIA ', 'Miami ')
        news = news.replace('MIL ', 'Milwaukee ')
        news = news.replace('MIN ', 'Minnesota ')
        news = news.replace('NOP ', 'New Orleans ')
        news = news.replace('NYK ', 'New York ')
        news = news.replace('OKC ', 'Oklahoma City ')
        news = news.replace('ORL ', 'Orlando ')
        news = news.replace('PHI ', 'Philadelphia ')
        news = news.replace('PHX ', 'Phoenix ')
        news = news.replace('POR ', 'Portland ')
        news = news.replace('SAC ', 'Sacramento ')
        news = news.replace('SAS ', 'San Antonio ')
        news = news.replace('TOR ', 'Toronto ')
        news = news.replace('UTA ', 'Utah ')
        news = news.replace('WAS ', 'Washington ')
        news = news.replace('LA ', 'Washington ')
        news = news.replace('GTD', 'game time decision')
        news = news.split(' - ',2)[0]
        news_list.append(news)
    
    str1 = "...." 
    news_list = str1.join(news_list) 
    
#    news_list = ["NBA stands for National Basketball League. ", 
#         "This game is great"  	]
 

    speech_output = news_list #random.choice(news_list)
    reprompt_text = "Want news on a specific player? Say.. 'whats the news on Lebron James' for instance.. Or else say quit"
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# originally used Amazon.Athlete to define the slot. now using custom slot i populated
def get_player_news_response(player_name):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = 'News Around the League'
    
    NewsFeed = feedparser.parse("http://premium.rotoworld.com/rss/feed.aspx?sport=nba&ftype=news&count=12&format=rss")   
    entries = NewsFeed.entries[0:100]

    player_dict = {}
    entries = NewsFeed.entries[0:100]
    for entry in entries:
        news = entry.title 
        news = news.replace('OT ', 'overtime ')
        news = news.replace('Mon ', 'Monday ')
        news = news.replace('Tues ', 'Tuesday ')
        news = news.replace('Weds ', 'Wednesday ')
        news = news.replace('Thurs ', 'Thursday ')
        news = news.replace('Fri ', 'Friday ')
        news = news.replace('Sat ', 'Saturday ')
        news = news.replace('Sun ', 'Sunday ')
        news = news.replace('?', '')
        news = news.replace('Justise', 'Justice')
        news = news.replace('re-signed', 're signed')
        news = news.replace('/', ', ')
        news = news.replace('ATL ', 'Atlanta ')
        news = news.replace('BKN ', 'Brooklyn ')
        news = news.replace('BOS ', 'Boston ')
        news = news.replace('CHA ', 'Charlotte ')
        news = news.replace('CHI ', 'Chicago ')
        news = news.replace('CLE ', 'Cleveland ')
        news = news.replace('DAL ', 'Dallas ')
        news = news.replace('DEN ', 'Denver ')
        news = news.replace('DET ', 'Detroit ')
        news = news.replace('GSW ', 'Golden ')
        news = news.replace('HOU ', 'Houston ')
        news = news.replace('IND ', 'Indiana ')
        news = news.replace('LAC ', 'LA Clippers ')
        news = news.replace('LAL ', 'LA Lakers ')
        news = news.replace('MEM ', 'Memphis ')
        news = news.replace('MIA ', 'Miami ')
        news = news.replace('MIL ', 'Milwaukee ')
        news = news.replace('MIN ', 'Minnesota ')
        news = news.replace('NOP ', 'New Orleans ')
        news = news.replace('NYK ', 'New York ')
        news = news.replace('OKC ', 'Oklahoma City ')
        news = news.replace('ORL ', 'Orlando ')
        news = news.replace('PHI ', 'Philadelphia ')
        news = news.replace('PHX ', 'Phoenix ')
        news = news.replace('POR ', 'Portland ')
        news = news.replace('SAC ', 'Sacramento ')
        news = news.replace('SAS ', 'San Antonio ')
        news = news.replace('TOR ', 'Toronto ')
        news = news.replace('UTA ', 'Utah ')
        news = news.replace('WAS ', 'Washington ')
        news = news.replace('LA ', 'Washington ')
        news = news.replace('GTD', 'game time decision')
        text = news.split('|',2)[0]
        name = text.split()[-2:]
        str1 = " " 
        name = str1.join(name)
        text = text.split(' - ',2)[0]
        
        # Keeping the date the roto update was made for future work
        player_dict[name] = {entry.updated: text} 
    
    # Loading original dictionary from s3 bucket
    bucketname = 'nba-dict'
    filename = 'nba_dict.p'
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = bucketname, Key=filename)
    file_content = fileObj["Body"].read()
    player_dict_original = pickle.loads(file_content)
    
    for key in player_dict.keys():
        if key in [*player_dict_original]:
            player_dict_original[key].update(player_dict[key])
        else:
            player_dict_original[key] = player_dict[key]
 
    player = player_name
    player = player.title()
    
    #Hardcoding some player replacements
    
    if player == 'Zion':
        player = 'Zion Williamson'
    elif player == 'Giannis':
        player = 'Giannis Antetokounmpo'
    elif player == 'LeBron':
        player = 'LeBron James'
    elif player == 'Lebron':
        player = 'LeBron James'
    elif player == 'Lebron James':
        player = 'LeBron James'
    elif player == 'Carmelo':
        player = 'Carmelo Anthony'
    elif player == 'DJ Augustin':
        player = 'D.J. Augustin'
    elif player == 'Dj Augustin':
        player = 'D.J. Augustin'
    elif player == 'Michael Porter Junior':    
        player = 'Porter Jr.'
    else: 
        player = player
        
    
    print('final player retrieved as: ', player)
    
    # card_title = "player entered as: {}".format(player)

    
    if player in player_dict_original:
        speech_output_list = []
        for date in sorted(player_dict_original[player].keys(), reverse=True)[:3]:
            news = player_dict_original[player][date]
            month = date[5:7]
            month = month.replace('01', 'January')
            month = month.replace('02', 'February')
            month = month.replace('03', 'March')
            month = month.replace('04', 'April')
            month = month.replace('05', 'May')
            month = month.replace('06', 'June')
            month = month.replace('07', 'July')
            month = month.replace('08', 'August')
            month = month.replace('09', 'September')
            month = month.replace('10', 'October')
            month = month.replace('11', 'November')
            month = month.replace('12', 'December')
            day = date[8:10]     
            if day == '1':
                day = '1st'
            elif day == '2':
                day = '2nd'
            elif day == '3':
                day = '3rd'
            elif day == '4':
                day = '4th'
            elif day == '5':
                day = '5th'
            elif day == '6':
                day = '6th'
            elif day == '7':
                day = '7th'
            elif day == '8':
                day = '8th'
            elif day == '9':
                day = '9th'
            elif day == '10':
                day = '10th'
            elif day == '11':
                day = '11th'
            elif day == '12':
                day = '12th'
            elif day == '13':
                day = '13th'
            elif day == '14':
                day = '14th'
            elif day == '15':
                day = '15th'
            elif day == '16':
                day = '16th'
            elif day == '17':
                day = '17th'
            elif day == '18':
                day = '18th'
            elif day == '19':
                day = '19th'
            elif day == '20':
                day = '20th'
            elif day == '21':
                day = '21st'
            elif day == '22':
                day = '22nd'
            elif day == '23':
                day = '23rd'
            elif day == '24':
                day = '24th'
            elif day == '25':
                day = '25th'
            elif day == '26':
                day = '26th'
            elif day == '27':
                day = '27th'
            elif day == '28':
                day = '28th'
            elif day == '29':
                day = '29th'
            elif day == '30':
                day = '30th'
            elif day == '31':
                day = '31st'              

            speech_output_list.append(month + ' ' + day + ': ' + news)
        str1 = "...." 
        speech_output_list = str1.join(speech_output_list) 
        speech_output = str(speech_output_list)
        
    else: 
        speech_output = 'That player has no recent news. Try someone else'
    
    
    reprompt_text = "Who else would you like news for? For instance, Say.. 'whats the news on James Harden'.. Or else say quit"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def top_dfs_plays():
    print('begin top dfs plays function')
	
    import datetime
    session_attributes = {}
    card_title = 'News Around the League'
    
    ranking_dict = {}
    
    def get_bball_monster():
        resp = requests.get('https://basketballmonster.com', verify=True, timeout=10) 
        print('begin parsing with beautiful soup')
        soup = bs.BeautifulSoup(resp.content, 'html.parser')
        print('complete parsing with Beautiful Soup')		
        table = soup.find('table', {'class': 'datatable w3-hoverable'})
        for row in table.findAll('tr')[1:21]:
            rank = row.findAll('td')[0].text
            player = row.findAll('td')[1].text
            ranking_dict[rank] = player 
        return ranking_dict    
    
    def get_day():
        resp = requests.get('https://basketballmonster.com')
        soup = bs.BeautifulSoup(resp.content, 'html.parser')
        divs = soup.findAll('div', {'class': lambda x: x  and 'clearfix' in x.split()})
        str_divs = str(divs)
        dy = re.split('1 Day ',str_divs)[-1]
        dy = re.split('<', dy)[0]
        dy = dy.replace('(Thu)', 'Thursday')
        return(dy)

    dy = get_day()
    print('Basketball Monster date is:', dy)


    # getting current date and time
    d = datetime.datetime.today()
    tdy = d.strftime('%A')
    
    # find the full date of Basketball Monster Data
    def finding_the_date():
        if dy != tdy:
            bm_dt = datetime.datetime.today() - datetime.timedelta(days=1)
            bm_month = bm_dt.strftime('%B')
            day = bm_dt.strftime('%d')
            """  
            if day == '1':
                day = '1st'
            elif day == '2':
                day = '2nd'
            elif day == '3':
                day = '3rd'
            elif day == '4':
                day = '4th'
            elif day == '5':
                day = '5th'
            elif day == '6':
                day = '6th'
            elif day == '7':
                day = '7th'
            elif day == '8':
                day = '8th'
            elif day == '9':
                day = '9th'
            elif day == '10':
                day = '10th'
            elif day == '11':
                day = '11th'
            elif day == '12':
                day = '12th'
            elif day == '13':
                day = '13th'
            elif day == '14':
                day = '14th'
            elif day == '15':
                day = '15th'
            elif day == '16':
                day = '16th'
            elif day == '17':
                day = '17th'
            elif day == '18':
                day = '18th'
            elif day == '19':
                day = '19th'
            elif day == '20':
                day = '20th'
            elif day == '21':
                day = '21st'
            elif day == '22':
                day = '22nd'
            elif day == '23':
                day = '23rd'
            elif day == '24':
                day = '24th'
            elif day == '25':
                day = '25th'
            elif day == '26':
                day = '26th'
            elif day == '27':
                day = '27th'
            elif day == '28':
                day = '28th'
            elif day == '29':
                day = '29th'
            elif day == '30':
                day = '30th'
            elif day == '31':
                day = '31st'              
            """
            txt = 'Top DFS Plays for ' + dy + ' ' + bm_month + ' ' + day
            return txt
        elif dy == tdy:
            bm_dt = datetime.datetime.today()  
            bm_month = bm_dt.strftime('%B')
            day = bm_dt.strftime('%d')
            """     dont think this is necessary
            if day == '1':
                day = '1st'
            elif day == '2':
                day = '2nd'
            elif day == '3':
                day = '3rd'
            elif day == '4':
                day = '4th'
            elif day == '5':
                day = '5th'
            elif day == '6':
                day = '6th'
            elif day == '7':
                day = '7th'
            elif day == '8':
                day = '8th'
            elif day == '9':
                day = '9th'
            elif day == '10':
                day = '10th'
            elif day == '11':
                day = '11th'
            elif day == '12':
                day = '12th'
            elif day == '13':
                day = '13th'
            elif day == '14':
                day = '14th'
            elif day == '15':
                day = '15th'
            elif day == '16':
                day = '16th'
            elif day == '17':
                day = '17th'
            elif day == '18':
                day = '18th'
            elif day == '19':
                day = '19th'
            elif day == '20':
                day = '20th'
            elif day == '21':
                day = '21st'
            elif day == '22':
                day = '22nd'
            elif day == '23':
                day = '23rd'
            elif day == '24':
                day = '24th'
            elif day == '25':
                day = '25th'
            elif day == '26':
                day = '26th'
            elif day == '27':
                day = '27th'
            elif day == '28':
                day = '28th'
            elif day == '29':
                day = '29th'
            elif day == '30':
                day = '30th'
            elif day == '31':
                day = '31st' 
            """             
            txt = 'Top DFS Plays ' + dy + ' ' + bm_month + ' ' + day
            return txt
        else:
            print('Error')

    
    #### something wrong whewn calling the function it appears
    print('started calling the functions at bottom')
    ranking_dict = get_bball_monster()    ##<--- issue calling this function
    print('player_list has begun being created')
    player_list = [finding_the_date()]
    for player_rk in ranking_dict.keys():
        player = str(player_rk) + ': ' + str(ranking_dict[player_rk])
        player_list.append(player)






##################
    speech_output = str(player_list[0:11])
    #speech_output = 'Have a great day'

    reprompt_text = "Want news on a specific player? Say.. 'whats the news on Lebron James' for instance.. Or else say quit"
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome to your #1 source for news around the league"
    speech_output = "Ask me about a specific player. Or Say, 'whats the latest news' to get all caught up"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, let's get you caught up on the league!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Hope you got what you needed! " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "RecentNews":
        return get_recent_news_response()
    if intent_name == "PlayerNews":
        player_name = intent['slots']['PlayerName']['value']
        return get_player_news_response(player_name)
    if intent_name == "TopDFSPlays":
        return top_dfs_plays()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
