import instaloader

def download_profile(username):
    loader = instaloader.Instaloader()
    loader.download_profile(username, profile_pic_only=True)

download_profile("natgeo")
