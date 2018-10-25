package1 = RunRules 
package2 = ScanResources 
package3 = StoreResources
package4 = TagResources 
package5 = TaskScheduler

sphinx:
	cd docs && \
	make clean && \
	sphinx-apidoc -f -o source/generated/$(package1) ../$(package1) && \
	sphinx-apidoc -f -o source/generated/$(package2) ../$(package2) && \
	sphinx-apidoc -f -o source/generated/$(package3) ../$(package3) && \
	sphinx-apidoc -f -o source/generated/$(package4) ../$(package4) && \
	sphinx-apidoc -f -o source/generated/$(package5) ../$(package5) && \
	make html

ghpages:
	-git checkout gh-pages && \
	mv docs/build/html new-docs && \
	rm -rf docs && \
	mv new-docs docs && \
	cp -r docs/* . && \
	rm -rf docs && \
	touch .nojekyll && \
	git add . && \
	git commit -m "Updated generated Sphinx documentation"