-include ./path.mak

CC := $(LINUXarm_GCC)
CFLAGS := -g
LINKER_FLAGS := -lstdc++

all: app.arm

app.arm: app.o
	$(CC) $(CFLAGS) $(LINKER_FLAGS) $^ -o $@
	@echo; echo $@ successfully create; echo

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

test:
	@echo CC = $(CC)

clean:
	rm -rf  app.o
	rm -rf app.arm
