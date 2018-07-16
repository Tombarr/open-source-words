# My wonderful world of macOS [![Thanks](https://img.shields.io/badge/Say%20Thanks-💗-ff69b4.svg)](https://www.patreon.com/nikitavoloboev)
> List of applications and tools that make my macOS experience even more amazing

![](https://raw.githubusercontent.com/nikitavoloboev/my-mac-os/master/mac.png)

> [Wallpaper link](https://ello.co/maalavidaa/post/0avsbcnwu5jet6j-uckz2g)

##### Contents
- [Applications](#applications)
	- [Productivity](#productivity)
	- [Code](#code)
	- [Social](#social)
	- [Writing](#writing)
	- [Design](#design)
	- [Music](#music)
	- [Images](#images)
	- [Video](#video)
	- [Finance](#finance)
	- [Utilities](#utilities)
	- [Browsers](#browsers)
- [Command Line Apps](#command-line-apps)
- [Preference Panes](#preference-panes)
- [My wonderful world of iOS](#my-wonderful-world-of-ios-)
- [Similar Setups](#similar-setups)
- [Related](#related)
- [Contributing](#contributing)

## Applications
I use a lot of applications on my mac. Below is a list of the ones that I love and use the most in my day to day life.

I also share [my dotfiles](https://github.com/nikitavoloboev/dotfiles) together with my [iOS setup](https://github.com/nikitavoloboev/my-ios#readme). And I made a [Telegram group](https://t.me/macOSautomation) to discuss all things macOS/iOS.

### Productivity
#### [Alfred](https://www.alfredapp.com) - Launcher
- Alfred is a very powerful launcher that you can program to show anything you want. It saved me a lot of time in my life.
<img src="https://i.imgur.com/5Cs4oly.png" width="600" alt="img">

- It has a great [community](http://www.alfredforum.com/) and [amazing workflows](https://github.com/learn-anything/alfred-workflows#readme) that you can use.

- I wrote [an article](https://medium.com/@NikitaVoloboev/writing-alfred-workflows-in-go-2a44f62dc432) on how anyone can start developing workflows of their own using Go language and [AwGo](https://github.com/deanishe/awgo) library.

#### [Karabiner](https://pqrs.org/osx/karabiner/) - Keyboard remapping
- Karabiner is an absolutely amazing app that lets you remap keys at a very low level on macOS.
- I have completely remapped my keyboard with it and every key on my keyboard is a custom modifier key that I can program to do what I want.
- For example you can make caps lock into an escape key when pressed once but if you hold it, it becomes a [hyper key](http://brettterpstra.com/2017/06/15/a-hyper-key-with-karabiner-elements-full-instructions/). Hyper key means that a key now serves two purposes, once when pressed alone and once when held down. So for example, for remapping caps lock, we can remap it to act as escape when pressed alone once but if we hold down on it, it becomes `⌘ + ⌃` modifier key. So `Caps Lock + F` becomes `⌘ + ⌃ + F`. And so on.
- I take this idea further and define these kind of hyper keys for __every single key on my keyboard__.
- I describe how I use Karabiner in detail [here](https://wiki.nikitavoloboev.xyz/macOS/apps/karabiner/karabiner.html).

#### [Keyboard Maestro](https://www.keyboardmaestro.com/main/) - Automation tool
- Keyboard Maestro is essentially an IDE for automation. You create macros of actions that you can then easily call from Karabiner.
- It has a [wonderful community](https://forum.keyboardmaestro.com/) that is happy to help with whatever you are trying to achieve.
- I share [all the macros I use](https://wiki.nikitavoloboev.xyz/macOS/apps/keyboard-maestro/km-macros.html) with the app.

#### [2Do](http://www.2doapp.com/mac) - Flexible task manager
- I love GTD methodology. This app is phenomenal with helping me [organize my tasks](https://wiki.nikitavoloboev.xyz/macOS/apps/2do.html). Here is how my sidebar looks:
<img src="https://i.imgur.com/URuzerx.png" width="150">

- It also has global quick add with a hotkey. Together with lists, priorities, powerful search and a lot more.
<img src="https://i.imgur.com/UPdjh6N.png" width="400" alt="img">

#### [Trello](https://trello.com) - Project management tool
- I use the app a lot to track various projects I have in my life.
- I share many boards I made [publicly](https://wiki.nikitavoloboev.xyz/sharing/my-trello.html). Here is an example of a public board for tracking various [things I want to learn](https://trello.com/b/cu32qF3q).
![](https://i.imgur.com/cZzCfJ3.jpg)

- I nearly always use two labels: __Important__ and __Next__. And I mark the cards I am working on and set deadlines on most cards.

#### [1Password](https://1password.com) - Password manager
- Generate all of my passwords with it and keep everything in a secured and encrypted vault kept secure by my one master password.
- No longer need to remember passwords and I now have a unique password for every website that I am signed up on whilst [activating two factor authentication](https://support.1password.com/one-time-passwords/) wherever possible.

#### [Timing](https://timingapp.com/whats-new) - Automatic time tracker
- I use Timing app to fully automate tracking my time on my computer.
- The fact that I can combine active and passive tracking together is very powerful and allows me to be more aware of where I spend my time.
<img src="https://i.imgur.com/lgQuK47.png" width="600" alt="img">

#### [MindNode](https://mindnode.com) - Interactive Mind Mapping
- An application which allowed me to originally create all of the maps for [Learn Anything](https://learn-anything.xyz).
<img src="https://raw.githubusercontent.com/learn-anything/learn-anything/master/media/header.png" width="700" alt="img">

- I have a __Think__ map that I open with Karabiner by pressing `f + :`. And I [brainstorm things](../../research/solving-problems.md) I am doing __now__ there.
- I also use MindNode to visualize topics and their relations as an [interactive mind map](https://my.mindnode.com/uQPgJs5DnVaAqyR9yrqxySQB6sCDRy2bmb7yxqKg#1653.2,-925.0,2).

![](https://i.imgur.com/mQWt0vx.jpg)

#### [Typinator](http://www.ergonis.com/products/typinator/) - Text expansions
- I use the app to [fully automate writing repetitive text](https://medium.com/@NikitaVoloboev/write-once-never-write-again-c2fa1f6c4e8).
- I share all the Typinator sets I made with the app [here](typinator).

#### [BetterTouchTool](https://www.boastr.net/) - Mac input customizer
- I use this app a lot for mapping [various trackpad gestures](https://medium.com/@NikitaVoloboev/take-control-of-your-touchpad-on-macos-45c581f542e0#.7n1ye6vze) to hotkeys and actions both globally and per specific applications.
<img src="https://i.imgur.com/BXdQ1LZ.png" width="500" alt="img">

- I love scrolling through my tabs in Safari with three finger swipes left and right as well as opening and closing tabs with swiping up and down respectively.
- I share [all the different gestures I have setup to use with the app](btt#readme) that you can view and download.

#### [PDF Expert](https://pdfexpert.com/) - PDF reader/editor
- I read a lot of PDFs like books, research papers and the like. This app is a huge upgrade over Preview app that I used before.
- Multiple tabs, sepia mode, very nice annotation tools, great search, performance.

#### [Fantastical](https://flexibits.com/fantastical) - Calendar
- I use the app to manage events in my life.
- I take great use of Fantastical's natural language input and I use [many Typinator expansions](https://medium.com/@NikitaVoloboev/fantastical-natural-input-text-expansions-3ea8cf7ccac3#.pv5937ncr) to ease this process.
- I always view my events from `Week` view. And show 5 days only with all 24h shown for all days. This lets me have a perspective over what I have to do now. What deadlines I have to complete soon. And gives me the freedom to adjust my schedule in light of upcoming deadlines and events.

#### [Contexts](https://contexts.co) - Window switcher
- Allows me to fuzzy search through all the currently active windows that I have.
<img src="https://i.imgur.com/q6nfG2P.png" width="500" alt="img">

- Makes jumping to the right window I need effortless. I often may have many VS Code instances with different projects running and this lets me switch to the project I need in seconds.

#### [Dictionary](http://www.wikiwand.com/en/Dictionary_(software))
- Comes natively with macOS and I started to love using it for exploring and searching through Wikipedia.
- It is incredibly fast to make the searches and it gives quick autosuggestions for any query I type that I can then select with up and down arrows.
<img src="https://i.imgur.com/Brw1wLV.png" width="500" alt="img">

#### [Bartender](https://www.macbartender.com/) - Menu bar organizer
- A great utility app that allows you to customize and hide the contents of your menu bar and improve the aesthetics of your OS. It is also is quite beneficial for me as I customized it to have the most important information that I need to show in it.
<img src="https://i.imgur.com/vcwCL1s.png" width="500" alt="img">

- I can also activate Bartender and start searching for the menu bar item I need all from the keyboard.

#### [Focus](https://heyfocus.com) - Block distracting websites
- I have front pages of [Hckrnews](http://hckrnews.com), [Reddit](https://www.reddit.com), [Twitter](https://twitter.com) and many more time sinking websites on the black list.
<img src="https://i.imgur.com/B9Tsaxf.png" width="500" alt="img">

- I then have a schedule where I can only use these websites for 20 minutes every 2 hours. It also turns on Do Not Disturb mode whilst I am in Focus mode.
<img src="https://i.imgur.com/rZkauBr.png" width="500" alt="img">

- If I go to any of my blocked websites during my `Focus` time, I am greeted with this message.
<img src="https://i.imgur.com/MMSn0zl.png" width="500" alt="img">

#### [Annotate](https://itunes.apple.com/us/app/annotate-capture-screenshot/id918207447?mt=12) - Create and annotate screenshots
- Best annotation tool I found to exist. After you make a screenshot, it allows for quick edits. Adding arrows, some text, blurring parts of the image as well as ability to quickly save the image or drag it to Dropzone to upload to Imgur to share the link quickly with anyone I want.

#### [Popclip](https://pilotmoon.com/popclip/) - iOS like mouse text selection popover
- Another great utility I cannot live without, brings up a quick menu whenever some text is selected on which I can do a number of quick actions, like searching on Google, DuckDuckGo, YouTube, Dictionary, Reddit, Google Images or it can translate text selected, copy it or even make a SnippetsLab snippet from it. Here is how it looks for me:
<img src="https://i.imgur.com/VLFRDAC.png" width="400" alt="img">

#### [Noizio](http://noiz.io/) - Ambient sounds
- I never listen to music when I want to focus on something as it is distracting. Instead I listen to sounds of rain, train or fire.

#### [Hammerspoon](http://www.hammerspoon.org) - Automation tool
- Powerful automation engine, wanted to use it for window management at first but found BetterTouchTool to be more performant.
- Right now I use it show the task I am currently working on in a little window in the middle of the screen for a brief moment:
<img src="https://i.imgur.com/E7RsarV.png" width="300" alt="img">

- My config for it can be seen [here](https://github.com/nikitavoloboev/dotfiles/blob/master/hammerspoon/).

#### [Reeder](http://reederapp.com/mac/) - RSS Reeder
- The app I use to keep up with my RSS feeds. I use RSS to follow my favorite blogs, stay up to date on new podcast episodes and even track some software releases.
- I use [Inoreader](https://www.inoreader.com) to sync [blogs I follow](https://wiki.nikitavoloboev.xyz/research/blogs.html) between phone and mac.
- Here is how Reeder looks like for me:
<img src="https://i.imgur.com/WCGFLl8.png" width="500" alt="img">

#### [Dropzone](https://aptonic.com) - Drag and drop actions
- A quick utility that pops up when I drag some file into it or open it with a hotkey, use it to upload images to [Imgur](http://imgur.com), dropping files into a preset number of folders that I made quickly as well as going to them in an instant.
<img src="https://i.imgur.com/UTqei1d.png" width="300" alt="img">

#### [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html) - Control incoming/outgoing network traffic
- Amazing networking tool that gives you a clear picture of what connections are incoming to your computer and what are outgoing.
- Takes a bit of time to set it up correctly and is quite an insightful experience first turning it on and having it notify every couple of seconds that some app is trying to send data to some server and whether you want to allow that.
- This is essential if you want to take control of what information gets sent out from your computer and what connections have right to connect to your data.

#### [BeardedSpice](https://github.com/beardedspice/beardedspice) - Extend Mac Media Keys
- Enhance play/pause as well as previous/next playback keys to not only work in iTunes and Spotify but work for SoundCloud, YouTube and many other services.

#### [Transmission](https://www.transmissionbt.com/) - BitTorrent client
- A torrent client that I use. Very minimal in its UI but very powerful and has all the features that I need.

#### [Transmit](https://www.panic.com/transmit/) - Transfer files
- I often use this app to quickly send files from my local file system to the cloud and get a shareable link I can send to people.
- I use [this Alfred workflow](https://github.com/bigluck/alfred2-transmit) to quickly open the cloud storage I need.
<img src="http://i.imgur.com/RkkcdvA.png" width="400" alt="img">

#### [Anki](http://ankisrs.net) - Intelligent flash cards
- [Spaced repetition learning](http://www.wikiwand.com/en/Spaced_repetition) is quite powerful. Essentially all this software does is provide you the means to write your own digital flashcards that you can then test yourself on. It also has a lot of [amazing addons](https://ankiweb.net/shared/addons/) that you can get to add more functionality to the app.

#### [TotalSpaces2](https://totalspaces.binaryage.com/) - Grid space manager
- Allows me to completely remove the animation of switching between spaces/full screen apps.
- I now run most applications in full screen and switch between them with [Karabiner](https://wiki.nikitavoloboev.xyz/macOS/apps/karabiner/karabiner.html).

#### [Paprika Recipe Manager](https://itunes.apple.com/us/app/paprika-recipe-manager-3/id1303222628?ls=1&mt=12)
- Use the app to fully plan any meal or recipe I want to make throughout the day as well as [collect recipes](https://github.com/nikitavoloboev/recipes#readme) and manage my shopping list.

### Code
#### [VS Code](https://github.com/Microsoft/vscode) - Code editor
- My favorite editor that I use to write code in. I use [many extensions](https://wiki.nikitavoloboev.xyz/text-editors/vs-code/vs-code-extensions.html) for it.
- My config for it can be found [here](https://github.com/nikitavoloboev/dotfiles/blob/master/vscode/settings.json).
- I use [Monokai Octagon](https://www.monokai.pro/vscode/) theme with [Fira Code](https://github.com/tonsky/FiraCode) font. Here is how it looks:

![](https://i.imgur.com/hss9CH8.png)

#### [iTerm](https://www.iterm2.com/) - Terminal Emulator
- Use Zsh as my shell together with [Antibody](https://github.com/getantibody/antibody) plugin manager and [Pure](https://github.com/sindresorhus/pure) theme.
- Assigned w + j with [Karabiner](https://wiki.nikitavoloboev.xyz/macOS/apps/karabiner/karabiner.html) to open the app from Keyboard Maestro in seconds.
- I made my own [Monokai theme](iterm#readme) for it. Which goes well with [Ayu theme for Vim](https://github.com/ayu-theme/ayu-vim).

<img src="https://i.imgur.com/WQNfyfO.png" width="500" alt="img">

- I also love using [this workflow](https://github.com/isometry/alfred-tty) to quickly switch between active tty sessions.
<img src="https://i.imgur.com/UUDBHcq.png" width="500" alt="img">

- I go over how I use the app [here](https://wiki.nikitavoloboev.xyz/macOS/apps/iterm.html).

#### [Sublime Text](https://www.sublimetext.com) - Text Editor
- Use this editor in addition to VS Code and Neovim for its blazing fast speed of opening files.
- I use it primarily to edit markdown files like [my wiki](https://wiki.nikitavoloboev.xyz/other/wiki-workflow.html). I also edit config files and open large and small files for quick edits.
- I use [many plugins](https://wiki.nikitavoloboev.xyz/text-editors/sublime-text/sublime-text-plugins.html) together with [Ayu theme](https://github.com/dempfi/ayu).

#### [Dash](https://kapeli.com/dash) - API Documentation Browser
- Allows you to download any docset that you might want to use, search for any method, class or anything that you need very quickly, comes with the amazing [Alfred worfklow](https://www.alfredapp.com/blog/productivity/dash-quicker-api-documentation-search/) to simplify the process of searching for the right things.
<img src="http://i.imgur.com/tBEkKtL.png" width="500" alt="img">

- I also use [this workflow](https://github.com/nikitavoloboev/small-workflows/tree/master/dash-profile-switch#readme) I made to quickly switch between Dash profiles.

<img src="https://i.imgur.com/wyqtfCM.png" width="500" alt="img">

#### [SnippetsLab](https://www.renfei.org/snippets-lab/) - Snippet manager
- I use the app to manage my own personal library of snippets. I prefix all snippets I make. For example vim snippets are prefixed with `vim:`. Git related snippets with `git:` and so on.
- This lets me then use the [Alfred workflow](https://www.renfei.org/snippets-lab/press-release/whats-new/osx-1.6.html) that the app's author provides to search for these snippets insanely fast.
<img src="https://i.imgur.com/gzoH1Dh.png" width="500" alt="img">

Here is how my library looks:
![](https://i.imgur.com/LBQVFPo.png)

- I share my entire library of snippets as [GitHub Gists](https://wiki.nikitavoloboev.xyz/sharing/my-gists.html). And I share my local library too that you can download [here](https://wiki.nikitavoloboev.xyz/macOS/apps/snippetslab.html).

#### [Tower](https://www.git-tower.com) - Git client
- Use the app to help me version control any project I am working on. Love the ability to search through commits, check out branches with ease and searching through all the Git repositories I have on my mac with quick search.
![](https://i.imgur.com/0rtjf6K.png)

#### [Paw](https://paw.cloud) - HTTP client
- Use the tool to quickly make HTTP requests and test out API endpoints.

#### [Neovim](https://neovim.io) - Text Editor
- The best text editing experience you will ever get. It is worth learning it as you will start thinking about text editing differently.
- I use some kind of vim bindings in any app I use and if there is a vim plugin for the app, I often use it. I use [vim editor](https://wiki.nikitavoloboev.xyz/text-editors/vim/vim.html) often when connecting to remote sessions and when I need a console editor.
- My config for it can be seen [here](https://github.com/nikitavoloboev/dotfile/blob/master/nvim/init.vim). I use a [few plugins](https://wiki.nikitavoloboev.xyz/text-editors/vim/vim-plugins.html) for it.

#### [Bee](https://www.neat.io/bee/) - GitHub Issue Tracker
- Use the app to stay on top of all issues across my GitHub repos. All issues I want to work on soon are put into __Next__ queue and I work through each one, one by one.

### Social
#### [Textual](https://www.codeux.com/textual/) - IRC Client
- I love IRC and this is the best macOS client for it.
- I created my own [Night Blue theme](textual#readme) for it that I love.

![](https://i.imgur.com/YgNVUMH.png)

- The app also has an awesome channel search feature that I use a lot.
<img src="http://i.imgur.com/jwVCcMb.png" width="500" alt="img">

#### [Telegram](https://desktop.telegram.org/) - Messenger
- The app has a very clean interface, a native client for macOS and stickers. Chats are not encrypted by default and don't use [approved cryptography](https://security.stackexchange.com/questions/49782/is-telegram-secure) but the client is amazing and fast.

#### [Airmail](http://airmailapp.com/) - Email client
- By far the most well designed and feature rich mail application that I have used so far. Has simple design, support for multiple accounts and a multitude of nice shortcuts that you can use.
- I approach all of my email tasks [in GTD style](https://wiki.nikitavoloboev.xyz/macOS/apps/airmail.html). Keeping my email Inbox close to 0 at all times.

#### [Tweetbot](http://tapbots.com/tweetbot/mac/) - Twitter client
- I use the app to stay up to date and communicate on Twitter.
- Tweetbot is also blocked for me during my [Focus time](https://wiki.nikitavoloboev.xyz/focusing/focusing.html). I can only post tweets but I can't visit the app to see my feeds.
- Twitter is my primary way to stay up to date on things and is my favorite social network after GitHub. I curate and publicly share all [Twitter lists](https://twitter.com/nikitavoloboev/lists) I personally use.
- I have Tweetbot open in full screen with four columns (Mentions/[Top](https://twitter.com/nikitavoloboev/lists/top)/[ML](https://twitter.com/nikitavoloboev/lists/ml)/[Other](https://twitter.com/nikitavoloboev/lists/other1)). Here is how that looks for me:

<img src="https://i.imgur.com/cy67ddm.png" width="600" alt="img">

### Writing
#### [Day One](http://dayoneapp.com/) - Digital journal
- Day One is my digital life journal.
- My entire life's experiences lives encrypted in the journal. Adding photographs I made, the thoughts I had and events that happened to me.
- I document and review [my life](https://wiki.nikitavoloboev.xyz/looking-back/looking-back.html) publicly too.
- The app has integration with [IFTTT](https://ifttt.com/day_one) which I use to automatically log all [my tweets](https://twitter.com/nikitavoloboev) and [Insgragram posts](https://instagram.com/nikitavoloboev).
- If you don't journal, I suggest you to start, it is a very powerful mind cleanser and acts as a wonderful history record of your life.

#### [Ulysses](http://www.ulyssesapp.com/) - Writing app
- The app I use to write all my [Medium](https://medium.com/@NikitaVoloboev) articles in.
- All your writing in one place is the motto and the underlying design of the app. I hook up my [wiki](https://github.com/nikitavoloboev/knowledge) as an external folder and I love how it creates an index of everything that I can search over:
<img src="http://i.imgur.com/Aa17RCQ.png" width="500" alt="img">

- It also has pretty awesome export functions that let you export the text you write to PDF, ePub and HTML. I mostly use it's ability to export text to Medium.
- I use [Ayu](https://styles.ulyssesapp.com/bundle/Ayu/5ae3545d5075368b0270daa9) theme when I write. Here is how it looks:

![](https://i.imgur.com/fp5CY5h.png)

- I describe my thoughts and approach to writing [here](https://wiki.nikitavoloboev.xyz/writing/writing.html).

#### [Marked](http://marked2app.com) - Preview rendered markdown files
- If I ever need to preview a readme or any other markdown file that I wrote or just want to read, this app is the best application for that I found. It also features live updating and quite a lot of customizable features.

### Design
#### [Sketch](https://www.sketchapp.com/) - Design tool
- Use the app to quickly prototype new designs. I also enjoy using [Figma](https://www.figma.com) a lot.

#### [Sip](https://sipapp.io/) - Collect, organize & share colors
- A great color picker I use to collect my favorite colors and color schemes.

<img src="https://i.imgur.com/YZe3vix.png" width="400" alt="img">

### Music
#### [Spotify](https://www.spotify.com/us/) - Music streaming
- Found a [lot of great music](https://open.spotify.com/user/nikitavoloboev) with this application and the phenomenal [Alfred Workflow](http://alfred-spotify-mini-player.com/) makes using the application an absolute joy.
- Quickly finding artists, songs I want to listen, instantly adding the song playing to my [Likes](https://open.spotify.com/user/nikitavoloboev/playlist/0ERn0U4qZIKC8Dy7RrMMsn?) playlist or any other playlist I want, seeing what other songs the artist has and more.
<img src="https://i.imgur.com/UgRLB92.png" width="500" alt="img">

### Images
#### [Pixave](http://www.littlehj.com/mac) - Image/GIF/Video organizer
- I use Pixave as my own personal image library. I sort images in groups and I have powerful search I can use to find any image I need.
- Here is how my library looks like:
![](https://i.imgur.com/MjGFvSb.jpg)

- The red tag means that the image was uploaded to my [Instagram page](https://instagram.com/prettiways).

#### [Pixelmator](http://www.pixelmator.com/mac/) - Image editor
- Mostly use the app to do quick, small edits on images like adding transparent background to an image.

#### [ImageOptim](https://imageoptim.com/mac) - Compress images without losing quality & remove metadata
- Quickly remove all the unneeded metadata from the image as well as compress images without losing any visual quality and saving a lot of bandwidth when uploading these images on your website or blog.

### Video
#### [IINA](https://github.com/lhc70000/iina) - Video player
- Open source alternative to VLC built specifically for macOS.
- It is based on [mpv](https://github.com/mpv-player/mpv) and has a more modern and native look than VLC.

#### [GIF Brewery](http://gifbrewery.com) - Create GIFs
- Allows me to create some great GIFs from video clips as well as converting the entire video clip into a GIF if need be.

#### [Kap](https://github.com/wulkano/kap) - Screen recorder
- An open source screen recorder I use to record GIFs.
- Has keyboard support so I can quickly start and end recording of the GIF in one hotkey.

### Finance
#### [Actual](actualbudget.com) - Budget manager
- Use it to track, budget and overview all of [my finances](https://wiki.nikitavoloboev.xyz/finance/finance.html). I use [YNAB ideology](http://classic.youneedabudget.com/method) for managing my money with the goal of being proactive with budgeting and spending. Knowing how much money I have and how much money I can spend on any given category. I find this proactive approach in dealing with money very freeing and powerful.

### Utilities
#### [Hazel](https://www.noodlesoft.com) - Automated File Organization
- Use it to fully automate my filing process and automatically commit changes in [many curated lists](https://github.com/learn-anything/curated-lists#readme).
- I use prefixes for most files. This allows me to write some great rules for my Downloads folder that will file the files where I want them to be based on the prefix.
- Here is one example of such rule:
<img src="http://i.imgur.com/7oiSYV3.png" width="500" alt="img">

#### [Next Meeting](https://itunes.apple.com/us/app/next-meeting-menu-bar-app/id1017470484?mt=12) - Show time until next event in menu bar
- It has been quite a big addition to my workflow as I know can quickly know how much time is left until my next class or some other event starts.

#### [DaisyDisk](https://daisydiskapp.com) - Visualize taken disk space
- A great tool to quickly get a visual glance over what is taking up your disk space and where.

#### [Gemini](http://macpaw.com/gemini) - Search & remove duplicate files
- A great little utility to find duplicate files in the system. Didn't get much use of it so far but it may be quite useful on occasions where I do want to clean up my system from useless files and junk.

#### [Default Folder X](http://stclairsoft.com/DefaultFolderX/) - Extend & improve open/save dialogues
- Neat little utility I mostly use to quickly go to various folders from file save windows from hotkeys.
<img src="https://i.imgur.com/RATGaNJ.png" width="400" alt="img">

#### [iStat Menus](https://bjango.com/mac/istatmenus/) - Mac system monitoring from menu bar
- Great system monitoring tools of which I use to quickly see my CPU/network/memory usage as well as quickly see my calendar and weather. I find it very valuable to know if my CPU is being abused by some application and if so by which. I then use [ProcessControl](https://github.com/vitorgalvao/alfred-workflows/tree/master/ProcessControl#readme) workflow to quickly kill off misbehaving processes.

#### [PodcastMenu](https://github.com/insidegui/PodcastMenu) - Puts Overcast in menu bar
- Allows you to listen and control playback of podcasts from [Overcast](https://overcast.fm) right from your menu bar.

### Browsers
#### [Safari](https://www.apple.com/lae/safari/)
- My favorite browser. It is incredibly fast, doesn't have the baggage of all the Google Chrome tracking and is native to macOS so it is extremely optimized and doesn't kill your battery.
- One powerful plus that Chrome does have over safari is the amount of Chrome extensions that you can get. Fortunately the ones most needed for me do [exist on Safari](https://github.com/learn-anything/safari-extensions#readme).
- My absolute favorite extension on Safari is [sVim](https://github.com/flipxfx/sVim) which gives me full keyboard control over my browser. [Here](https://gist.github.com/nikitavoloboev/c26e6a05e4e426e0542e55b7513b581c) is my config for it.

#### [Google Chrome](https://www.google.com/chrome/)
- I only use Chrome for web development due to its superior Chrome Dev tools.
- I also love the variety of [Chrome extensions](https://github.com/learn-anything/chrome-extensions#readme) that people have built and shared.

#### [Beaker Browser](https://beakerbrowser.com)
- Experimental Peer to Peer browser. Experimenting with using it more and more as I find the [technology and the implications of it fascinating](https://www.youtube.com/watch?v=-ep0ZIe6i10).

#### [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)
- Use it for web development for its superior Dev Tools in debugging CSS Grid. Prefer Chrome dev tools still.

## Command Line Apps
I use [Nix](https://nixos.org/nix/) package manager to install all the [packages I use on my system](https://gist.github.com/nikitavoloboev/3fbe13ce427132d0297f411b62f49034).

I curate a list of [interesting CLI tools](https://github.com/learn-anything/command-line-tools#readme) you can use. Below are some command line tools I personally use and love.

- [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder.
- [ripgrep](https://github.com/BurntSushi/ripgrep) - Search text for patterns fast.
- [fd](https://github.com/sharkdp/fd) - Simple, fast and user-friendly alternative to 'find'.
- [exa](https://github.com/ogham/exa) - Replacement for ls written in rust.
- [bat](https://github.com/sharkdp/bat) - Cat clone with wings.
- [up](https://github.com/apex/up) - Deploy infinitely scalable serverless apps, APIs, and sites in seconds to AWS.
- [jq](https://github.com/stedolan/jq) - JSON processor.
- [git](https://github.com/git/git) - Version control.
- [curl](https://curl.haxx.se/docs/manpage.html) - Transfer data from or to a server.
- [ccat](https://github.com/jingweno/ccat) - [cat](http://www.linfo.org/cat.html) command with colors.
- [youtube-dl](https://github.com/rg3/youtube-dl) - Download videos from YouTube and other video sites.
- [tmux](https://github.com/tmux/tmux) - Terminal multiplexer.
- [direnv](https://direnv.net/) - Environment switcher for the shell.
- [htop](https://github.com/hishamhm/htop) - Interactive text-mode process viewer for Unix systems.
- [httpie](https://github.com/jakubroztocil/httpie) - HTTP client.
- [rq](https://github.com/dflemstr/rq) - Tool for doing record analysis and transformation.
- [pandoc](https://github.com/jgm/pandoc) - Universal markup converter.
- [trash](https://github.com/sindresorhus/trash) - Move files and folders to the trash.
- [vtop](https://github.com/MrRio/vtop) - Graphical activity monitor.
- [gotop](https://github.com/cjbassi/gotop) - Terminal based graphical activity monitor inspired by gtop and vtop.
- [curl](https://github.com/curl/curl) - Transfer data, supports various protocols.
- [howdoi](https://github.com/gleitz/howdoi) - Instant coding answers.
- [asciinema](https://github.com/asciinema/asciinema) - Terminal session recorder.
- [tldr](https://github.com/tldr-pages/tldr) - Simplified and community-driven man pages.
- [imgcat](https://github.com/eddieantonio/imgcat) - Like [cat](http://www.linfo.org/cat.html) but for images.
- [screenfetch](https://github.com/KittyKatt/screenFetch) - Fetches system/theme information in terminal.
- [hugo](https://github.com/gohugoio/hugo) - Fast and flexible static site generator.
- [reflex](https://github.com/cespare/reflex) - Run a command when files change.
- [modd](https://github.com/cortesi/modd) - Flexible tool for responding to file system changes.
- [create-react-app](https://github.com/facebookincubator/create-react-app) - Create React apps with no build configuration.
- [now](https://github.com/zeit/now-cli) - Real time global deployments served over HTTP/2.
- [yarn](https://github.com/yarnpkg/yarn) - Fast, reliable, and secure dependency management.
- [hub](https://github.com/github/hub) - GitHub wrapper.
- [entr](http://www.entrproject.org/) - Run arbitrary commands when files change.
- [xsv](https://github.com/BurntSushi/xsv) - Fast CSV command line toolkit written in Rust.
- [pv](https://ivarch.com/programs/pv.shtml) - Pipe Viewer.
- [m-cli](https://github.com/rgcr/m-cli) - Useful utils for macOS.
- [pgcli](https://github.com/dbcli/pgcli) - Postgres CLI with autocompletion and syntax highlighting.
- [mas](https://github.com/mas-cli/mas) - CLI for mac app store.
- [loc](https://github.com/cgag/loc) - Count lines of code quickly.
- [alfred](https://godoc.org/github.com/jason0x43/go-alfred/alfred) - Manage Go-based Alfred workflows.
- [neofetch](https://github.com/dylanaraps/neofetch) - System information tool.
- [license-up](https://github.com/nikitavoloboev/license-up) - Create a license quickly for your project.
- [piknik](https://github.com/jedisct1/piknik) - Copy/paste anything over the network.
- [bench](https://github.com/Gabriel439/bench) - Command-line benchmark tool.
- [ghq](https://github.com/motemen/ghq) - Manage remote repository clones.
- [npx](https://github.com/zkat/npx) - Execute npm package binaries.
- [devd](https://github.com/cortesi/devd) - Local webserver for developers.

## Preference Panes
- [GPG Suite](https://gpgtools.org/) - Encrypt, decrypt, sign and verify files or messages.
- [RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) - Set the default application used for various URL schemes, file extensions, file types, MIME types, and Uniform Type Identifiers.

## Desktop Screenshot
![](https://i.imgur.com/3cPVMJQ.jpg)
> Using [Neofetch](https://github.com/dylanaraps/neofetch)

## Alfred launcher
![](https://i.imgur.com/FpAKitO.jpg)
> Searching [Alfred Learn Anything](https://github.com/nikitavoloboev/alfred-learn-anything). Using [Ayu](https://www.alfredapp.com/extras/theme/6aSDGHwmmC/) theme.

## Launchpad
![](https://i.imgur.com/glXw4jB.jpg)
> Using [this](https://www.macrumors.com/how-to/group-app-icons-macos-dock) to add spaces between apps in Dock.

## [My wonderful world of iOS 📱](https://github.com/nikitavoloboev/my-ios#readme)
If you found this interesting, I also have [similar repository](https://github.com/nikitavoloboev/my-ios#readme) going over what applications I use on iOS as well as how and why I use them.

<a align="center" href="https://github.com/nikitavoloboev/my-ios#readme">
    <img width="250" heigth="400" src="https://i.imgur.com/Ew6Ldsn.jpg"></a>

<a align="center" href="https://github.com/nikitavoloboev/my-ios#readme">
    <img width="250" heigth="400" src="https://i.imgur.com/CcYlsSg.jpg"></a>

<a align="center" href="https://github.com/nikitavoloboev/my-ios#readme">
    <img width="250" heigth="400" src="https://i.imgur.com/rD6DEmB.jpg"></a>

## Similar Setups
Here you can find more setups by other people that you can take ideas and inspiration from.
- [Works for me](https://works-for-me.github.io/) - Collection of developer toolkits.
- [Use This Interviews](https://usesthis.com) - What do people use to get stuff done?

## Related
- [Awesome mac](https://github.com/jaywcjlove/awesome-mac#readme)
- [Interesting macOS apps](https://github.com/learn-anything/macos-apps#readme)
- [Open Source macOS apps](https://github.com/serhii-londar/open-source-mac-os-apps#readme)

## Contributing
If you shared a similar personal setup to this, be it for Windows, Linux or anything else, you can add it in [Similar Setups](#similar-setups) section.

I love finding new awesome tools and apps. If you have a favorite tool or app that you think I missed, please [say it](../../issues/new).

## Thank you 💜
You can support me on [Patreon](https://www.patreon.com/nikitavoloboev) or look into [other projects](https://nikitavoloboev.xyz/projects) I shared.

## License
MIT © [Nikita Voloboev](https://www.nikitavoloboev.xyz)