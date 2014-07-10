xscreensaver-watcher
====================

A tool to watch [xscreensaver](http://www.jwz.org/xscreensaver/man3.html) events and invoke programs on lock/unlock.

This initial version demonstrates this by watching for lock/unlock events, and invoking Clementine's pause and start commands.

### Installation
Put a copy of these scripts (via symlink or whatnot) into `~/bin/` or someplace useful.  Right now, this assumes that you have both xscreensaver and Clementine installed.

### Usage:
Once per login, invoke this:

```bash
xscreensaver-command -watch | python ~/bin/xscreensaver-watcher.py
```

I've included a shell script that can be used to do this for convenience:

```bash
~/bin/clementine-screensaver-watcher.sh > /dev/null &
```

### Test/demo:
Fixtures are provided which demonstrate recognition of lock/unlock events.  Since the watcher script is not yet generalized, these will cause Clementine to pause/start. ;-)
```bash
# Note that this will invoke pause in Clementine.
python xscreensaver-watcher.py < fixtures/lock-example.txt
```

### Future plans:

I should refactor this so that the invocation of things when we see xscreensaver events is separated from whether we run clementine, or any other command.
