wiki \ documentation \ twitter \ community \ sponsors \ gitter chat \ 中文官网 spacevim is a community driven modular vim distribution it manages collections of plugins in layers which help collect related packages together to provide ide like features spacevim is not just a vimrc but an ultimate vim configuration it contains many built in features the last release is v0 8 0 check out following head page for what happened since last release see the quick start guide documentation or the available layers for more information here is a throughput graph of the repository for the last few weeks vim markdown toc gfm new features project layout support spacevim credits thanks vim markdown toc new features this is a list of latest features implemented in spacevim use toml as default configuration here is an example for using toml as spacevim config toml this is basic configuration example for spacevim all spacevim option below option section options set spacevim theme by default colorscheme layer is not loaded if you want to use more colorscheme please load the colorscheme layer colorscheme gruvbox background dark disable guicolors in basic mode many terminal do not support 24bit true colors enable guicolors false disable statusline separator if you want to use other value please install nerd fonts statusline separator nil statusline inactive separator bar buffer index type 4 windows index type 3 enable tabline filetype icon false enable statusline mode false statusline unicode symbols false enable vim compatible mode avoid changing origin vim key bindings vimcompatible true enable autocomplete layer layers name autocomplete auto completion return key behavior complete auto completion tab key behavior cycle layers name shell default position top default height 30 iedit mode spacevim uses powerful iedit mode to quick edit multiple occurrences of a symbol or selection two new modes iedit normal iedit insert the default color for iedit is red green which is based on the current colorscheme highlight cursor symbol spacevim supports highlighting of the current symbol on demand and adds a transient state to easily navigate and rename this symbol fly grep in vim with this feature vim will display the searching result as you type of course it is running asynchronously before using this feature you need to install a searching tool flygrep works through search tools ag rg ack pt and grep choose one you like mnemonic key bindings navigation you dont need to remember any key bindings as the mapping guide will show up after the spc is pressed the mapping guide is also available for g z and s help description for key bindings use spc h d k to get the help description of a key binding and gd to find definition of key bindings asynchronous plugin manager create an ui for dein vim the best asynchronous vim plugin manager for more features please read spacevims blog project layout txt ├─ ci build automation ├─ github issue pr templates ├─ spacevim d project specific configuration ├─ autoload spacevim vim spacevim core file ├─ autoload spacevim api public apis ├─ autoload spacevim layers available layers ├─ autoload spacevim plugins buildin plugins ├─ autoload spacevim mapping mapping guide ├─ doc help cn en ├─ docs website cn en ├─ wiki wiki cn en ├─ bin executable └─ test tests support spacevim the best way to support spacevim is to contribute to it either by reporting bugs helping the community on the gitter chat or sending pull requests for more info please check our development guidelines if you want to show your support financially you can buy a drink for the maintainer by clicking following icon wechat alipay bitcoin 1dtuveg81c2l9nehdavtaabrcr3pn5xpfv credits thanks this project exists thanks to all the people who have contributed gabirel and his hack spacevim everettjf and his spacevimtutorial vimdoc generate doc file for spacevim rafael bodill and his vim config bailey ling and his dotvim authors of all the plugins used in spacevim vim set nowrap