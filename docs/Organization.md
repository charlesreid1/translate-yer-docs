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

# Plans

The tool in this repository (the pandoc filter) will eventually
become a command line tool that can be run in-place from any 
repository, and the translated markdown deposited into a new 
directory.

This requires one major design change: rather than using pandoc
and applying filters from the command line, we must call the 
pandoc API from Python directly. Then we can define the filter
as part of the command line tool, and when we call the translate
the docs tool, it applies the filter in-place.

The end result, for the user, is the ability to run a single command
that will translate their docs:

```
$ translate_the_docs --list-languages
ru
de
es
fr
ar
...

$ translate_the_docs 

Before we can translate your docs, we will start with a few questions.

What directory contains your current markdown docs?
Leave empty for default: docs
Answer: docs

What language do you want to translate your markdown docs into?
Type ? for a list of languages.
Answer: ?

Possible languages: ru, de, es, fr, ar, ...

What language do you want to translate your markdown docs into?
Type ? for a list of languages.
Answer: ru

What directory do you want to contain your translated markdown docs?
Leave empty for default: ru_docs
Answer:

Translating...
Done!
```

Or set with command line options:

```
$ translate_the_docs --source=doc/ --target=ru_docs --language=ru
```

