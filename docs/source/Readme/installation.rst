Sphinx Tool Installation
-------------------------------------------

PlantUML requires java runtime environment installed. If you don’t have already Java Runtime Environment installed on your computer, you can download if from http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html




Windows
=======

1. Download latest Python 2.7 https://www.python.org/downloads/windows/

2. Install Python.

3. Add Python and Python Scripts directories to Windows PATH variable.

    1. Open Control Panel -> System -> Advanced system settings

        .. image:: advanced_system_settings.png

    2. Click on "Environment Variables" button.

        .. image:: environment_variables.png

    3. Add *C:\\Python27* and *C:\\Python27\\Scripts* to PATH variable.

        .. image:: edit_path.png

4.  Execute following commands.

    .. code-block:: sh
    
        pip install sphinx --proxy http://defra1c-proxy.emea.nsn-net.net:8080
        pip install plantuml --proxy http://defra1c-proxy.emea.nsn-net.net:8080
        pip install sphinxcontrib-plantuml  --proxy http://defra1c-proxy.emea.nsn-net.net:8080


Linux (LinSee server)
=====================

To install all dependencies:

1. Checkout https://wrscmi.inside.nsn.com/isource/svnroot/BTS_DOCS_SMALLCELLS/trunk

2. Install sphinx & dependencies.

    .. code-block:: sh

        pip install --user sphinx
        pip install --user plantuml
        pip install --user sphinxcontrib-plantuml

3. Execute script from trunk directory

    .. code-block:: sh

        ./init_linux.sh


Linux
=====

1. Install Python

    .. code-block:: sh
       
       sudo apt-get install python2.7

2. Install sphinx & dependencies.

    .. code-block:: sh

        pip install sphinx
        pip install plantuml
        pip install sphinxcontrib-plantuml
