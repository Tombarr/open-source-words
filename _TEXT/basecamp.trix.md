trix a rich text editor for everyday writing compose beautifully formatted text in your web application trix is a wysiwyg editor for writing messages comments articles and lists—the simple documents most web apps are made of it features a sophisticated document model support for embedded attachments and outputs terse and consistent html trix is an open source project from basecamp the creators of ruby on rails millions of people trust their text to basecamp and we built trix to give them the best possible editing experience see trix in action in the all new basecamp 3 different by design most wysiwyg editors are wrappers around htmls contenteditable and execcommand apis designed by microsoft to support live editing of web pages in internet explorer 5 5 and eventually reverse engineered and copied by other browsers because these apis were never fully specified or documented and because wysiwyg html editors are enormous in scope each browsers implementation has its own set of bugs and quirks and javascript developers are left to resolve the inconsistencies trix sidesteps these inconsistencies by treating contenteditable as an i o device when input makes its way to the editor trix converts that input into an editing operation on its internal document model then re renders that document back into the editor this gives trix complete control over what happens after every keystroke and avoids the need to use execcommand at all built for the modern web trix supports all evergreen self updating desktop and mobile browsers trix is built with emerging web standards notably custom elements mutation observer and promises eventually we expect all browsers to implement these standards in the meantime trix includes polyfills for missing functionality getting started include the bundled trix css and trix js files in the head of your page html head … link rel stylesheet type text css href trix css script type text javascript src trix js script head trix css includes default styles for the trix toolbar editor and attachments skip this file if you prefer to define these styles yourself to use your own polyfills or to target only browsers that support all of the required standards include trix core js instead creating an editor place an empty trix editor trix editor tag on the page trix will automatically insert a separate trix toolbar before the editor like an html textarea trix editor accepts autofocus and placeholder attributes unlike a textarea trix editor automatically expands vertically to fit its contents integrating with forms to submit the contents of a trix editor with a form first define a hidden input field in the form and assign it an id then reference that id in the editors input attribute html form … input id x type hidden name content trix editor input x trix editor form trix will automatically update the value of the hidden input field with each change to the editor populating with stored content to populate a trix editor with stored content include that content in the associated input elements value attribute html form … input id x value editor content goes here type hidden name content trix editor input x trix editor form always use an associated input element to safely populate an editor trix wont load any html content inside a trix editor … trix editor tag styling formatted content to ensure what you see when you edit is what you see when you save use a css class name to scope styles for trix formatted content apply this class name to your trix editor element and to a containing element when you render stored trix content for display in your application html trix editor class trix content trix editor html div class trix content stored content here div the default trix css file includes styles for basic formatted content—including bulleted and numbered lists code blocks and block quotes—under the class name trix content we encourage you to use these styles as a starting point by copying them into your applications css with a different class name storing attached files trix automatically accepts files dragged or pasted into an editor and inserts them as attachments in the document each attachment is considered pending until you store it remotely and provide trix with a permanent url to store attachments listen for the trix attachment add event upload the attached files with xmlhttprequest yourself and set the attachments url attribute upon completion see the attachment example for detailed information if you dont want to accept dropped or pasted files call preventdefault on the trix file accept event which trix dispatches just before the trix attachment add event editing text programmatically you can manipulate a trix editor programmatically through the trix editor interface available on each trix editor element through its editor property js var element document queryselector trix editor element editor is a trix editor instance understanding the document model the formatted content of a trix editor is known as a document and is represented as an instance of the trix document class to get the editors current document use the editor getdocument method js element editor getdocument is a trix document instance you can convert a document to an unformatted javascript string with the document tostring method js var document element editor getdocument document tostring is a javascript string immutability and equality documents are immutable values each change you make in an editor replaces the previous document with a new document capturing a snapshot of the editors content is as simple as keeping a reference to its document since that document will never change over time this is how trix implements undo to compare two documents for equality use the document isequalto method js var document element editor getdocument document isequalto element editor getdocument true getting and setting the selection trix documents are structured as sequences of individually addressable characters the index of one character in a document is called a position and a start and end position together make up a range to get the editors current selection use the editor getselectedrange method which returns a two element array containing the start and end positions js element editor getselectedrange 0 0 you can set the editors current selection by passing a range array to the editor setselectedrange method js select the first character in the document element editor setselectedrange 0 1 collapsed selections when the start and end positions of a range are equal the range is said to be collapsed in the editor a collapsed selection appears as a blinking cursor rather than a highlighted span of text for convenience the following calls to setselectedrange are equivalent when working with collapsed selections js element editor setselectedrange 1 element editor setselectedrange 1 element editor setselectedrange 1 1 directional movement to programmatically move the cursor or selection through the document call the editor movecursorindirection or editor expandselectionindirection methods with a direction argument the direction can be either forward or backward js move the cursor backward one character element editor movecursorindirection backward expand the end of the selection forward by one character element editor expandselectionindirection forward converting positions to pixel offsets sometimes you need to know the x and y coordinates of a character at a given position in the editor for example you might want to absolutely position a pop up menu element below the editors cursor call the editor getclientrectatposition method with a position argument to get a domrect instance representing the left and top offsets width and height of the character at the given position js var rect element editor getclientrectatposition 0 rect left rect top 17 49 inserting and deleting text the editor interface provides methods for inserting replacing and deleting text at the current selection to insert or replace text begin by setting the selected range then call one of the insertion methods below trix will first remove any selected text then insert the new text at the start position of the selected range inserting plain text to insert unformatted text into the document call the editor insertstring method js insert “hello” at the beginning of the document element editor setselectedrange 0 0 element editor insertstring hello inserting html to insert html into the document call the editor inserthtml method trix will first convert the html into its internal document model during this conversion any formatting that cannot be represented in a trix document will be lost js insert a bold “hello” at the beginning of the document element editor setselectedrange 0 0 element editor inserthtml strong hello strong inserting a file to insert a dom file object into the document call the editor insertfile method trix will insert a pending attachment for the file as if you had dragged and dropped it onto the editor js insert the selected file from the first file input element var file document queryselector input type file file element editor insertfile file inserting a line break to insert a line break call the editor insertlinebreak method which is functionally equivalent to pressing the return key js insert “hello\n” element editor insertstring hello element editor insertlinebreak deleting text if the current selection is collapsed you can simulate deleting text before or after the cursor with the editor deleteindirection method js “backspace” the first character in the document element editor setselectedrange 1 1 element editor deleteindirection backward delete the second character in the document element editor setselectedrange 1 1 element editor deleteindirection forward to delete a range of text first set the selected range then call editor deleteindirection with either direction as the argument js delete the first five characters element editor setselectedrange 0 4 element editor deleteindirection forward working with attributes and nesting trix represents formatting as sets of attributes applied across ranges of a document by default trix supports the inline attributes bold italic href and strike and the block level attributes heading1 quote code bullet and number applying formatting to apply formatting to the current selection use the editor activateattribute method js element editor insertstring hello element editor setselectedrange 0 5 element editor activateattribute bold to set the href attribute pass a url as the second argument to editor activateattribute js element editor insertstring trix element editor setselectedrange 0 4 element editor activateattribute href https trix editor org removing formatting use the editor deactivateattribute method to remove formatting from a selection js element editor setselectedrange 2 4 element editor deactivateattribute bold formatting with a collapsed selection if you activate or deactivate attributes when the selection is collapsed your formatting changes will apply to the text inserted by any subsequent calls to editor insertstring js element editor activateattribute italic element editor insertstring this is italic adjusting the nesting level to adjust the nesting level of quotes bulleted lists or numbered lists call the editor increasenestinglevel and editor decreasenestinglevel methods js element editor activateattribute quote element editor increasenestinglevel element editor decreasenestinglevel using undo and redo trix editors support unlimited undo and redo successive typing and formatting changes are consolidated together at five second intervals all other input changes are recorded individually in undo history call the editor undo and editor redo methods to perform an undo or redo operation js element editor undo element editor redo changes you make through the editor interface will not automatically record undo entries you can save your own undo entries by calling the editor recordundoentry method with a description argument js element editor insertstring hello element editor recordundoentry insert text loading and saving editor state serialize an editors state with json stringify and restore saved state with the editor loadjson method the serialized state includes the document and current selection but does not include undo history js save editor state to local storage localstorage editorstate json stringify element editor restore editor state from local storage element editor loadjson json parse localstorage editorstate observing editor changes the trix editor element emits several events which you can use to observe and respond to changes in editor state trix initialize fires when the trix editor element is attached to the dom and its editor object is ready for use trix change fires whenever the editors contents have changed trix selection change fires any time the selected range changes in the editor trix focus and trix blur fire when the editor gains or loses focus respectively trix file accept fires when a file is dropped or inserted into the editor you can access the dom file object through the file property on the event call preventdefault on the event to prevent attaching the file to the document trix attachment add fires after an attachment is added to the document you can access the trix attachment object through the attachment property on the event if the attachment object has a file property you should store this file remotely and set the attachments url attribute see the attachment example for detailed information trix attachment remove fires when an attachment is removed from the document you can access the trix attachment object through the attachment property on the event you may wish to use this event to clean up remotely stored files contributing to trix trix is open source software freely distributable under the terms of an mit style license the source code is hosted on github we welcome contributions in the form of bug reports pull requests or thoughtful discussions in the github issue tracker please see the code of conduct for our pledge to contributors trix was created by javan makhmali and sam stephenson with development sponsored by basecamp building from source trix is written in coffeescript and compiled to javascript with blade from inside a checkout of the trix git repository issue the following commands to build the distributable files in dist bin setup bin blade build developing in browser you can spawn a development web server to work on trix in a more convenient fashion instead of manually rebuilding the source each time just reload a page in your browser to see your changes to develop in browser run bin setup and follow the displayed instructions running tests make sure youre set up to build from source using the instructions above then run bin blade runner and visit the displayed url to run the trix test suite pull requests only commit changes to trixs source everything except the compiled files in dist and leave the version unchanged we update both when publishing new releases heart © 2018 basecamp llc