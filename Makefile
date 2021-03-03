# Deployment instructions
# 0. Fill in `pypirc.sample`, and `cp pypirc.sample ~/.pypirc`
# 1. Check changelogs.rst and check if documents are up-to-date (Make show_docs, make show_docs_ko will help you out. Requirements can be installed by `git submodule init; git submodule update`.)
# 2. Check translations at docs/locale/ko/LC_MESSAGES/*.po
# 3. Check version at konlpy/konlpy/about.py
# 4. $ make testpypi
# 5. $ make pypi  # Beware not to change the version number at this stage!!!
# 6. Document update at RTD (latest)
# 7. Push tag
# 8. Document update at RTD (current version)
#
# TODO: use flake8 and/or pylint

build:
	python setup.py sdist --formats=gztar,zip

check:
	check-manifest \
	--ignore