# Autor: Kevin Uriarte
# Fecha: 2026-04-16

CC=clang
CFLAGS=-fPIC -O2 -g
LDFLAGS=-shared

BUILD=build
TARGET=$(BUILD)/libops.so

all: $(BUILD) $(TARGET)

$(BUILD):
	mkdir -p $(BUILD)

$(TARGET): $(BUILD) bridge.o
	$(CC) $(LDFLAGS) -o $@ bridge.o

bridge.o: bridge.c
	$(CC) $(CFLAGS) -c bridge.c

clean:
	rm -rf *.o $(BUILD)
