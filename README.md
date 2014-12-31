pre-commit-reject-large-files
=============================

This is a [pre-commit](https://github.com/pre-commit) hook that will reject
large files.

* [pre-commit](https://github.com/pre-commit)


Add this to your ``.pre-commit-config.yaml`` file

    -   repo: git://github.com/guykisel/pre-commit-reject-large-files
        sha: <latest git hash>
        hooks:
        -   id: reject-large-files

Available flags:

* ``--max_filesize``: Maximum allowable filesize in bytes. Defaults to 5 MB (5242880 bytes).
