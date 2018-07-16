gooey beta turn almost any python 2 or 3 console program into a gui application with one line gooey now supports python 3 table of contents gooey table of contents latest update quick start installation instructions usage examples what it is why is it who is this for how does it work internationalization global configuration layout customization run modes full advanced basic no config input validation using dynamic values customizing icons packaging screenshots contributing image credits quick start installation instructions the easiest way to install gooey is via pip pip install gooey alternatively you can install gooey by cloning the project to your local directory git clone https github com chriskiehl gooey git run setup py python setup py install note python 2 users must manually install wxpython unfortunately this cannot be done as part of the pip installation and should be manually downloaded from the wxpython website usage gooey is attached to your code via a simple decorator on whichever method has your argparse declarations usually main from gooey import gooey gooey all it takes def main parser argumentparser rest of code different styling and functionality can be configured by passing arguments into the decorator options gooey advanced boolean toggle whether to show advanced config or not language language string translations configurable via json show config true skip config screens all together target executable cmd explicitly set the subprocess executable arguments program name name defaults to script name program description defaults to argparse description default size 610 530 starting size of the gui required cols 1 number of columns in the required section optional cols 2 number of columbs in the optional section dump build config false dump the json gooey uses to configure itself load build config none loads a json gooey generated configuration monospace display false uses a mono spaced font in the output screen def main parser argumentparser rest of code see how does it work section for details on each option gooey will do its best to choose sensible widget defaults to display in the gui however if more fine tuning is desired you can use the drop in replacement gooeyparser in place of argumentparser this lets you control which widget displays in the gui see gooeyparser from gooey import gooey gooeyparser gooey def main parser gooeyparser description my cool gui program parser add argument filename widget filechooser parser add argument date widget datechooser examples gooey downloaded and installed great wanna see it in action head over the the examples repository to download a few ready to go example scripts theyll give you a quick tour of all gooeys various layouts widgets and features direct download what is it gooey converts your console applications into end user friendly gui applications it lets you focus on building robust configurable programs in a familiar way all without having to worry about how it will be presented to and interacted with by your average user why because as much as we love the command prompt the rest of the world looks at it like an ugly relic from the early 80s on top of that more often than not programs need to do more than just one thing and that means giving options which previously meant either building a gui or trying to explain how to supply arguments to a console application gooey was made to hopefully solve those problems it makes programs easy to use and pretty to look at who is this for if youre building utilities for yourself other programmers or something which produces a result that you want to capture and pipe over to another console application e g nix philosophy utils gooey probably isnt the tool for you however if youre building run and done around the office style scripts things that shovel bits from point a to point b or simply something thats targeted at a non programmer gooey is the perfect tool for the job it lets you build as complex of an application as your heart desires all while getting the gui side for free how does it work gooey is attached to your code via a simple decorator on whichever method has your argparse declarations gooey def my run func parser argumentparser rest of code at run time it parses your python script for all references to argumentparser the older optparse is currently not supported these references are then extracted assigned a component type based on the action they provide and finally used to assemble the gui mappings gooey does its best to choose sensible defaults based on the options it finds currently argumentparser actions are mapped to the following wx components parser action widget example store textctrl store const checkbox store true checkbox store false checkbox append textctrl count dropdown mutually exclusive group radiogroup choice dropdown gooeyparser if the above defaults arent cutting it you can control the exact widget type by using the drop in argumentparser replacement gooeyparser this gives you the additional keyword argument widget to which you can supply the name of the component you want to display best part you dont have to change any of your argparse code to use it drop it in and youre good to go example from argparse import argumentparser def main parser argumentparser description my cool gooey app parser add argument filename help name of the file to process given then above gooey would select a normal textfield as the widget type like this however by dropping in gooeyparser and supplying a widget name you can display a much more user friendly filechooser from gooey import gooeyparser def main parser gooeyparser description my cool gooey app parser add argument filename help name of the file to process widget filechooser custom widgets widget example dirchooser filechooser multifilechooser datechooser passwordfield listbox internationalization gooey is international ready and easily ported to your host language languages are controlled via an argument to the gooey decorator gooey language russian def main all program text is stored externally in json files so adding new langauge support is as easy as pasting a few key value pairs in the gooey languages directory thanks to some awesome contributers gooey currently comes pre stocked with the following language sets english dutch french portuguese want to add another one submit a pull request global configuration just about everything in gooeys overall look and feel can be customized by passing arguments to the decorator parameter summary encoding text encoding to use when displaying characters default utf 8 use legacy titles rewrites the default argparse group name from positional to required this is primarily for retaining backward compatibilty with previous versions of gooey which had poor support awareness of groups and did its own naive bucketing of arguments advanced toggles whether to show the full configuration screen or a simplified version auto start skips the configuration all together and runs the program immediately language tells gooey which language set to load from the gooey languages directory target tells gooey how to re invoke itself by default gooey will find python but this allows you to specify the program and arguments if supplied program name the name displayed in the title bar of the gui window if not supplied the title defaults to the script name pulled from sys argv 0 program description sets the text displayed in the top panel of the settings screen defaults to the description pulled from argumentparser default size initial size of the window required cols controls how many columns are in the required arguments section warning deprecation notice see group parameters for modern layout controls optional cols controls how many columns are in the optional arguments section warning deprecation notice see group parameters for modern layout controls dump build config saves a json copy of its build configuration on disk for reuse editing load build config loads a json copy of its build configuration from disk monospace display uses a mono spaced font in the output screen warning deprecation notice see group parameters for modern font configuration image dir path to the directory in which gooey should look for custom images icons language dir path to the directory in which gooey should look for custom languages files disable stop button disable the stop button when running show stop warning displays a warning modal before allowing the user to force termination of your program force stop is error toggles whether an early termination by the shows the success or error screen show success modal toggles whether or not to show a summary modal after a successful run run validators controls whether or not to have gooey perform validation before calling your program poll external updates experimental when true gooey will call your code with a gooey seed ui cli argument and use the response to fill out dynamic values in the ui see using dynamic values return to config when true gooey will return to the configuration settings window upon successful run progress regex a text regex used to pattern match runtime progress information see showing progress for a detailed how to progress expr a python expression applied to any matches found via the progress regex see showing progress for a detailed how to disable progress bar animation disable the progress bar navigation sets the navigation style of gooeys top level window options tabbedsidebar navigation title controls the heading title above the sidebars navigation pane defaults to actions show sidebar show hide the sidebar in when navigation mode sidebar body bg color hex value of the main gooey window header bg color hex value of the header background header height height in pixels of the header header show title show hide the header title header show subtitle show hide the header subtitle footer bg color hex value of the footer background sidebar bg color hex value of the sidebars background terminal panel color hex value of the terminals panel terminal font color hex value of the font displayed in gooeys terminal terminal font family name of the font family to use in the terminal terminal font weight weight of the font normal bold terminal font size point size of the font displayed in the terminal error color hex value of the text displayed when a validation error occurs layout customization you can achieve fairly flexible layouts with gooey by using a few simple customizations at the highest level you have several overall layout options controllable via various arguments to the gooey decorator show sidebar true show sidebar false navigation tabbed tabbed groups true grouping inputs by default if youre using argparse with gooey your inputs will be split into two buckets positional and optional however these arent always the most descriptive groups to present to your user you can arbitrarily bucket inputs into logic groups and customize the layout of each with argparse this is done via add argument group parser argumentparser search group parser add argument group search options customize the search options you can add arguments to the group as normal search group add argument query help base search string which will display them as part of the group within the ui customizing group layout note make sure youre using gooeyparser if you want to take advantage of the layout customizations with a group created we can now start tweaking how it looks gooeyparser extends the api of add argument group to accept an additional keyword argument gooey options it accepts two keys show border and columns gooey options show border bool columns 1 100 show border is nice for visually tying together closely related items within a parent group setting it to true will draw a small border around all of the inputs and nest the title at the top columns controls how many many items get places on each row within the run modes gooey has a handful of presentation modes so you can tailor its layout to your content type and users level or experience advanced the default view is the full or advanced configuration screen it has two different layouts depending on the type of command line interface its wrapping for most applications the flat layout will be the one to go with as its layout matches best to the familiar cli schema of a primary command followed by many options e g curl ffmpeg on the other side is the column layout this one is best suited for clis that have multiple paths or are made up of multiple little tools each with their own arguments and options think git it displays the primary paths along the left column and their corresponding arguments in the right this is a great way to package a lot of varied functionality into a single app both views present each action in the argument parser as a unique gui component it makes it ideal for presenting the program to users which are unfamiliar with command line options and or console programs in general help messages are displayed along side each component to make it as clear as possible which each widget does setting the layout style currently the layouts cant be explicitely specified via a parameter on the todo the layouts are built depending on whether or not there are subparsers used in your code base so if you want to trigger the column layout youll need to add a subparser to your argparse code it can be toggled via the advanced parameter in the gooey decorator gooey advanced true def main rest of code basic the basic view is best for times when the user is familiar with console applications but you still want to present something a little more polished than a simple terminal the basic display is accessed by setting the advanced parameter in the gooey decorator to false gooey advanced false def main rest of code no config no config pretty much does what youd expect it doesnt show a configuration screen it hops right to the display section and begins execution of the host program this is the one for improving the appearance of little one off scripts input validation warning note this functionality is experimental its api may be changed or removed alltogether feedback thoughts on this feature is welcome and encouraged gooey can optionally do some basic pre flight validation on user input internally it uses these validator functions to check for the presence of required arguments however by using gooeyparser you can extend these functions with your own validation rules this allows gooey to show much much more user friendly feedback before it hands control off to your program writing a validator validators are specified as part of the gooey options map available to gooeyparser its a simple map structure made up of a root key named validator and two internal pairs test the inner body of the validation test you wish to perform message the error message that should display given a validation failure e g gooey options validator test len user input 3 message some helpful message the test function your test function can be made up of any valid python expression it receives the variable user input as an argument against which to perform its validation note that all values coming from gooey are in the form of a string so youll have to cast as needed in order to perform your validation full code example from gooey python bindings gooey decorator import gooey from gooey python bindings gooey parser import gooeyparser gooey def main parser gooeyparser description example validator parser add argument secret metavar super secret number help a number specifically between 2 and 14 gooey options validator test 2 int user input 14 message must be between 2 and 14 args parser parse args print cool your secret number is args secret with the validator in place gooey can present the error messages next to the relevant input field if any validators fail using dynamic values warning note this functionality is experimental its api may be changed or removed alltogether feedback on this feature is welcome and encouraged gooeys choice style fields dropdown listbox can be fed a dynamic set of values at runtime by enabling the poll external updates option this will cause gooey to request updated values from your program everytime the user visits the configuration page this can be used to for instance show the result of a previous execution on the config screen without requiring that the user restart the program how does it work at runtime whenever the user hits the configuration screen gooey will call your program with a single cli argument gooey seed ui this is a request to your program for updated values for the ui in response to this on stdout your program should return a json string mapping cli inputs to a list of options for example assuming a setup where you have a dropdown that lists user files parser add argument load metavar load previous save help load a previous save file dest filename widget dropdown choices list savefiles here the input we want to populate is load so in response to the gooey seed ui request you would return a json string with load as the key and a list of strings that youd like to display to the user as the value e g load filename 1 txt filename 2 txt filename n txt checkout the full example code in the examples repository or checkout a larger example in the silly little tool that spawned this feature savingoverit customizing icons gooey comes with a set of six default icons these can be overridden with your own custom images icons by telling gooey to search additional directories when initializing this is done via the image dir argument to the goeey decorator gooey program name custom icon demo image dir path to my image directory def main rest of program images are discovered by gooey based on their filenames so for example in order to supply a custom configuration icon simply place an image with the filename config icon png in your images directory these are the filenames which can be overridden program icon ico success icon png running icon png loading icon gif config icon png error icon png packaging thanks to some awesome contributers packaging gooey as an executable is super easy the tl dr pyinstaller version is to drop this build spec into the root directory of your application edit its contents so that the application and name are relevant to your project then execute pyinstaller build spec to bundle your app into a ready to go executable detailed step by step instructions can be found here screenshots flat layout column layout success screen error screen warning dialog custom groups tabbed groups tabbed navigation sidebar navigation input validation wanna help code translation graphics pull requests are welcome