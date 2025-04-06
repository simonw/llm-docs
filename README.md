# llm-docs

[![PyPI](https://img.shields.io/pypi/v/llm-docs.svg)](https://pypi.org/project/llm-docs/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-docs?include_prereleases&label=changelog)](https://github.com/simonw/llm-docs/releases)
[![Tests](https://github.com/simonw/llm-docs/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/llm-docs/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-docs/blob/main/LICENSE)

Ask questions of LLM documentation using LLM

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-docs
```
## Usage

This depends on the next release of LLM. Once installed you can ask questions of the LLM documentation like this:

```bash
llm -t docs: 'How do I calculate embeddings for a CSV file?'
```
It also works against other packages that have their documentation recorded in the [docs-for-llms](https://github.com/simonw/docs-for-llms) repository, for example `sqlite-utils`:
```bash
llm -t docs:sqlite-utils 'How do I vacuum my database?'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-docs
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
