RESORT
======

Documentation
-------------

To build documentation at GitHub Pages, at the project root path and
documentation branch, follow next steps. If *gf-pages* remote branch exists,
remove it.

```
$ python3 setup.py build_sphinx
$ mkdir .tmp
$ mv docs/build/html/* .tmp
$ git stash
$ git checkout --orphan gh-pages
$ rm -rf *
$ mv .tmp/* .
$ rm -rf .tmp
$ touch .nojekyll
$ git add --all .
$ git commit -m "Project doumentation"
$ git push <remote> gh-pages
$ git checkout <documentation_branch>
$ git branch -D gh-pages
$ git stash pop
```

Documentation will be available [here](http://miquelo.github.io/resort/).

Release
-------

Package should be registered at [PyPI](https://pypi.python.org) with

```
$ python3 setup.py register
```

On branch ``develop``, change version in ``setup.py`` file, commit changes and
execute

```
$ python3 setup.py sdist bdist_wheel upload
$ git tag -a <version> -m "<version_description>"
$ git push origin <version>
```

