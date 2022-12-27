# De-Tokenize

-----------------

![Package](https://img.shields.io/badge/Package-detokenize-brightgreen)
[![PyPI version](https://badge.fury.io/py/detokenize.svg)](https://badge.fury.io/py/detokenize)
![Author](https://img.shields.io/badge/author-littinrajan-blue)
![License](https://img.shields.io/github/license/littinrajan/bank_statement_renamer)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Downloads](https://static.pepy.tech/personalized-badge/detokenize?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20Downloads)](https://pepy.tech/project/detokenize)

## What is it?
**De-Tokenize** is a Python  package which provides fast, accurate structuring of tokens back to original sentence form.

## Contributor
**Littin Rajan**

## Main Features
  - Light-weight package
  - No more dependencies
  - Powerful, flexible

## Where to get it?
The source code is currently hosted on GitHub at: https://github.com/littinrajan/detokenize

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/detokenize) and on [Conda](https://docs.conda.io/en/latest/).

```sh
# conda
conda install detokenize
```

```sh
# or PyPI
pip install detokenize
```

## Usage

```sh
from detokenize.detokenizer import detokenize

sample_tokens = ['These', 'are', 'some', 'tokens', '.']
sentence = detokenize(sample_tokens)
```

## License
[MIT](LICENSE)

## Contributing to De-Tokenize
All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
