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

## Related
- [`hafas-client`](https://github.com/public-transport/hafas-client) – JavaScript client for the HAFAS API.
- [`public-transport-enabler`](https://github.com/schildbach/public-transport-enabler) – Unleash public transport data in your Java project.
- [*Friendly Public Transport Format*](https://github.com/public-transport/friendly-public-transport-format#friendly-public-transport-format-fptf) – A format for APIs, libraries and datasets containing and working with public transport data.
- [`db-hafas`](https://github.com/derhuerst/db-hafas#db-hafas) – JavaScript client for the DB HAFAS API.

## Contributing
If you **have a question**, **found a bug** or want to **propose a feature**, have a look at [the issues page](https://github.com/n0emis/pyhafas/issues).
