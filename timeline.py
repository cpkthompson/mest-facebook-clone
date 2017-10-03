from datetime import datetime

class Content(object):
    time_created = datetime.now()

class TextContent(Content):
    content = ""

class Video(Content):
    content = ""

class ImageContent(Content):
    content = ""
        
class Timeline:

    def __init__(self):

        # obtain current user

        
        # obtain current users friends
        # obtain current users friends posts
        # append current users friends posts to a lists
        # loop over lists and display chronologically
        # posts show with a number beside so number entered shows posts details
        # in post details, post is shown with options to like or comment
        pass

    def show_post(self):
        pass

    def show_ads(self):
        pass

    def view_page(self):
        pass

    def create_page(self):
        pass

    def dismiss_ad(self):
        pass

    def obtain_current_user_friends(self):
        pass

    def posts_from_user_friends(self):
        pass

class Post():
    content_types = ["text","video", "image" ]

    def __init__(self):
        #function to check if user is signed in
        self.create_post()

    def create_post(self):
        collect = input("Enter post type (text, video or image): ")

        if collect in self.content_types:
            if collect == "text":
                self.content = input("Enter your text status update: ")
            elif collect == "video":
                self.content = input("Enter the link to video: ")
            elif collect == "image":
                self.content = input("Enter link to image: ")
        else:
            print ("You typed a wrong type")
            self.create_post()


    def like_post(self):
        posts = []
        for post in posts:
            print(post)


    def comment_on_post(self):
        pass
    

if __name__ == '__main__':
        new_post = Post()