grumpy go running python overview grumpy is a python to go source code transcompiler and runtime that is intended to be a near drop in replacement for cpython 2 7 the key difference is that it compiles python source code to go source code which is then compiled to native code rather than to bytecode this means that grumpy has no vm the compiled go source code is a series of calls to the grumpy runtime a go library serving a similar purpose to the python c api although the api is incompatible with cpythons limitations things that will probably never be supported by grumpy exec eval and compile these dynamic features of cpython are not supported by grumpy because grumpy modules consist of statically compiled go code supporting dynamic execution would require bundling grumpy programs with the compilation toolchain which would be unwieldy and impractically slow c extension modules grumpy has a different api and object layout than cpython and so supporting c extensions would be difficult in principle its possible to support them via an api bridge layer like the one that jyni provides for jython but it would be hard to maintain and would add significant overhead when calling into and out of extension modules things that grumpy will support but doesnt yet there are three basic categories of incomplete functionality language features most language features are implemented with the notable exception of old style classes there are also a handful of operators that arent yet supported builtin functions and types there are a number of missing functions and types in builtins that have not yet been implemented there are also a lot of methods on builtin types that are missing standard library the python standard library is very large and much of it is pure python so as the language features and builtins get filled out many modules will just work but there are also a number of libraries in cpython that are c extension modules which will need to be rewritten c locale support go doesnt support locales in the same way that c does as such some functionality that is locale dependent may not currently work the same as in cpython running grumpy programs method 1 make run the simplest way to execute a grumpy program is to use make run which wraps a shell script called grumprun that takes python code on stdin and builds and runs the code under grumpy all of the commands below are assumed to be run from the root directory of the grumpy source code distribution echo print hello world make run method 2 grumpc and grumprun for more complicated programs youll want to compile your python source code to go using grumpc the grumpy compiler and then build the go code using go build since grumpy programs are statically linked all the modules in a program must be findable by the grumpy toolchain on the gopath grumpy looks for go packages corresponding to python modules in the python subdirectory of the gopath by convention this subdirectory is also used for staging python source code making it similar to the pythonpath the first step is to set up the shell so that the grumpy toolchain and libraries can be found from the root directory of the grumpy source distribution run make export path pwd build bin path export gopath pwd build export pythonpath pwd build lib python2 7 site packages you will know things are working if you see the expected output from this command echo import sys print sys version grumprun next we will write our simple python module into the python directory echo def hello print hello world gopath src python hello py to build a go package from our python script run the following mkdir p gopath src python hello grumpc modname hello gopath src python hello py \ gopath src python hello module go you should now be able to build a go program that imports the package python hello we can also import this module into python programs that are built using grumprun echo from hello import hello hello grumprun grumprun is doing a few things under the hood here compiles the given python code to a dummy go package the same way we produced python hello module go above produces a main go package that imports the go package from step 1 and executes it as our main python package executes go run on the main package generated in step 2 developing grumpy there are three main components and depending on what kind of feature youre writing you may need to change one or more of these grumpc grumpy converts python programs into go programs and grumpc is the tool responsible for parsing python code and generating go code from it grumpc is written in python and uses the pythonparser module to accomplish parsing the grumpc script itself lives at tools grumpc it is supported by a number of python modules in the compiler subdir grumpy runtime the go code generated by grumpc performs operations on data structures that represent python objects in running grumpy programs these data structures and operations are defined in the grumpy go library source is in the runtime subdir of the source distribution this runtime is analogous to the python c api and many of the structures and operations defined by grumpy have counterparts in cpython grumpy standard library much of the python standard library is written in python and thus just works in grumpy these parts of the standard library are copied from cpython 2 7 possibly with light modifications for licensing reasons these files are kept in the third party subdir the parts of the standard library that cannot be written in pure python e g file and directory operations are kept in the lib subdir in cpython these kinds of modules are written as c extensions in grumpy they are written in python but they use native go extensions to access facilities not otherwise available in python source code overview compiler python package implementating python go transcompilation logic lib grumpy specific python standard library implementation runtime go source code for the grumpy runtime library third party ouroboros pure python standard libraries copied from the ouroboros project third party pypy pure python standard libraries copied from pypy third party stdlib pure python standard libraries copied from cpython tools transcompilation and utility binaries contact questions comments drop us a line at grumpy users googlegroups com or join our gitter channel