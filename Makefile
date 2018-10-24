package = ../RunRules

sphinx:
	cd docs && \
	make clean && \
	sphinx-apidoc -f -o source/generated $(package) && \
	make html
