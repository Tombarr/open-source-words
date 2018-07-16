headroom js give your pages some headroom hide your header until you need it whats it all about headroom js is a lightweight high performance js widget with no dependencies that allows you to react to the users scroll the header on this site is a living example it slides out of view when scrolling down and slides back in when scrolling up why use it fixed headers are a popular approach for keeping the primary navigation in close proximity to the user this can reduce the effort required for a user to quickly navigate a site but they are not without problems… large screens are usually landscape oriented meaning less vertical than horizontal space a fixed header can therefore occupy a significant portion of the content area small screens are typically used in a portrait orientation whilst this results in more vertical space because of the overall height of the screen a meaningfully sized header can still be quite imposing headroom js allows you to bring elements into view when appropriate and give focus to your content the rest of the time how does it work at its most basic headroom js simply adds and removes css classes from an element in response to a scroll event this means you must supply your own css styles separately the classes that are used in headroom js that are added and removed are html initially scrolling down scrolling up relying on css classes affords headroom js incredible flexibility the choice of what to do when scrolling up or down is now entirely yours anything you can do with css you can do in response to the users scroll usage using headroom js is really simple it has a pure js api plus an optional jquery zepto plugin and angularjs directive install with npm bash npm install headroom js save install with bower bash bower install https unpkg com headroom js bower zip save using headroom js with a cdn a universal build suitable for script tags commonjs and amd is available from unpkg com https unpkg com headroom js https unpkg com headroom js with pure js include the headroom js script in your page and then js grab an element var myelement document queryselector header construct an instance of headroom passing the element var headroom new headroom myelement initialise headroom init with jquery zepto include the headroom js and jquery headroom js scripts in your page and then js simple as this note init is implicitly called with the plugin header headroom the plugin also offers a data api if you prefer a declarative approach html selects data headroom note zeptos additional data module https github com madrobby zepto zepto modules is required for compatibility with angularjs include the headroom js and angular headroom js scripts in your page and include the headroom module javascript angular module app your requires headroom and then use the directive in your markup html or or with options note in angularjs you cannot pass a dom element as a directive attribute instead you have to provide a selector that can be passed to angular element http docs angularjs org api ng function angular element if you use default angularjs jqlite selector engine here are the compliant selectors https code google com p jqlite wiki usingjqlite options headroom js can also accept an options object to alter the way it behaves you can see the default options by inspecting headroom options the structure of an options object is as follows js vertical offset in px before element is first unpinned offset 0 scroll tolerance in px before state changes tolerance 0 or scroll tolerance per direction tolerance down 0 up 0 element which is source of scroll events defaults to window scroller element css classes to apply classes when element is initialised initial headroom when scrolling up pinned headroom pinned when scrolling down unpinned headroom unpinned when above offset top headroom top when below offset nottop headroom not top when at bottom of scoll area bottom headroom bottom when not at bottom of scroll area notbottom headroom not bottom callback when pinned this is headroom object onpin function callback when unpinned this is headroom object onunpin function callback when above offset this is headroom object ontop function callback when below offset this is headroom object onnottop function callback at bottom of page this is headroom object onbottom function callback when moving away from bottom of page this is headroom object onnotbottom function examples head over to the headroom js playroom http wicky nillia ms headroom js playroom if you want see some example usages there you can tweak all of headrooms options and apply different css effects in an interactive demo browser support headroom js is dependent on the following browser apis requestanimationframe http caniuse com feat requestanimationframe classlist http caniuse com feat classlist function prototype bind https developer mozilla org en us docs web javascript reference global objects function bind browser compatibility all of these apis are capable of being polyfilled so headroom js can work with less capable browsers if desired check the linked resources above to determine if you must polyfill to achieve your desired level of browser support contributions issues contributions are welcome please clearly explain the purpose of the pr and follow the current style issues can be resolved quickest if they are descriptive and include both a reduced test case and a set of steps to reproduce license licensed under the mit license http www opensource org licenses mit license php