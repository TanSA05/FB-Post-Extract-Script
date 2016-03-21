import urllib2
import json

def create_post_url(graph_url, APP_ID, APP_SECRET):
    #method to return 
	post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	post_url = graph_url + post_args 
	return post_url

def render_to_json(graph_url):
    #render graph url call to JSON
    web_response = urllib2.urlopen(graph_url)
    readable_page = web_response.read()
    json_data = json.loads(readable_page)
    
    return json_data

def main():
    #to find go to page's FB page, at the end of URL find username
    #e.g. http://facebook.com/walmart, walmart is the usernames
	graph_url = "https://graph.facebook.com/"
	#extract post data
	APP_ID = "Enter your APP_ID!"
	APP_SECRET = "Enter your APP_SECRET!"
	current_page = "https://www.facebook.com/bbchindi"
	final_page = graph_url + current_page[25:]
	post_url = create_post_url(final_page, APP_ID, APP_SECRET)
	#post_url = "https://graph.facebook.com/walmart/posts/?key=value&access_token=912600455526187|01641acf5f36a15834aeb5ef7909cad2"
	json_postdata = render_to_json(post_url)
	json_fbposts = json_postdata['data']

	f = open("posts.txt","w")

	for post in json_fbposts:
		f.write(post["message"])

if __name__ == "__main__":
    main()
