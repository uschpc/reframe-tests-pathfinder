# Using ReFrame on the Pathfinder testbed cluster

## Installing ReFrame

Currently, tests are developed and run using ReFrame v4.6.2. A shared installation is available on Pathfinder in `/home/hpcroot/rfm/reframe-4.6.2`.

The following steps were used to install ReFrame:

```
cd /home/hpcroot/rfm
module purge
module load gcc/13.3.0 python/3.11.9 curl tar gzip
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v4.6.2.tar.gz
tar -xf v4.6.2.tar.gz
rm v4.6.2.tar.gz
cd reframe-4.6.2
./bootstrap.sh
py="$(type -p python3)"
sed -i "1s%.*%#\!${py}%" ./bin/reframe
unset py
module purge
cd ..
chmod -R ug-w reframe-4.6.2
./reframe-4.6.2/bin/reframe -V
```

## Installing the Pathfinder test suite

A shared installation of the test suite is available on Pathfinder in `/home/hpcroot/rfm/reframe-tests-pathfinder`.

To install the test suite, clone the repo:

```
git clone https://github.com/uschpc/reframe-tests-pathfinder.git
cd reframe-tests-pathfinder
```

## Listing and validating tests

To list and validate tests, use the `--list` option:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/ --list
```

The `-C` option specifies the path to a configuration file, and the `-c` option specifies the path to the test files.

## Running tests

The ReFrame tests can be run individually, as a subset, or as the entire suite. To run tests, use the `-r` option.

### Individual test

To run an individual test, use the path to the test file. For example:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/julia-pi.py -r
```

### Subset of tests

To run a subset of tests, use the `-n` option with grep-like syntax. For example:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/ -n 'Python|Julia' -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition. For example:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/ --system=pathfinder:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` and `--distribute` options. For example:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/julia-pi.py --system=pathfinder:compute --distribute=all -r
```

### Entire test suite

To run the entire suite of tests, use the path to the tests directory:

```
cd /home/hpcroot/rfm
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/ -r
```

## Checking test logs

Various log files can be found in `/home/hpcroot/rfm/`.

## Reference guide for test suite

A reference guide for specific tests to run during testing or maintenance periods.

```
module purge
cd /home/hpcroot/rfm

# All tests
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/ -r

# Test every node using Julia test
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/julia-pi.py --distribute=all -r

# Test every node using file download test
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/file-download.py --distribute=all -r

# Test every node using container test
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/container-hello.py --distribute=all -r

# Test GPU access for every node in gpu partition
./reframe-4.6.2/bin/reframe -C ./reframe-tests-pathfinder/config/pathfinder.py -c ./reframe-tests-pathfinder/tests/container-gpu-hello.py --distribute=all -r
```
