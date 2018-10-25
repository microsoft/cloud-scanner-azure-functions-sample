sphinx:
	cd docs && \
	make clean && \
	sphinx-apidoc -f -o source/generated/RunRules ../RunRules && \
	sphinx-apidoc -f -o source/generated/ScanResources ../ScanResources && \
	sphinx-apidoc -f -o source/generated/StoreResources ../StoreResources && \
	sphinx-apidoc -f -o source/generated/TagResources ../TagResources && \
	sphinx-apidoc -f -o source/generated/TaskScheduler ../TaskScheduler && \
	make html