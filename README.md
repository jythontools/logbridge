Logbridge
=========

The Logbridge project bridges Python's [logging][] library and the
[Simple Logging Facade for Java][SLF4J] (SLF4J). The actual code is
about 1 page of Python, so this is quite straightforward.

The rest of this README assumes the Jython command is aliased as
`jython27`. For more details on setting Jython up from source, refer
to the [Jython developer guide][].

Install Logbridge as usual into `site-packages`:

````bash
$ jython27 setup.py install
````

Tests will be formalized shortly. For now you can simply try this
example:

````bash
$ (cd tests && CLASSPATH=./slf4j-api-1.7.7.jar:./slf4j-simple-1.7.7.jar jython27 test_logbridge.py)
````

SLF4J always requires two jars. So assuming we are running 1.7.7 of
SLF4J, in the `CLASSPATH` - `slf4j-api-1.7.7.jar` for the API and a
specific logger like `slf4j-simple-1.7.7.jar`, which in this case
simply prints to stderr.

Configuring logging to use Logbridge is straightforward; we will
follow the example code in the tutorial on how to [configure
logging][] in Python.

```python
import logging
import logbridge


# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logbridge.SLF4JHandler()  # use SLF4J's root logger
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
````

Running the above script will result in the following output:

````
[MainThread] INFO ROOT - 2014-04-27 11:28:55,507 - simple_example - info message
[MainThread] WARN ROOT - 2014-04-27 11:28:55,509 - simple_example - warn message
[MainThread] ERROR ROOT - 2014-04-27 11:28:55,510 - simple_example - error message
[MainThread] ERROR ROOT - 2014-04-27 11:28:55,512 - simple_example - critical message
````

Note that besides using `logbridge.SLF4JHandler`, the format string is
changed so that the level name (eg `ERROR`) is not repeated, since
SLF4J will output this by default.


<!-- references -->

[configure logging]: https://docs.python.org/2/howto/logging.html#configuring-logging
[Jython developer guide]: https://wiki.python.org/jython/JythonDeveloperGuide
[logging]: https://docs.python.org/2/library/logging.html
[SLF4J]: http://www.slf4j.org/
