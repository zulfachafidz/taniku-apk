from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
import json
from components.post_card import PostCard
from components.circular_avatar_image import CircularAvatarImage


class HomePage(MDScreen):
    profile_picture = 'https://images.unsplash.com/photo-1623065691913-e9a650810efd?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'

    def __init__(self, **kw):
        Builder.load_file("kv/signup.kv")
        Builder.load_file("kv/home_page.kv")
        Builder.load_file('components/appbar.kv')
        Builder.load_file("components/story_creator.kv")
        Builder.load_file("components/bottom_nav.kv")
        Builder.load_file("components/circular_avatar_image.kv")
        Builder.load_file("components/post_card.kv")
        super().__init__(**kw)

    def on_enter(self):
        self.list_stories()
        self.list_posts()

    def list_stories(self):
        with open('assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar = data[name]['avatar'],
                    name = name
                ))
    
    def list_posts(self):
        with open('assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))