import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time
import urllib
import json
import sys
import csv
import re
from watson_developer_cloud import ToneAnalyzerV3

ckey = "r27pD98Njw3xR16etBJzUSGIl" #""LgTkFWkDNUGCbuEkqVqCbAkm5
csecret = "WUkS92ojlYz9HZJ7n0mMraIQ8TB4RdinxFiTdHFSLXH11JweeV" #"bWh96OUqUid9ThkmAKoAOpmfrmSbPTJqytwijJixdYDZFpp9Wg
atoken = "51715790-Z3Vqs8EwlfrUvq92Yp4BSxXxVmMfpPBZKPCEhkMMN" #51715790-"hDAgGPPF4O0YNWE4NCMBUZExUp0brdgGw4KIGXyrL
asecret = "USNsLTAdQBMpiGirs2LyXq3LP3jySB52qztrwuWIUTVRB" #"QVSxMvJWT5uiehMWqOMqdGsjQo2FGWpEOEyxo5DmfbgYW

tone_analyzer = ToneAnalyzerV3(
   username='c712c79c-0774-4478-8d08-2ee85d48a5e8',
   password='uu6NSwq7UkGB',
   version='2017-03-27')

sentdexAuth = ''

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

def sentimentAnalysis(text):
	encode_text = urllib.quote(text)
	API_Call = 'http://sentdex.com/api/api.php?text='+encode_text+'&auth='+sentdexAuth
	x = len(text)
	output = urllib.urlopen(API_Call).read()
	return output


def analyze_tone(text):
    username = 'c712c79c-0774-4478-8d08-2ee85d48a5e8'
    password = 'uu6NSwq7UkGB'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,
         data=data)
        return r.text
    except:
        return False

def display_results(data):
    data = json.loads(str(data))

    anger = float (data['document_tone']['tone_categories'][0]['tones'][0]['score'])
    print anger_s
    disgust = float (data['document_tone']['tone_categories'][0]['tones'][1]['score'])
    print disgust
    fear = float (data['document_tone']['tone_categories'][0]['tones'][2]['score'])
    print fear
    joy = float (data['document_tone']['tone_categories'][0]['tones'][3]['score'])
    print joy
    sadness = float (data['document_tone']['tone_categories'][0]['tones'][4]['score'])
    print sadness

def motor1(anger,disgust,fear,sadness):
    global m1
    m1 = 0

    if anger > 90:
        m1 = m1 + 11
    elif anger > 80:
        m1 = m1 + 10
    elif anger > 70:
        m1 = m1 + 9
    elif anger > 60:
        m1 = m1 + 8
    elif anger > 50:
        m1 = m1 + 7
    elif anger > 40:
        m1 = m1 + 6
    elif anger > 30:
        m1 = m1 + 5
    elif anger > 20:
        m1 = m1 + 4
    elif anger > 15:
        m1 = m1 + 3
    elif anger > 10:
        m1 = m1 + 2
    elif anger > 5:
        m1 = m1 + 1

    if disgust > 90:
        m1 = m1 + 11
    elif disgust > 80:
        m1 = m1 + 10
    elif disgust > 70:
        m1 = m1 + 9
    elif disgust > 60:
        m1 = m1 + 8
    elif disgust > 50:
        m1 = m1 + 7
    elif disgust > 40:
        m1 = m1 + 6
    elif disgust > 30:
        m1 = m1 + 5
    elif disgust > 20:
        m1 = m1 + 4
    elif disgust > 15:
        m1 = m1 + 3
    elif disgust > 10:
        m1 = m1 + 2
    elif disgust > 5:
        m1 = m1 + 1

    if fear > 90:
        m1 = m1 + 5.5
    elif fear > 80:
        m1 = m1 + 5
    elif fear > 70:
        m1 = m1 + 4.5
    elif fear > 60:
        m1 = m1 + 4
    elif fear > 50:
        m1 = m1 + 3.5
    elif fear > 40:
        m1 = m1 + 3
    elif fear > 30:
        m1 = m1 + 2.5
    elif fear > 20:
        m1 = m1 + 2
    elif fear > 15:
        m1 = m1 + 1.5
    elif fear > 10:
        m1 = m1 + 1
    elif fear > 5:
        m1 = m1 + 0.5

    if sadness > 90:
        m1 = m1 + 11
    elif sadness > 80:
        m1 = m1 + 10
    elif sadness > 70:
        m1 = m1 + 9
    elif sadness > 60:
        m1 = m1 + 8
    elif sadness > 50:
        m1 = m1 + 7
    elif sadness > 40:
        m1 = m1 + 6
    elif sadness > 30:
        m1 = m1 + 5
    elif sadness > 20:
        m1 = m1 + 4
    elif sadness > 15:
        m1 = m1 + 3
    elif sadness > 10:
        m1 = m1 + 2
    elif sadness > 5:
        m1 = m1 + 1

def motor2(anger,fear,joy):
    global m2
    m2 = 0

    if anger > 90:
        m2 = m2 + 11
    elif anger > 80:
        m2 = m2 + 10
    elif anger > 70:
        m2 = m2 + 9
    elif anger > 60:
        m2 = m2 + 8
    elif anger > 50:
        m2 = m2 + 7
    elif anger > 40:
        m2 = m2 + 6
    elif anger > 30:
        m2 = m2 + 5
    elif anger > 20:
        m2 = m2 + 4
    elif anger > 15:
        m2 = m2 + 3
    elif anger > 10:
        m2 = m2 + 2
    elif anger > 5:
        m2 = m2 + 1

    if fear > 90:
        m2 = m2 + 5.5
    elif fear > 80:
        m2 = m2 + 5
    elif fear > 70:
        m2 = m2 + 4.5
    elif fear > 60:
        m2 = m2 + 4
    elif fear > 50:
        m2 = m2 + 3.5
    elif fear > 40:
        m2 = m2 + 3
    elif fear > 30:
        m2 = m2 + 2.5
    elif fear > 20:
        m2 = m2 + 2
    elif fear > 15:
        m2 = m2 + 1.5
    elif fear > 10:
        m2 = m2 + 1
    elif fear > 5:
        m2 = m2 + 0.5

    if joy > 90:
        m2 = m2 + 5.5
    elif joy > 80:
        m2 = m2 + 5
    elif joy > 70:
        m2 = m2 + 4.5
    elif joy > 60:
        m2 = m2 + 4
    elif joy > 50:
        m2 = m2 + 3.5
    elif joy > 40:
        m2 = m2 + 3
    elif joy > 30:
        m2 = m2 + 2.5
    elif joy > 20:
        m2 = m2 + 2
    elif joy > 15:
        m2 = m2 + 1.5
    elif joy > 10:
        m2 = m2 + 1
    elif joy > 5:
        m2 = m2 + 0.5

def motor3(joy):
    global m3
    m3 = 0

    if joy > 90:
        m3 = m3 + 11
    elif joy > 80:
        m3 = m3 + 10
    elif joy > 70:
        m3 = m3 + 9
    elif joy > 60:
        m3 = m3 + 8
    elif joy > 50:
        m3 = m3 + 7
    elif joy > 40:
        m3 = m3 + 6
    elif joy > 30:
        m3 = m3 + 5
    elif joy > 20:
        m3 = m3 + 4
    elif joy > 15:
        m3 = m3 + 3
    elif joy > 10:
        m3 = m3 + 2
    elif joy > 5:
        m3 = m3 + 1

def motor4(anger,disgust,fear,sadness):
    global m4
    m4 = 0

    if anger > 90:
        m4 = m4 + 11
    elif anger > 80:
        m4 = m4 + 10
    elif anger > 70:
        m4 = m4 + 9
    elif anger > 60:
        m4 = m4 + 8
    elif anger > 50:
        m4 = m4 + 7
    elif anger > 40:
        m4 = m4 + 6
    elif anger > 30:
        m4 = m4 + 5
    elif anger > 20:
        m4 = m4 + 4
    elif anger > 15:
        m4 = m4 + 3
    elif anger > 10:
        m4 = m4 + 2
    elif anger > 5:
        m4 = m4 + 1

    if disgust > 90:
        m4 = m4 + 5.5
    elif disgust > 80:
        m4 = m4 + 5
    elif disgust > 70:
        m4 = m4 + 4.5
    elif disgust > 60:
        m4 = m4 + 4
    elif disgust > 50:
        m4 = m4 + 3.5
    elif disgust > 40:
        m4 = m4 + 3
    elif disgust > 30:
        m4 = m4 + 2.5
    elif disgust > 20:
        m4 = m4 + 2
    elif disgust > 15:
        m4 = m4 + 1.5
    elif disgust > 10:
        m4 = m4 + 1
    elif disgust > 5:
        m4 = m4 + 0.5

    if fear > 90:
        m4 = m4 + 5.5
    elif fear > 80:
        m4 = m4 + 5
    elif fear > 70:
        m4 = m4 + 4.5
    elif fear > 60:
        m4 = m4 + 4
    elif fear > 50:
        m4 = m4 + 3.5
    elif fear > 40:
        m4 = m4 + 3
    elif fear > 30:
        m4 = m4 + 2.5
    elif fear > 20:
        m4 = m4 + 2
    elif fear > 15:
        m4 = m4 + 1.5
    elif fear > 10:
        m4 = m4 + 1
    elif fear > 5:
        m4 = m4 + 0.5

    if sadness > 90:
        m4 = m4 + 11
    elif sadness > 80:
        m4 = m4 + 10
    elif sadness > 70:
        m4 = m4 + 9
    elif sadness > 60:
        m4 = m4 + 8
    elif sadness > 50:
        m4 = m4 + 7
    elif sadness > 40:
        m4 = m4 + 6
    elif sadness > 30:
        m4 = m4 + 5
    elif sadness > 20:
        m4 = m4 + 4
    elif sadness > 15:
        m4 = m4 + 3
    elif sadness > 10:
        m4 = m4 + 2
    elif sadness > 5:
        m4 = m4 + 1

def motor5(fear,joy):
    global m5
    m5 = 0

    if fear > 90:
        m5 = m5 + 11
    elif fear > 80:
        m5 = m5 + 10
    elif fear > 70:
        m5 = m5 + 9
    elif fear > 60:
        m5 = m5 + 8
    elif fear > 50:
        m5 = m5 + 7
    elif fear > 40:
        m5 = m5 + 6
    elif fear > 30:
        m5 = m5 + 5
    elif fear > 20:
        m5 = m5 + 4
    elif fear > 15:
        m5 = m5 + 3
    elif fear > 10:
        m5 = m5 + 2
    elif fear > 5:
        m5 = m5 + 1

    if joy > 90:
        m5 = m5 + 5.5
    elif joy > 80:
        m5 = m5 + 5
    elif joy > 70:
        m5 = m5 + 4.5
    elif joy > 60:
        m5 = m5 + 4
    elif joy > 50:
        m5 = m5 + 3.5
    elif joy > 40:
        m5 = m5 + 3
    elif joy > 30:
        m5 = m5 + 2.5
    elif joy > 20:
        m5 = m5 + 2
    elif joy > 15:
        m5 = m5 + 1.5
    elif joy > 10:
        m5 = m5 + 1
    elif joy > 5:
        m5 = m5 + 0.5

    # # print(data)
    # for i in data['document_tone']['tone_categories']:
    #     print(i['category_name'])
    #     print("-" * len(i['category_name']))
    #     for j in i['tones']:
    #         print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
    #     print()
    # print()

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
text_tweet = ''''''
# q=''

text_number = 0

for tweet in tweepy.Cursor(api.search,geocode='22.2479,114.2034,15mi', lang="en", since='2017-05-11',until='2017-05-12').items(5000):
    text = remove_urls(tweet.text)

    
    text_number = text_number + 1

    # fd.write(text.encode('utf-8'))
    print "Tweet Number [   " + str(text_number) + "   ]"
    print " \n"
    print text
    print " \n"


    text_tweet = text_tweet + text

    if ((text_number%100)==0):
        data = json.loads(str(json.dumps(tone_analyzer.tone(text=text_tweet), indent=1)))
        anger = 100*float (data['document_tone']['tone_categories'][0]['tones'][0]['score'])
        # print anger
        disgust = 100*float (data['document_tone']['tone_categories'][0]['tones'][1]['score'])
        # print disgust
        fear = 100*float (data['document_tone']['tone_categories'][0]['tones'][2]['score'])
        # print fear
        joy = 100*float (data['document_tone']['tone_categories'][0]['tones'][3]['score'])
        # print joy
        sadness = 100*float (data['document_tone']['tone_categories'][0]['tones'][4]['score'])
        # print sadness

        anger_str = "%0.2f" % anger
        disgust_str = "%0.2f" % disgust
        fear_str = "%0.2f" % fear
        joy_str = "%0.2f" % joy
        sadness_str = "%0.2f" % sadness
        print " \n" 
        print " \n"
        print " \n" 

        print "Anger[" +str(anger_str) + "%] Disgust[" +str(disgust_str)+"%] Fear[" +str(fear_str)+ "%] Joy[" + str(joy_str)+"%]"+" Sadness[" +str(sadness_str)+ "%]"
        print " \n" 
        print " \n"
        print " \n" 



        motor1(anger,disgust,fear,sadness)
        motor2(anger,fear,joy)
        motor3(joy)
        motor4(anger,disgust,fear,sadness)
        motor5(fear,joy)

        if ((m3-m4)>0):
            m3 = m3-m4
            m4 = 0
        else:
            m4 = m4-m3
            m4 = 0

        print "        Eyebrow Middle [  " + str(m2) + "  ] Eyebrow Beginning [  " + str(m1) +  "  ]"
        print " \n" 
        print "                         Mouth Upward [  " + str(m3) +  "  ]"
        print " \n" 
        print "                         Mouth Downward [  " + str(m4) +  "  ]"    
        print " \n" 
        print "                         Mouth Open [  " + str(m5) +  "  ]"
        print " \n" 

        time.sleep(5) # delays for 5 seconds
