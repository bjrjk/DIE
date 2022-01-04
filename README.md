# DIE

Repository for "Fuzzing JavaScript Engines with Aspect-preserving Mutation" (in S&P'20).

## General Setup

For nodejs and npm,
```
$ sudo apt -y install npm
$ sudo npm install -g n
$ sudo n stable
```
For redis,
```
$ sudo apt install redis-server
```

To compile afl, afl-fast & JS Engines smoothly,
```
$ sudo apt -y install build-essential cmake clang clang-6.0 llvm 
```

## DIE Setup

To setup environment for AFL,
```
$ sudo sh fuzz/scripts/prepare.sh
```

To compile whole project,
```
$ sh fuzz/scripts/compile.sh
```

To set the configurations,
```
$ nano fuzz/scripts/config.py
```


### Typer
To install d8,

```
pushd engines/utils
sh fetch_depot_tools.sh
popd

pushd engines
./download-engine.sh v8 latest
./build-v8.sh latest
```

We used d8 to profile type information. So, please change 
d8_path in fuzz/TS/typer/typer.py before execution.

```
cd fuzz/TS/typer
python3 typer.py [corpus directory]
```
\*.jsi file will be created if instrumentation works well. 

\*.t file will be created if profiling works well.

### Server Setup
* Make Corpus Directory
(We used [Die-corpus](https://github.com/sslab-gatech/DIE-corpus.git) as corpus)
```
$ git clone https://github.com/sslab-gatech/DIE-corpus.git
$ python3 ./fuzz/scripts/make_initial_corpus.py ./DIE-corpus ./corpus
```
* Make ssh-tunnel for connection with redis-server
```
$ ./fuzz/scripts/redis.py
```
* Dry run with corpus
```
$ ./fuzz/scripts/populate.sh [target binary path] [path of DIE-corpus dir] [target js engine (ch/jsc/v8/ffx)]
# Example
$ ./fuzz/scripts/populate.sh ~/ch ./DIE-corpus ch
```
It's done! Your corpus is well executed and the data should be located on redis-server.

#### Tips
To check the redis-data,
```
$ redis-cli -p 9000
127.0.0.1:9000> keys *
```
If the result contains "crashBitmap", "crashQueue", "pathBitmap", "newPathsQueue" keys, the fuzzer was well registered and executed.


### Client Setup
* Make ssh-tunnel for connection with redis-server
```
$ ./fuzz/scripts/redis.py
```

* Usage
```
$ ./fuzz/scripts/run.sh [target binary path] [path of DIE-corpus dir] [target js engine (ch/jsc/v8/ffx)]
# Example
$ ./fuzz/scripts/run.sh ~/ch ./DIE-corpus ch
```

* Check if it's running
```
$ tmux ls
```
You can find a session named `fuzzer` if it's running.

## CVEs
If you find bugs and get CVEs by running DIE, please let us know.

* ChakraCore: CVE-2019-0609, CVE-2019-1023, CVE-2019-1300, CVE-2019-0990, CVE-2019-1092
* JavaScriptCore: CVE-2019-8676, CVE-2019-8673, CVE-2019-8811, CVE-2019-8816
* V8: CVE-2019-13730, CVE-2019-13764, CVE-2020-6382

# Paper: Fuzzing JavaScript Engines with Aspect-preserving Mutation

You can check the [paper](https://gts3.org/assets/papers/2020/park:die.pdf) for technical details.

## Contacts

* Soyeon Park <soyeon@gatech.edu>
* Wen Xu <wen.xu@gatech.edu>
* Insu Yun <insu@gatech.edu>
* Daehee Jang <daehee87@gatech.edu>
* Taesoo Kim <taesoo@gatech.edu>

## Paper Citation

```
@inproceedings{park:die,
  title        = {{Fuzzing JavaScript Engines with Aspect-preserving Mutation}},
  author       = {Soyeon Park and Wen Xu and Insu Yun and Daehee Jang and Taesoo Kim},
  booktitle    = {Proceedings of the 41st IEEE Symposium on Security and Privacy (Oakland)},
  month        = may,
  year         = 2020,
  address      = {San Francisco, CA},
}
```