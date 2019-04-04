from setuptools import setup

setup(
    name="verocoin-server",
    version="1.0",
    scripts=['run_verocoin_server.py','verocoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'verocoinserver':'src'
        },
    py_modules=[
        'verocoinserver.__init__',
        'verocoinserver.utils',
        'verocoinserver.storage',
        'verocoinserver.deserialize',
        'verocoinserver.networks',
        'verocoinserver.blockchain_processor',
        'verocoinserver.server_processor',
        'verocoinserver.processor',
        'verocoinserver.version',
        'verocoinserver.ircthread',
        'verocoinserver.stratum_tcp'
    ],
    description="Bitcoin Verocoin Server",
    author="Thomas Voegtlin",
    author_email="thomasv@verocoin.org",
    license="MIT Licence",
    url="https://github.com/spesmilo/verocoin-server/",
    long_description="""Server for the Verocoin Lightweight Bitcoin Wallet"""
)
