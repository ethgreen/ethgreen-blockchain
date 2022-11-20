from __future__ import annotations

import os

from setuptools import setup

dependencies = [
    "aiofiles==22.1.0",  # Async IO for files
    "blspy==1.0.16",  # Signature library
    "chiavdf==1.0.7",  # timelord and vdf verification
    "chiabip158==1.1",  # bip158-style wallet filters
    "chiapos==1.0.11",  # proof of space
    "clvm==0.9.7",
    "clvm_tools==0.4.5",  # Currying, Program.to, other conveniences
    "chia_rs==0.1.14",
    "clvm-tools-rs==0.1.24",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.8.3",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.5",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.20",  # Concurrently log and rotate logs
    "cryptography==36.0.2",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.8.0",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.6.0",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.2.3",  # Gives the ethgreen processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.2.1",  # Query DNS seeds
    "watchdog==2.1.9",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.22",  # dns lib
    "typing-extensions==4.3.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.2.6",
    "packaging==21.3",
    "psutil==5.9.1",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    "coverage",
    "diff-cover",
    "pre-commit",
    "py3createtorrent",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-cov",
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy",
    "black==22.8.0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.3",
    "types-aiofiles",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

kwargs = dict(
    name="ethgreen-blockchain",
    description="ETHgreen blockchain full node, farmer, timelord, and wallet.",
    url="https://eth-green.com/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="ethgreen blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "ethgreen",
        "ethgreen.cmds",
        "ethgreen.clvm",
        "ethgreen.consensus",
        "ethgreen.daemon",
        "ethgreen.data_layer",
        "ethgreen.full_node",
        "ethgreen.timelord",
        "ethgreen.farmer",
        "ethgreen.harvester",
        "ethgreen.introducer",
        "ethgreen.plot_sync",
        "ethgreen.plotters",
        "ethgreen.plotting",
        "ethgreen.pools",
        "ethgreen.protocols",
        "ethgreen.rpc",
        "ethgreen.seeder",
        "ethgreen.server",
        "ethgreen.simulator",
        "ethgreen.types.blockchain_format",
        "ethgreen.types",
        "ethgreen.util",
        "ethgreen.wallet",
        "ethgreen.wallet.db_wallet",
        "ethgreen.wallet.puzzles",
        "ethgreen.wallet.cat_wallet",
        "ethgreen.wallet.did_wallet",
        "ethgreen.wallet.nft_wallet",
        "ethgreen.wallet.settings",
        "ethgreen.wallet.trading",
        "ethgreen.wallet.util",
        "ethgreen.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "ethgreen = ethgreen.cmds.ethgreen:main",
            "ethgreen_daemon = ethgreen.daemon.server:main",
            "ethgreen_wallet = ethgreen.server.start_wallet:main",
            "ethgreen_full_node = ethgreen.server.start_full_node:main",
            "ethgreen_harvester = ethgreen.server.start_harvester:main",
            "ethgreen_farmer = ethgreen.server.start_farmer:main",
            "ethgreen_introducer = ethgreen.server.start_introducer:main",
            "ethgreen_crawler = ethgreen.seeder.start_crawler:main",
            "ethgreen_seeder = ethgreen.seeder.dns_server:main",
            "ethgreen_timelord = ethgreen.server.start_timelord:main",
            "ethgreen_timelord_launcher = ethgreen.timelord.timelord_launcher:main",
            "ethgreen_full_node_simulator = ethgreen.simulator.start_simulator:main",
            "ethgreen_data_layer = ethgreen.server.start_data_layer:main",
            "ethgreen_data_layer_http = ethgreen.data_layer.data_layer_server:main",
        ]
    },
    package_data={
        "ethgreen": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "ethgreen.util": ["initial-*.yaml", "english.txt"],
        "ethgreen.ssl": ["ethgreen_ca.crt", "ethgreen_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/ethgreen/ethgreen-blockchain/",
        "Changelog": "https://github.com/ethgreen/ethgreen-blockchain/blob/main/CHANGELOG.md",
    },
)


if len(os.environ.get("ETHGREEN_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
