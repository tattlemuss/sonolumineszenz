
CC=g++
CPPFLAGS=-I${SRC_PATH}/lib -std=c++11 -g -Wall


all: bin/unlinker bin/linkfile

bin/unlinker: unlinkfile.o
	@mkdir -p $(@D)
	${CC} $< -o $@

bin/linkfile: linkfile.o
	@mkdir -p $(@D)
	${CC} $< -o $@

clean:
	@rm -rf ${OUT_PATH}
	@rm *.o
