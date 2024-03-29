# -*- coding: utf-8 -*-

import tinkerer, datetime
import tinkerer.paths

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = "hoamon's sandbox"

# Change this to the tagline of your blog
tagline = '"sandbox" is a jargon of Version Control System.'

# Change this to your name
author = 'Ho, Yueh-Feng &lt;<a href="http://www.hoamon.info/">http://<b>hoamon</b>.info/</a>&gt;'

# Change this to your copyright string
copyright = '2006 ~ %s, Yueh-Feng Ho(hoamon)'%datetime.datetime.today().year

# Change this to your blog root URL (required for RSS feed)
website = 'http://www.hoamon.info/blog/'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = "hoamoninfo"

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'favicon.ico'

# Pick another Tinkerer theme or use your own
html_theme = "modern5"

# Theme-specific options, see docs
html_theme_options = { }

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = 'http://feeds.feedburner.com/hoamon/DFdn'

# Number of blog posts per page
posts_per_page = 10

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus', 'patch_extra']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['./', tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*"]

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["about_me.html",
           "ads.html",
           "cc.html",
           "recent.html",
           "custom_search.html",
           "categories.html",
           "tags_cloud.html",
           "tags.html",
           "javascript.html",
           "css.html",
           ]
}

#archive.html, aggregated.html

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

import os, git

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
repo = git.Repo(search_parent_directories=True)
release = repo.head.object.hexsha[:7]
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
