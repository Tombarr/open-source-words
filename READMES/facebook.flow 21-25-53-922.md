flow flow is a static typechecker for javascript to find out more about flow check out flow org for a background on the project please read this overview requirements flow works with mac os x linux 64 bit windows 64 bit there are binary distributions for each of these platforms and you can also build it from source on any of them as well installing flow flow is simple to install all you need is the flow binary on your path and youre good to go installing flow per project the recommended way to install flow is via the flow bin npm package adding flow bin to your projects package json provides a smoother upgrade experience since the correct version of flow is automatically used based on the revision you check out installs flow as part of your existing npm install workflow lets you use different versions of flow on different projects npm install save dev flow bin node modules bin flow installing flow globally although not recommended you can also install flow globally for example perhaps you dont use npm or package json the best way to install globally is via flow bin npm install g flow bin flow make sure npm bin g is on your path on mac os x you can install flow via the homebrew package manager brew update brew install flow you can also build and install flow via the ocaml opam package manager since flow has some non ocaml dependencies you need to use the depext package like so opam install depext opam depext install flowtype if you dont have a new enough version of ocaml to compile flow you can also use opam to bootstrap a modern version install opam via the binary packages for your operating system and run opam init comp 4 05 0 opam install flowtype eval opam config env flow help getting started getting started with flow is super easy initialize flow by running the following command in the root of your project flow init add the following to the top of all the files you want to typecheck javascript flow run and see the magic happen flow check more thorough documentation and many examples can be found at https flow org building flow flow is written in ocaml ocaml 4 05 0 or higher is required you can install ocaml on mac os x and linux by following the instructions at ocaml org for example on ubuntu 16 04 and similar systems sudo apt get install opam opam init comp 4 05 0 on os x using the brew package manager brew install opam opam init comp 4 05 0 then restart your shell and install these additional libraries opam update opam pin add flowtype n opam install deps only flowtype once you have these dependencies building flow just requires running make this produces a bin folder containing the flow binary in order to make the flow js file you first need to install js of ocaml opam install y js of ocaml after that making flow js is easy make js the new flow js file will also live in the bin folder note at this time the ocaml dependency prevents us from adding flow to npm try flow bin if you need a npm binary wrapper flow can also compile its parser to javascript read how here building flow on windows this is a little more complicated here is a process that works though it probably can be simplified the general idea is that we build in cygwin targeting mingw this gives us a binary that works even outside of cygwin install cygwin install cygwin 64bit from https cygwin com install html in powershell run iex new object net webclient downloadstring https raw githubusercontent com ocaml ocaml ci scripts master appveyor install ps1 which will likely run a cygwin setup installer with a bunch of cygwin packages and stuff this helps make sure that every package that opam needs is available install opam open the cygwin64 terminal download opam with curl fssl o opam64 tar xz https github com fdopen opam repository mingw releases download 0 0 0 1 opam64 tar xz tar xf opam64 tar xz cd opam64 install opam install sh initialize opam to point to a mingw fork opam init a default https github com fdopen opam repository mingw git comp 4 05 0 mingw64c switch 4 05 0 mingw64c make sure opam stuff is in your path eval opam config env install flow clone flow git clone https github com facebook flow git cd flow tell opam to use this directory as the flowtype project opam pin add flowtype n install system dependencies opam depext u flowtype install flows dependencies opam install flowtype deps only finally build flow make all using flows parser from javascript while flow is written in ocaml its parser is available as a compiled to javascript module published to npm named flow parser most end users of flow will not need to use this parser directly and should install flow bin from npm above but javascript packages which make use of parsing flow typed javascript can use this to generate flows syntax tree with annotated types attached running the tests to run the tests first compile flow using make then run bash runtests sh bin flow there is a make test target that compiles and runs tests to run a subset of the tests you can pass a second argument to the runtests sh file for example bash runtests sh bin flow class grep v skip join the flow community website https flow org irc flowtype on freenode twitter follow flowtype and flowtype to keep up with the latest flow news stack overflow ask a question with the flowtype tag license flow is mit licensed license the website and documentation are licensed under the creative commons attribution 4 0 license website license documentation