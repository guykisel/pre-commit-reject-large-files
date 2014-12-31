pre-commit-reject-large-files
=============================

This is a [pre-commit](https://github.com/pre-commit) hook that will reject
large files.

* [pre-commit](https://github.com/pre-commit)

Inspired by [Albert-Jan Roskam's git hook](http://code.activestate.com/recipes/578883-git-pre-commit-hook-to-reject-large-files-using-py/).


Add this to your ``.pre-commit-config.yaml`` file

    -   repo: git://github.com/guykisel/pre-commit-reject-large-files
        sha: da21f6dac1aa20aa53598b145c5c0013cdd40d65
        hooks:
        -   id: reject-large-files

Available flags:

* ``--max-filesize``: Maximum allowable filesize in bytes. Defaults to 5 MB (5242880 bytes).
