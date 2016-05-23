RESORT
======

Release
-------

Package should be registered at [PyPI](https://pypi.python.org) with

```
$ python3 setup.py register
```

On branch ``develop``, change version in ``package.ini`` file, commit changes
and execute

```
$ python3 setup.py sdist bdist_wheel upload
$ git tag -a <version> -m "<version_description>"
$ git push <remote> <version>
$ git checkout master
$ git merge --no-ff --no-edit develop
$ git push <remote> master
$ git checkout develop
```

Documentation
-------------

On branch ``develop``, execute

```
$ git push <remote> :gh-pages
$ python3 setup.py build_sphinx
$ mkdir .tmp
$ mv docs/build/html/* .tmp
$ git checkout --orphan gh-pages
$ rm -rf *
$ mv .tmp/* .
$ rm -rf .tmp
$ touch .nojekyll
$ git add --all .
$ git commit -m "Project doumentation"
$ git push <remote> gh-pages
$ git checkout develop
$ git branch -D gh-pages
```

Documentation will be available [here](http://miquelo.github.io/resort/).

