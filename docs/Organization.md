# How this repo is organized

Here is a rundown of the directory structure
of translate the docs:

## Documentation

All of the documentation for how to translate the docs 
lives in markdown files in `docs/`.

This is converted to HTML documentation using `mkdocs`.

The configuration for mkdocs is in `mkdocs.yml`.

The mkdocs theme used is mkdocs-material, which is in the 
git submodule `mkdocs-material/`.

The static content is on the `gh-pages` branch and is hosted
on `https://pages.charlesreid1.com/` and on Github Pages.

## Translation

The document is first parsed with pandoc to convert markdown
to JSON.

The JSON is passed to a panflute filter, which processes the text.

Translation magic happens using the Google Cloud Translate API,
which is called by the panflute filter.

Pandoc is used to convert the JSON back to (translated) markdown.

