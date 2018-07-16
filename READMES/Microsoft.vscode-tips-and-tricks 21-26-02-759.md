vs code tips and tricks note tips and tricks has moved to the official visual studio code documentation at code visualstudio com the content is now at vscode docs pull requests and documentation issues are still greatly appreciated table of contents basics customization extensions file and folder management editing hacks intellisense snippets git integration debugging task runner other resources the key bindings below may or may not be accurate with the latest build see here for the latest keyboard shortcut reference basics insider version of vs code the visual studio code team uses the insiders version to test the latest features and bug fixes of vs code you can use this same version by downloading here for early adopters insiders has the most recent code changes and may lead to the occasional broken build frequent builds new builds everyday with the latest bug fixes and features side by side install insiders installs next to the stable build allowing you to use either independently getting started open the welcome page to get started with the basics of vs code help welcome includes the interactive playground command palette access all available commands based on your current context mac cmd shift p or f1 windows linux ctrl shift p or f1 reference keybindings all of the commands are in the command palette with the associated key binding if it exists if you forget what the key binding is use the command palette to help you out quick open quickly open files mac cmd p windows linux ctrl p tip type to view help suggestions navigate between recently opened files repeat the quick open keyboard shortcut to cycle quickly between recently opened files open multiple files from quick open you can open multiple files from quick open by pressing the right arrow key this will open the currently selected file in the background and you can continue selecting files from quick open cli tool linux follow instructions here windows follow instructions here mac see below open the command palette f1 and type shell command hit enter to execute shell command install code command in path bash open code with current directory code open the current directory in the most recently used code window code r create a new window code n change the language code locale es open diff editor code diff see help options code help disable all extensions code disable extensions vscode folder workspace specific files are in vscode for example tasks json for the task runner and launch json for the debugger status bar decorations errors and warnings mac shift cmd m windows linux ctrl shift m quickly jump to errors and warnings in the project cycle through errors with f8 or shift f8 you can filter problems by type errors warnings or text matching change language mode mac cmd k m windows linux ctrl k m if you want to persist the new language mode for that file type you can use the configure file association for command to associate the current file extension with an installed language customization there are many things you can do to customize vs code change your theme change your keyboard shortcuts tune your settings add json validation create snippets install extensions check out the full documentation change your theme open the command palette and type themes you can install more themes from the extension marketplace additionally you can install and change your file icon themes change your keyboard shortcuts keyboard reference sheets download the keyboard shortcut reference sheet for your platform macos windows linux keymaps are you used to keyboard shortcuts from another editor you can install a keymap extension that brings the keyboard shortcuts from your favorite editor to vs code go to preferences keymap extensions to see the current list on the marketplace some of the more popular ones vim sublime text keymap emacs keymap atom keymap customize your keyboard shortcuts open the command palette and type keyboard shortcuts you can now add your own keybindings in the file on the right see more in key bindings for visual studio code tune your settings open settings json mac cmd windows linux file preferences settings format on paste json editor formatonpaste true change the font size json editor fontsize 18 change the zoom level json window zoomlevel 5 font ligatures json editor fontfamily fira code editor fontligatures true tip you will need to have a font installed that supports font ligatures firacode is a popular font on the vs code team auto save json files autosave afterdelay you can also toggle auto save from the top level menu with the file auto save format on save json editor formatonsave true change the size of tab characters json editor tabsize 4 spaces or tabs json editor insertspaces true render whitespace json editor renderwhitespace all ignore files folders removes these files folders from your editor window json files exclude somefolder true somefile true remove these files folders from search results json search exclude somefolder true somefile true and many many others language specific settings for those settings you only want for specific languages json languageid tip you can find the language id by typing in the command palette configure language specific settings add json validation enabled by default for many files create your own schema and validation in settings json json json schemas filematch bower json url http json schemastore org bower or for a schema defined in your workspace json json schemas filematch foo json url myschema json or a custom schema json json schemas filematch myconfig schema type object properties name type string description the name of the entry see more in the documentation extensions find extensions in the vs code marketplace search inside vs code view extension recommendations community curated extension lists such as awesome vscode install extensions click the extensions activity bar button you can search via the search bar or click the more button to filter and sort by install count extension recommendations click the extensions activity bar button then click show recommended extensions in the more button menu creating my own extension are you interested in creating your own extension you can learn how to do this in the documentation specifically check out the documentation on contribution points configuration commands keybindings languages debuggers grammars themes snippets jsonvalidation file and folder management integrated terminal windows linux mac ctrl further reading official documentation mastering vs codes terminal article auto save open settings json with cmd json files autosave afterdelay you can also toggle auto save from the top level menu with the file auto save toggle sidebar mac cmd b windows linux ctrl b zen mode mac cmd k z windows linux ctrl k z enter distraction free zen mode side by side editing mac cmd \ or cmd then click a file from the file explorer windows linux ctrl \ linux ctrl 2 you can use drag and drop editors to create new editor groups and move editors between groups switch between editors mac cmd 1 cmd 2 cmd 3 windows linux ctrl 1 ctrl 2 ctrl 3 move to explorer window mac cmd shift e windows linux ctrl shift e create and open a file mac cmd click windows linux ctrl click close the currently opened folder mac cmd w windows linux ctrl k f history navigate entire history with ctrl tab navigate back mac ctrl windows linux alt left navigate forward mac ctrl shift windows linux alt right navigate to a file mac cmd e or cmd p windows linux ctrl e or ctrl p file associations create language associations for files that arent detected accurately for example many config files are json json file associations database json editing hacks here are a selection of common features for editing code if the keyboard shortcuts arent comfortable for you consider installing a keymap extension for your old editor multi cursor selection mac opt cmd up or opt cmd down windows ctrl alt up or ctrl alt down linux alt shift up or alt shift down add more cursors to current selection join line mac ctrl j windows linux not bound by default open keyboard shortcuts and bind editor action joinlines to a shortcut of your choice copy line up down mac opt shift up or opt shift down windows linux issue 5363 shift alt down or shift alt up shrink expand selection more in documentation mac ctrl shift cmd left or ctrl shift cmd right windows linux shift alt left or shift alt right go to symbol in file mac cmd shift o windows linux ctrl shift o you can group the symbols by kind by adding a colon go to symbol in workspace mac cmd t windows linux ctrl t navigate to a specific line mac ctrl g or cmd p windows linux ctrl g undo cursor position mac cmd u windows linux ctrl u move line up and down mac opt up or opt down windows linux alt up or alt down trim trailing whitespace mac cmd k cmd x windows linux ctrl k ctrl x code formatting currently selected source code mac cmd k cmd f windows linux ctrl k ctrl f whole document format windows linux shift alt f code folding mac alt cmd and alt cmd windows linux ctrl shift and ctrl shift select current line mac cmd i windows linux ctrl i navigate to beginning and end of file mac cmd up and cmd down windows ctrl up and ctrl down linux ctrl home and ctrl end open markdown preview in a markdown file use mac shift cmd v windows linux ctrl shift v side by side markdown edit and preview in a markdown file use mac cmd k v windows linux ctrl k v special bonus the preview will now sync intellisense anytime try ctrl space to trigger the suggestions widget you can view available methods parameter hints short documentation etc peek select a symbol then type alt f12 alternatively you can use the context menu go to definition select a symbol then type f12 alternatively you can use the context menu or ctrl click cmd click on macos you can go back to your previous location with the go back command or alt left ctrl on macos find all references select a symbol then type shift f12 alternatively you can use the context menu rename symbol select a symbol then type f2 alternatively you can use the context menu eslintrc json install the eslint extension configure your linter however youd like specification is here here is configuration to use es6 json env browser true commonjs true es6 true node true parseroptions ecmaversion 6 sourcetype module ecmafeatures jsx true classes true defaultparams true rules no const assign 1 no extra semi 0 semi 0 no fallthrough 0 no empty 0 no mixed spaces and tabs 0 no redeclare 0 no this before super 1 no undef 1 no unreachable 1 no use before define 0 constructor super 1 curly 0 eqeqeq 0 func names 0 valid typeof 1 package json see intellisense for your package json file emmet syntax support for emmet syntax snippets create custom snippets file preferences user snippets select the language and create a snippet json create component prefix component body class 1 extends react component render return 2 see more details in creating your own snippets git integration git integration comes with vs code in the box you can install other scm provider from the extension marketplace this section describes the git integration but much of the ui and gestures are shared by other scm providers diffs click the source control button in the activity bar then select the file to diff side by side default is side by side diff inline view toggle inline view by clicking the more button in the top right and selecting switch to inline view if you prefer the inline view you can set diffeditor rendersidebyside false review pane navigate through diffs with f7 and shift f7 this will present them in a unified patch format lines can be navigated with arrow keys and pressing enter will jump back in the diff editor and the selected line edit pending changes you can make edits directly in the pending changes of the diff view branches easily switch between git branches via the status bar staging stage all hover over the number of files and click the plus button stage selected stage a portion of a file by selecting that file using the arrows and then choosing stage selected ranges from the command palette undo last commit see git output vs code makes it easy to see what git commands are actually running this is helpful when learning git or debugging a difficult source control issue mac shift cmd u windows linux ctrl shift u to run toggleoutput select git in the drop down gutter indicators view diff decorations in editor see documentation for more details resolve merge conflicts during a merge click the source control button in the activity bar and make changes in the diff view select and accept current incoming or both changes in just one click setup vs code as default merge tool bash git config global merge tool code debugging configure debugger f1 and select debug open launch json select the environment this will generate a launch json file works out of the box as expected for node js and other environments may need some additional configuration for other languages see documentation for more details breakpoints and stepping through place breakpoints next to the line number navigate forward with the debug widget data inspection inspect variables in the debug panels and in the console inline values you can set debug inlinevalues true to see variable values inline in the debugger this feature is experimental and disabled by default task runner auto detect tasks select tasks from the top level menu run the command configure tasks then select the type of task youd like to run this will generate a task json file with content like the following see the tasks documentation for more details json see http go microsoft com fwlink linkid 733558 for the documentation about the tasks json format version 0 1 0 command npm isshellcommand true showoutput always suppresstaskname true tasks taskname install args install taskname build args run build there are occasionally issues with auto generation check out the documentation for getting things to work properly run tasks from the tasks menu select tasks from the top level menu run the command run task and select the task you want to run terminate the running task by running the command terminate task other resources vscode official docs react sample app awesome vscode