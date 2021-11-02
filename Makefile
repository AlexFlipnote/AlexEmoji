target: ;

build:
	sass scss:css --style compressed

dev:
	sass --watch scss:css --style compressed
