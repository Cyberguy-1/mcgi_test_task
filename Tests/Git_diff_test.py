#Import python requests
import requests

#Define Url of commit of interest (Github only please)
diff_url = "https://github.com/FFmpeg/FFmpeg/commit/a7a7f32c8ad0179a1a85d0a8cff35924e6d90be8"

#Append ".diff" to obtain raw commit message
diff_url = diff_url + ".diff"

#Make url call
r = requests.get(diff_url)

#Print result
print(r.text)