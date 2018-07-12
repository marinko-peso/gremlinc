# Gremlinc
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PyPI](https://img.shields.io/pypi/v/gremlinc.svg)](https://pypi.org/project/gremlinc/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gremlinc.svg)](https://pypi.org/project/gremlinc/)
[![license](https://img.shields.io/github/license/marinko-peso/gremlinc.svg)](https://github.com/marinko-peso/gremlinc/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Last Commit](https://img.shields.io/github/last-commit/marinko-peso/gremlinc.svg?maxAge=3600)](https://github.com/marinko-peso/gremlinc/commits/master)

Hide a message using zero width characters.


# Installation

Available via PyPi, latest version 0.3.
```sh
pip install gremlinc
```

# Usage

```python
from gremlinc import release, contain

text_in_gremlins = release('Your text goes here')
original_text = contain(text_in_gremlins)
```
Ideal for hiding messages in Javascript variables and DOM elements.


# License

MIT.
