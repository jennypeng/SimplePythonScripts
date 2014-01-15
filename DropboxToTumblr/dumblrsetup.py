# Include the Dropbox SDK
import dropbox

#Get your app key and secret from the Dropbox developer website
app_key = 'YOUR APP KEY HERE'
app_secret = 'YOUR APP SECRET HERE'

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
client = dropbox.client.DropboxClient(access_token)
#Set up for folders
client.file_create_folder('/Dumblr/')
client.file_create_folder('/Dumblr/Queue/')
client.file_create_folder('/Dumblr/Posted/')
client.file_create_folder('/Dumblr/Queue/photo/')
client.file_create_folder('/Dumblr/Queue/text/')
client.file_create_folder('/Dumblr/Posted/photo/')
client.file_create_folder('/Dumblr/Posted/text/')
