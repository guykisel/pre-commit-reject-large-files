import pkg_resources

__version__ = pkg_resources.get_distribution(
    "pre_commit_reject_large_files").version
