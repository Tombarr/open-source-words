announcement emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp version 6 0 0 is now released read the changelog changelog md 600 september 19 2017 emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp emsp rxdb a reactive offline first database for javascript documentation example projects a href https www patreon com rxdb img src https cdn rawgit com pubkey rxdb 4e7dd18f docs files icons patreon png width 111px a features multiplatform support for browsers nodejs electron cordova react native and every other javascript runtime reactive data handling based on rxjs replication between client and server data compatible with pouchdb couchdb and ibm cloudant schema based with the easy to learn standard of jsonschema mango query exactly like you know from mongodb and mongoose encryption of single data fields to protect your users data import export of the database state json awesome for coding with tdd multi window to synchronise data between different browser windows or nodejs processes orm capabilities to easily handle data code relations platform support rxdb is made so that you can use exactly the same code at browsers nodejs electron react native cordova phonegap nativescript we optimized double checked and made boilerplates so you can directly start to use rxdb with frameworks like react angular ng2 ionic2 vuejs quickstart installation sh npm install rxdb save peerdependencies npm install rxjs babel polyfill save import es7 javascript import babel polyfill only needed when you dont have polyfills import rxdb from rxdb const db await rxdb create name heroesdb adapter websql password mylongandstupidpassword optional multiinstance true default true create database await db collection name heroes schema myschema create collection db heroes insert name bob insert document es5 javascript require babel polyfill only needed when you dont have polyfills var rxdb require rxdb rxdb create name heroesdb adapter websql password mylongandstupidpassword optional multiinstance true default true create database then function db return db collection name heroes schema myschema create collection then function collection collection insert name bob insert document feature showroom click to toggle mango query to find data in your collection use the mquery api to create chained mango queries which you maybe know from mongodb or mongoose javascript mycollection find where name ne alice where age gt 18 lt 67 limit 10 sort age exec then docs console dir docs reactive rxdb implements rxjs to make your data reactive this makes it easy to always show the real time database state in the dom without manually re submitting your queries javascript db heroes find sort name returns observable of query subscribe docs mydomelement innerhtml docs map doc li doc name li join multiwindow tab when two instances of rxdb use the same storage engine their state and action stream will be broadcasted this means with two browser windows the change of window 1 will automatically affect window 2 this works completely offline replication because rxdb relies on glorious pouchdb it is easy to replicate the data between devices and servers and yes the changeevents are also synced schema schemas are defined via jsonschema and are used to describe your data javascript const myschema title hero schema version 0 incremental version number description describes a simple hero type object properties name type string primary true this means unique required string and will be used as id secret type string encrypted true this means that the value of this field is stored encrypted skills type array maxitems 5 uniqueitems true item type object properties name type string damage type number required color encryption by setting a schema field to encrypted true the value of this field will be stored in encryption mode and cant be read without the password of course you can also encrypt nested objects example json secret type string encrypted true level adapters the underlying pouchdb can use different adapters as storage engine so you can use rxdb in different environments by just switching the adapter for example you can use websql in the browser localstorage in mobile browsers and a leveldown adapter in nodejs js this requires the localstorage adapter rxdb plugin require pouchdb adapter localstorage this creates a database with the localstorage adapter const db await rxdb create heroesdb localstorage some adapters you can use indexeddb localstorage fruitdown memory websql or any leveldown adapter import export rxdb lets you import and export the whole database or single collections into json objects this is helpful to trace bugs in your application or to move to a given state in your tests js export a single collection const jsoncol await mycollection dump export the whole database const jsondb await mydatabase dump import the dump to the collection await emptycollection importdump json import the dump to the database await emptydatabase importdump json leader election imagine your website needs to get a piece of data from the server once every minute to accomplish this task you create a websocket or pull interval if your user now opens the site in 5 tabs parallel it will run the interval or create the socket 5 times this is a waste of resources which can be solved by rxdbs leaderelection js myrxdatabase waitforleadership then this will only run when the instance becomes leader mysocket createwebsocket in this example the leader is marked with the crown ♛ key compression depending on which adapter and in which environment you use rxdb client side storage is limited in some way or the other to save disc space rxdb has an internal schema based key compression to minimize the size of saved documents example js when you save an object with big keys await mycollection insert firstname foo lastname bar stupidlongkey 5 rxdb will internally transform it to a foo b bar c 5 so instead of 46 chars the compressed version has only 28 the compression works internally so you can of course still access values via the original key names console log mydoc firstname foo querychangedetection similar to meteors oplog observe driver rxdb has a querychangedetection to optimize observed or reused queries this makes sure that when you update insert remove documents the query does not have to re run over the whole database but the new results will be calculated from the events this creates a huge performance gain with zero cost the querychangedetection works internally and is currently in beta disabled by default use case example imagine you have a very big collection with many user documents at your page you want to display a toplist with users which have the most points and are currently logged in you create a query and subscribe to it js const query userscollection find where loggedin eq true sort points query subscribe users document queryselector body innerhtml users reduce prev cur prev cur username br as you may detect the query can take very long time to run because you have thousands of users in the collection when a user now logs off the whole query will re run over the database which takes again very long js anyuser loggedin false await anyuser save but not with the querychangedetection enabled now when one user logs off it will calculate the new results from the current results plus the rxchangeevent this often can be done in memory without making io requests to the storage engine the querychangedetection not only works on subscribed queries but also when you do multiple exec s on the same query browser support all major evergreen browsers and ie11 are supported tests automatically run against firefox and chrome and manually in a virtualbox for ie11 and edge as rxdb heavily relies on pouchdb see their browser support for more information also do keep in mind that different browsers have different storage limits especially on mobile devices getting started get started now by reading the docs or exploring the example projects contribute check out how you can contribute to this project follow up follow rxdb on twitter to not miss the latest enhancements join the chat on gitter for discussion thank you a big thank you to every contributor of this project license apache 2 0