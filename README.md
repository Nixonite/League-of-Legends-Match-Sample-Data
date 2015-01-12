# League-of-Legends-Match-Sample-Data

<style type="text/css">
code { background-color: gray; color: cyan; }
</style>

League of Legends Match History data for 800 players.

It comes with a python file for retreiving more, and uses the RiotWatcher python module found <a href="https://github.com/pseudonym117/Riot-Watcher">here</a>.
I used my own developer api key so you'll have to get your own (free).

It took about 1.5-2 hours to fetch it all. Have fun.

Notes:
It was exported to json with mongoexport. The json file is actually one json per line so it's best to just make a list like so

<code>data = []</code>

and to read the file in one by one i.e.

<code>
with open('lol.json') as jsondata:
	data.append(json.load(jsondata))
</code>
It's weird, but it works.