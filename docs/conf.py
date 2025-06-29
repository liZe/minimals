import minimals

project = "Minimals"
copyright = "Guillaume Ayoub and contributors"
release = minimals.__version__

html_theme = "furo"
html_theme_options = {
    "top_of_page_buttons": ["edit"],
    "source_edit_link": "https://github.com/liZe/minimals/edit/main/docs/{filename}",
}

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
]
