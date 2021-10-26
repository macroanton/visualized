import json
import numpy as np
import matplotlib.pyplot as plt
tweets=[]
files = ['tweets_folder/condensed_2014.json', 'tweets_folder/condensed_2015.json', 'tweets_folder/condensed_2016.json', 'tweets_folder/condensed_2017.json', 'tweets_folder/condensed_2018.json']
for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_dacas=0
num_fake_news=0
num_mainstream_media=0
num_mexicos=0
num_obamas=0
num_russias=0
num_trumps=0
num_greats=0
num_walls=0
num_hilary=0
num_china=0

for tweet in tweets:
    if 'daca' in tweet['text'].lower():
        num_dacas += 1
    if 'fake news' in tweet['text'].lower():
        num_fake_news += 1
    if 'mainstream media' in tweet['text'].lower():
        num_mainstream_media += 1
    if 'mexico' in tweet['text'].lower():
        num_mexicos += 1
    if 'obama' in tweet['text'].lower():
        num_obamas += 1
    if 'russia' in tweet['text'].lower():
        num_russias += 1
    if 'trump' in tweet['text'].lower():
        num_trumps += 1
    if 'great' in tweet['text'].lower():
        num_greats += 1
    if 'wall' in tweet['text'].lower():
        num_walls += 1
    if 'hilary' in tweet['text'].lower():
        num_hilary += 1
    if 'china' in tweet['text'].lower():
        num_china += 1

print('num_dacas=', num_dacas)
print('percent dacas=', num_dacas/len(tweets)*100)
print('num_fake_news=', num_fake_news)
print('percent fake news=', num_fake_news/len(tweets))
print('num_mainstream_media=', num_mainstream_media)
print('percent mainstream media=', num_mainstream_media/len(tweets)*100)
print('num_mexicos=', num_mexicos)
print('percent mexico=', num_mexicos/len(tweets)*100)
print('num_obamas=', num_obamas)
print('percent obama=', num_obamas/len(tweets))
print('num_russias=', num_russias)
print('percent russia=', num_russias/len(tweets)*100)
print('num_trumps=', num_trumps)
print('percent trump=', num_trumps/len(tweets)*100)
print('num_greats=', num_greats)
print('percent great=', num_greats/len(tweets)*100)
print('num_walls=', num_walls)
print(' wall=', num_walls/len(tweets)*100)
print('num_hilary=', num_hilary)
print('percent hilary=', num_hilary/len(tweets)*100)
print('num_china=', num_china)
print('percent china=', num_china/len(tweets)*100)



tweets=[]
files = ['tweets_folder/condensed_2009.json', 'tweets_folder/condensed_2010.json', 'tweets_folder/condensed_2011.json', 'tweets_folder/condensed_2012.json', 'tweets_folder/condensed_2013.json']

for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_dacas1=0
num_fake_news1=0
num_mainstream_media1=0
num_mexicos1=0
num_obamas1=0
num_russias1=0
num_trumps1=0
num_greats1=0
num_walls1=0
num_hilary1=0
num_china1=0

for tweet in tweets:
    if 'daca' in tweet['text'].lower():
        num_dacas1 += 1
    if 'fake news' in tweet['text'].lower():
        num_fake_news1 += 1
    if 'mainstream media' in tweet['text'].lower():
        num_mainstream_media1 += 1
    if 'mexico' in tweet['text'].lower():
        num_mexicos1 += 1
    if 'obama' in tweet['text'].lower():
        num_obamas1 += 1
    if 'russia' in tweet['text'].lower():
        num_russias1 += 1
    if 'trump' in tweet['text'].lower():
        num_trumps1 += 1
    if 'great' in tweet['text'].lower():
        num_greats1 += 1
    if 'wall' in tweet['text'].lower():
        num_walls1 += 1
    if 'hilary' in tweet['text'].lower():
        num_hilary1 += 1
    if 'china' in tweet['text'].lower():
        num_china1 += 1
n_groups = 4
means_frank = (num_china, num_walls, num_russias, num_mexicos)
means_guido = (num_china1, num_walls1, num_russias1, num_mexicos1)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='2009-2013')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='2014-2018')

plt.xlabel('Words')
plt.ylabel('Occurences')
plt.title('Word occurences in Trumps tweets')
plt.xticks(index + bar_width, ('China', 'Wall', 'Russia', 'Mexico'))
plt.legend()

plt.tight_layout()
plt.show()
fig.savefig("tweets.png")