COMPILER = python3
FLAGS = 
FILES = solution.py
# FILES = zoombot.py
# DIR = zoombot

all: main

main: $(FILES)
	$(COMPILER) $(FLAGS) $^

clean:
	rm -rf __pycache__

.PHONY: clean all