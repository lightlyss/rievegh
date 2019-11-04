.PHONY: clean

clean:
	$(RM) *.txt game/*.rpyc game/camera/*.rpyc
	$(RM) -r game/cache game/saves
