i also make caret a markdown editor for mac and pc parsedown a href https packagist org packages erusev parsedown klzzwxh 0002 a better markdown parser in php demo benchmarks tests documentation features one file no dependencies super fast extensible github flavored tested in 5 3 to 7 2 and in hhvm markdown extra extension installation composer install the composer package by running the following command composer require erusev parsedown manual download the source code from the latest release include parsedown php example php parsedown new parsedown echo parsedown text hello parsedown prints hello parsedown you can also parse inline markdown only echo parsedown line hello parsedown prints hello parsedown more examples in the wiki and in this video tutorial security parsedown is capable of escaping user input within the html that it generates additionally parsedown will apply sanitisation to additional scripting vectors such as scripting link destinations that are introduced by the markdown syntax itself to tell parsedown that it is processing untrusted user input use the following php parsedown new parsedown parsedown setsafemode true if instead you wish to allow html within untrusted user input but still want output to be free from xss it is recommended that you make use of a html sanitiser that allows html tags to be whitelisted like html purifier in both cases you should strongly consider employing defence in depth measures like deploying a content security policy a browser security feature so that your page is likely to be safe even if an attacker finds a vulnerability in one of the first lines of defence above security of parsedown extensions safe mode does not necessarily yield safe results when using extensions to parsedown extensions should be evaluated on their own to determine their specific safety against xss escaping html ⚠️ warning this method isnt safe from xss if you wish to escape html in trusted input you can use the following php parsedown new parsedown parsedown setmarkupescaped true beware that this still allows users to insert unsafe scripting vectors such as links like xss javascript alert 281 29 questions how does parsedown work it tries to read markdown like a human first it looks at the lines its interested in how the lines start this helps it recognise blocks it knows for example that if a line starts with a then perhaps it belongs to a list once it recognises the blocks it continues to the content as it reads it watches out for special characters this helps it recognise inline elements or inlines we call this approach line based we believe that parsedown is the first markdown parser to use it since the release of parsedown other developers have used the same approach to develop other markdown parsers in php and in other languages is it compliant with commonmark it passes most of the commonmark tests most of the tests that dont pass deal with cases that are quite uncommon still as commonmark matures compliance should improve who uses it laravel framework bolt cms grav cms herbie cms kirby cms october cms pico cms statamic cms phpdocumentor raspberrypi org symfony demo and more how can i help use it star it share it and if you feel generous donate