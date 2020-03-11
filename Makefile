SRC=$(shell find . -mindepth 3 -maxdepth 3 -type f -name *.po)
OBJ=$(patsubst %.po,%.mo,$(SRC))
%.mo : %.po
	msgfmt -o $@ $<


all: $(OBJ)
