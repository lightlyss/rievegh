.PHONY: clean

clean:
	$(RM) *.txt game/*.rpyc
	$(RM) -r game/cache game/saves
