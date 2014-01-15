from time import strftime
#Include the Pytumblr SDK
import pytumblr
# Include the Dropbox SDK
import dropbox

# Authenticate Tumblr via OAuthclient 
# Get your keys from the Tumblr developer website
client = pytumblr.TumblrRestClient(
  '<consumer_key>',
  '<consumer_secret>',
  '<oauth_token>',
  '<oauth_secret>',
)

#Get your app key and secret from the Dropbox developer website
app_key = '<YOUR APP KEY HERE>'
app_secret = '<YOUR APP SECRET HERE>'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Generate an authorization URL using the start method of the flow object
authorize_url = flow.start()

#Have the user sign in and authorize this token (In real-world app, change to redirect and pass in callback URL)
print '1. Go to ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

#This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

"""HAVE TUMBLR ACCESS QUEUE AND POST TEXT FILES """
queue_metadata = dropbox_client.metadata('/Dumblr/Queue/text/')
queue_count = len(queue_metadata['contents'])
for n in range (0,queue_count):
	f, metadata = dropbox_client.get_file_and_metadata(queue_metadata['contents'][n]['path'])
	linestring = f.read()
# Make the request to create a text post
	client.create_text('YOURBLOGNAME.tumblr.com', title = '', body = linestring)
#Time posted
	current_time = strftime("%Y-%m-%d-%H-%Mm%Ss")
#Remove the queue files
	dropbox_client.file_move(queue_metadata['contents'][n]['path'],'/Dumblr/Posted/text/textpost{0}.txt'.format(current_time))

"""HAVE TUMBLR ACCESS QUEUE AND POST PHOTOS """
queue_metadata = dropbox_client.metadata('/Dumblr/Queue/photo/')
queue_count = len(queue_metadata['contents'])
for n in range (0, queue_count):
	ext = queue_metadata['contents'][n]['path'][-4:]
# Make the request to create a photo post
	client.create_photo('YOURBLOGNAME.tumblr.com', state='published' , data= ('C:/Users/USERNAMEHERE/Dropbox'+ queue_metadata['contents'][n]['path']))
#Time posted
	current_time = strftime("%Y-%m-%d-%H-%Mm%Ss")
#Remove the queue files
	dropbox_client.file_move(queue_metadata['contents'][n]['path'],'/Dumblr/Posted/photo/photopost{1}{0}'.format(ext,current_time))

