clean:
	rm -rf ./**/__pycache__
	rm -rf ./*.egg-info
	rm -rf ./build
	rm -rf ./dist

freeze:
	pip freeze | grep -v "pkg-resources" > ./requirements.txt