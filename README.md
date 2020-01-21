# pyhafas
**A python client for HAFAS public transport APIs**.

## Installation
You only need to install the pyhafas package, for example using pip:

```bash
$ pip install pyhafas
```

That’s it!

## Development setup
For development is **recommended** to use a ``venv``.

```bash
$ python3.6 -m venv .venv
$ source .venv/bin/activate
$ python setup.py develop
```

## Background
There's [a company called HaCon](https://hacon.de) that sells [a public transport management system called HAFAS](https://de.wikipedia.org/wiki/HAFAS). It is [used by companies all over Europe](https://gist.github.com/derhuerst/2b7ed83bfa5f115125a5) to serve routing and departure information for apps. All those endpoints are similar, with the same terms and API routes, but have slightly different options, filters and sets of enabled features.

## Contributing
If you **have a question**, **found a bug** or want to **propose a feature**, have a look at [the issues page](https://github.com/n0emis/pyhafas/issues).
