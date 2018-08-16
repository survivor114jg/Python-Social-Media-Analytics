import os 
import json
import facebook
import requests

if __name__ == '__main__':
	token = os.environ.get("FACEBOOK_TEMP_TOKEN")

	graph = facebook.GraphAPI(token)
	all_fields=[
	'message',
	'created_time',
	'description',
	'caption',
	'link',
	'place',
	'status_type'
	]
	all_fields = ','.join(all_fields)
	posts = graph.get_connections('me', 'posts', fields =all_fields)

	while True: # keep paginating
		try:
			with open('my_posts.json1', 'a') as f:
				for post in posts['data']:
					f.write(json.dumps(post)+"\n")
					# get next page
					posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			# No more pages, break the loop
			break
