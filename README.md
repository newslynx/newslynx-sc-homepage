[![Build status](https://travis-ci.org/newslynx/newslynx-sc-homepage.svg)](https://travis-ci.org/newslynx/newslynx-sc-homepage) [![Documentation Status](https://readthedocs.org/projects/newslynx-sc-homepage/badge/?version=latest)](https://readthedocs.org/projects/newslynx-sc-homepage/?badge=latest)

newslynx-sc-homepage
==========================================================================================



## Installation

### Production

To install `newslynx-sc-homepage` for an active installation of `newslynx-core`, run the following command:

```bash
$ newslynx sc-install https://github.com/newslynx/newslynx-sc-homepage.git
```

To add `newslynx-sc-homepage` all orgnaizations, run:

```bash
$ newslynx sc-sync
```

### Development 

If you want to modify / add Sous Chefs to `newslynx-sc-homepage`, do the following:

**NOTE** Will install a fresh version of `newslynx` via `pip`.

```bash
$ git clone https://github.com/newslynx/newslynx-sc-homepage.git
$ cd newslynx-sc-homepage
$ pip install --editable .
```

You should now be able to run `newslynx-sc-homepage`'s Sous Chefs in development mode

```bash 
% newslynx sc-run newslynx_sc_homepage/say_my_name.yaml --myname='Brian Abelson'
```

## Tests

Requires `nose`

```bash
$ make all_tests
```

## Documentation

Documentation for `newslynx-sc-homepage` is hosted on [Read The Docs](http://newslynx-sc-homepage.readthedocs.org/).

It's generated via the following steps

* converts this file (`README.md`) into a ReStructured Text file, saving it to [docs/index.rst](https://github.com/newslynx/newslynx-sc-homepage/blob/master/docs/index.rst)
* runs `newslynx sc-docs newslynx_sc_homepage -f rst` to generate documentation for all the Sous Chefs in `newslynx-sc-homepage` and saves the output to [docs/sous-chefs.rst](https://github.com/newslynx/newslynx-sc-homepage/blob/master/docs/sous-chefs.rst)
* Builds Sphinx Documentation from these files.


## Continuous Integration

Builds for `newslynx-sc-homepage` can be found on [Travis](https://travis-ci.org/newslynx/newslynx-sc-homepage)

## Contributing

See the [contributing guidelines](https://github.com/newslynx/newslynx-sc-homepage/blob/master/CONTRIBUTING.md).


## What's in this module ?

- [README.md](https://github.com/newslynx/newslynx-sc-homepage/blob/master/README.md)
	* This file 

- [VERSION](https://github.com/newslynx/newslynx-sc-homepage/blob/master/VERSION)
	* `newslynx-sc-homepage`'s source-of-truth version.

- [requirements.txt](https://github.com/newslynx/newslynx-sc-homepage/blob/master/requirements.txt)
	* `newslynx-sc-homepage`'s python dependencies.

- [MANIFEST.in](https://github.com/newslynx/newslynx-sc-homepage/blob/master/MANIFEST.in)
	* Specifications for which files to include in the PyPI distribution.
	* See the docs on this [here](https://docs.python.org/2/distutils/sourcedist.html#specifying-the-files-to-distribute).

- [setup.py](https://github.com/newslynx/newslynx-sc-homepage/blob/master/setup.py)
	* Specification's for building `newslynx-sc-homepage`'s PyPI distribution.

- [.travis.yml](https://github.com/newslynx/newslynx-sc-homepage/blob/master/.travis.yml)
	* Configurations for Travis Continuous Integration
	* You must activate this project on [travis-ci.org](https://github.com/newslynx/newslynx-sc-homepage/blob/master/http://travis-ci.org/) for this to run on subsequent updates.

- [Makefile](https://github.com/newslynx/newslynx-sc-homepage/blob/master/Makefile)
	* Helpers for managing `newslynx-sc-homepage`.
	* Includes:
		- `make clean`: 
			* Cleans out cruft from this directory.
		- `make install`: 
			* Installs `newslynx-sc-homepage`. Assumes that you're in a virtual environment.
		- `make all_tests`: 
			* Runs the tests.
		- `make readme`
			* Converts this file to `.rst`, including a table of contents, and saves it to [docs/index.rst](https://github.com/newslynx/newslynx-sc-homepage/blob/master/docs/index.rst)
		- `make sous_chef_docs`
			* Programmtically generates [Sous Chef documentation](https://github.com/newslynx/newslynx-sc-homepage/blob/master/docs/sous-chefs.rst) by running `newslynx sc-docs newslynx_sc_homepage/ --format=rst > docs/sous-chefs.rst`.
		- `make all_docs`: 
			* Builds the sphinx docs for `newslynx-sc-homepage` by running the above two commands.
		- `make view_docs`
			* Serves documentation at [localhost:8000](http://localhost:8000)
		- `make register`: 
			* Registers `newslynx-sc-homepage` on [PyPI](https://pypi.python.org/pypi).
		- `make distribute`: 
			* Publishes a new version of `newslynx-sc-homepage` to PyPI.

- [CONTRIBUTING.md](https://github.com/newslynx/newslynx-sc-homepage/blob/master/CONTRIBUTING.md)

- [newslynx_sc_homepage](https://github.com/newslynx/newslynx-sc-homepage/blob/master/newslynx_sc_homepage/)
	* `newslynx-sc-homepage`'s source code and Sous Chef configuration files.

- [docs](https://github.com/newslynx/newslynx-sc-homepage/blob/master/docs/)
	* Sphnix documentation for `newslynx-sc-homepage`

- [tests](https://github.com/newslynx/newslynx-sc-homepage/blob/master/tests/)
	* `nose` tests for `newslynx-sc-homepage`

