"""
import os sys json


import numpy as np
import pandas as pd]

from django.views.generic import ListView

from posts.models import Post

"""


from django.views.generic import ListView

from posts.models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
