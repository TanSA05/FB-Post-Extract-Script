import urllib2
import urllib
import json
import unicodedata
import codecs
import time

def create_post_url(graph_url, APP_ID, APP_SECRET):
    #method to return 
	post_args = "/feed/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	post_url = graph_url + post_args 
	return post_url

def create_comment_like_url(id, APP_ID, APP_SECRET):
	#method to return
	graph_url = "https://graph.facebook.com/"
	post_args = "/v2.8/" + id + "/likes/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	comment_like_url = graph_url + post_args

	return comment_like_url

def render_to_json(graph_url):
	#render graph url call to JSON
	web_response = urllib.urlopen(graph_url)
	json_data = json.loads(web_response.read())
	return json_data

def return_posts(post_url):
	# "Hello to new function"
	json_postdata = render_to_json(post_url)
	#json_fbposts = unicodedata.normalize('NFKD',json_postdata).encode('ascii','ignore')
	#print type(json_postdata)
	#haiku_posts = json.loads(json_fbposts)
	#print "Haiku Posts", json_fbposts
	for post in json_postdata['data']:
		#print post['message']
		p = unicodedata.normalize('NFKD', post['message']).encode('ascii','ignore')
		print p
		id = unicodedata.normalize('NFKD',post['id']).encode('ascii','ignore')
		print id
		print '\n\n'

	return json_postdata

def likes(comment_url):
	json_commentdata = render_to_json(comment_url)
	i = 0
	if (json_commentdata['data'] != []):
		for post in json_commentdata['data']:
			i+=1
	else:
		return 0

	return i

def main():
	#to find go to page's FB page, at the end of URL find username
	#e.g. http://facebook.com/walmart, walmart is the usernames
	graph_url = "https://graph.facebook.com/"
	#extract post data
	APP_ID = ""
	APP_SECRET = ""
	current_page = "https://www.facebook.com/v2.8/175065909612262"
	#Enter only the event id, for eg: 680613812093479
	final_page = graph_url + current_page[30:]
	post_url = create_post_url(final_page, APP_ID, APP_SECRET)
	d = {}
	while True:
		hp = return_posts(post_url)
		if (hp['data'] != []):
			post_url = hp['paging']['next']
			for post in hp['data']:
				p = unicodedata.normalize('NFKD', post['message']).encode('ascii','ignore')
				id = unicodedata.normalize('NFKD',post['id']).encode('ascii','ignore')
				d[id] = []
				d[id].append(p)
				time.sleep(10)
				comment_like_url = create_comment_like_url(id, APP_ID, APP_SECRET)
				like_count = likes(comment_like_url)
				d[id].append(like_count)
				print d
		else:
			print "You're done!"
			break
if __name__ == "__main__":
	main()
