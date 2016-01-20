import urllib2
import json
locu_api='c59c0fb87e17fa7bf8cc51eddb4014acbf7f5503'
#url='https://api.locu.com/v1_0/venue/search/?locality=Ahmedabad&api_key=c59c0fb87e17fa7bf8cc51eddb4014acbf7f5503'

#json=json.load(urllib2.urlopen(url))
#print json
#locality=Ahmedabad
#for data in json['objects']:
#    print "\nitem is : \n" + str(data)
 #   print data['name']
 #   print data['region']
    #print data['phone']

def locu(query):
    api=locu_api
    url='https://api.locu.com/v1_0/venue/search/?'
    locality=query
    final_url=url+'locality='+locality+'&api_key=' + api
    print final_url
    #json=json.load(urllib2.urlopen(final_url))
    json1=urllib2.urlopen(final_url)
    data=json.load(json1)

    for data1 in data['objects']:
        #print "\nitem is : \n" + str(data1)
        print data1['name']
        print data1['region']
        #print data['phone']
    


print locu('Ahmedabad')
