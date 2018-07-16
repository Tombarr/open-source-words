webassembly design this repository contains documents describing the design and high level overview of webassembly the documents and discussions in this repository are part of the webassembly community group overview webassembly or wasm is a new portable size and load time efficient format suitable for compilation to the web webassembly is currently being designed as an open standard by a w3c community group that includes representatives from all major browsers expect the contents of this repository to be in flux everything is still under discussion webassembly is efficient and fast wasm bytecode is designed to be encoded in a size and load time efficient binary format webassembly aims to execute at native speed by taking advantage of common hardware capabilities available on a wide range of platforms webassembly is safe webassembly describes a memory safe sandboxed execution environment that may even be implemented inside existing javascript virtual machines when embedded in the web webassembly will enforce the same origin and permissions security policies of the browser webassembly is open and debuggable webassembly is designed to be pretty printed in a textual format for debugging testing experimenting optimizing learning teaching and writing programs by hand the textual format will be used when viewing the source of wasm modules on the web webassembly is part of the open web platform webassembly is designed to maintain the versionless feature tested and backwards compatible nature of the web webassembly modules will be able to call into and out of the javascript context and access browser functionality through the same web apis accessible from javascript webassembly also supports non web embeddings more information resource repository location high level goals design highlevelgoals md frequently asked questions design faq md language specification spec readme md design process contributing the webassembly specification is being developed in the spec repository for now high level design discussions should continue to be held in the design repository via issues and pull requests so that the specification work can remain focused weve mapped out features we expect to ship an initial minimum viable product mvp release and soon after in future versions join us in the w3c community group its moderated announcement mailing list its open ended public discussion mailing list on irc irc irc w3 org 6667 webassembly on stack overflows webassembly tag by contributing when contributing please follow our code of ethics and professional conduct