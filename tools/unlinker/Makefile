OUT_PATH=bin/unlinker

CC=g++
CPPFLAGS=-I${SRC_PATH}/lib -std=c++11 -g -Wall

bin/unlinker: unlinkfile.o
	@mkdir -p $(@D)
	${CC} $< -o $@

all: $(OUT_PATH)

clean:
	@rm -rf ${OUT_PATH}
	@rm *.o
