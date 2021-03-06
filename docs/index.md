# translate yer docs

This repository translates yer docs into another language.

This uses the Google Cloud Translate API,
pandoc, and the panflute library to create
a translation filter for Markdown files.

See an example here: [russian-rainbow-mind-machine](https://pages.charlesreid1.com/russian-rainbow-mind-machine)
(page contains documentation for the [rainbow-mind-machine](https://pages.charlesreid1.com/b-rainbow-mind-machine)
library translated into Russian).

## How This Repo is Organized

[How this repo is organized](Organization.md)

## Part 1: Google Cloud Translate API Setup

The Google Cloud Translate API is what makes this all possible.

It is easier to translate documentation into Russian 
than it is to figure out how to parse Markdown programmatically
with panflute and pandocs.

[Part 1: Setup](Setup.md)

## Part 2: Pandoc

We want to parse and translate Markdown written
in English, and turn it into Markdown written in 
Russian. We use pandoc to parse the Markdown file
and identify the bits that can be translated,
pass them to the Google Cloud Translate API,
and convert the translated text back into
Markdown.

Part 2: Pandoc:

[Pandoc: Markdown to JSON](PandocA.md)

[Pandoc: JSON to JSON](PandocB.md)

## Part 3: Panflute

Panflute is a Python library for writing Pandoc filters.
It is picky and tricky.

Part 3: Panflute:

[Panflute: Translate](PanfluteA.md)

[Panflute: Page Elements](PanfluteB.md)

## Part 4: Pandoc

The panflute filter will process JSON and return more JSON,
so we have one last step, which is converting the final
JSON document into Markdown.

[Part 4: Pandoc: JSON to Markdown](PandocC.md)

## Part 5: Testing

You do want to write tests for all of this stuff, don't you?

[Part 5: Testing](Testing.md)

## Part 6: Useful Links

[Part 6: Useful Links](Links.md)

