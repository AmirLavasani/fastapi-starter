"""
Version Information

This module provides the version of the code, and it is autogenerated by the `python-semantic-release` package.
DO NOT EDIT IT MANUALLY.

[Python Semantic Release (PSR)](https://python-semantic-release.readthedocs.io/en/latest/) is a tool that can
automatically bump version numbers based on keywords it finds in commit messages. The idea is to use a standardized
commit message format and syntax, which PSR can parse to determine how to increment the version number.
The default commit message format used by PSR is the [Angular commit style]
(https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commit-message-format), which looks like this:


    <type>(optional scope): short summary in present tense

    (optional body: explains motivation for the change)

    (optional footer: note BREAKING CHANGES here, and issues to be closed)


<type> refers to the kind of change made and is usually one of:

* feat: A new feature.

* fix: A bug fix.

* docs: Documentation changes.

* style: Changes that do not affect the meaning of the code (white-space, formatting,
    missing semi-colons, etc).

* refactor: A code change that neither fixes a bug nor adds a feature.

* perf: A code change that improves performance.

* test: Changes to the test framework.

* build: Changes to the build process or tools.

scope is an optional keyword that provides context for where the change was made. It can
be anything relevant to your package or development workflow (e.g., it could be the module or
function name affected by the change).

Different text in the commit message will trigger PSR to make different kinds of releases:

* A <type> of fix triggers a patch version bump, e.g.:

$ git commit -m "fix(mod_plotting): fix confusing error message in plot_words"


* A <type> of feat triggers a minor version bump, e.g.:

$ git commit -m "feat(package): add example data and new module to package"


* The text BREAKING CHANGE: in the footer will trigger a major release, e.g.:

$ git commit -m "feat(mod_plotting): move code from plotting module to pycounts module
$
$               BREAKING CHANGE: plotting module wont exist after this release."

"""
__version__ = "0.4.0"
