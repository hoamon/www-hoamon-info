# -*- coding: utf-8 -*-

import tinkerer
import tinkerer.paths

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = "hoamon's sandbox"

# Change this to the tagline of your blog
tagline = '"sandbox" is a jargon of Version Control System.'

# Change this to your name
author = 'hoamon'

# Change this to your copyright string
copyright = '2006-2012, ' + author

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
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus']

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
    "**": ["ads.html", "about_me.html", "cc.html", "recent.html", "custom_search.html", "categories.html", "tags.html", "javascript.html"]
}

#archive.html, aggregated.html

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

import os

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = os.popen('hg id -n -i').read().replace(' ', '-').replace('+', '').replace('\n', '')
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
