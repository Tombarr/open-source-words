pikaday a refreshing javascript datepicker lightweight less than 5kb minified and gzipped no dependencies but plays well with moment js modular css classes for easy styling try pikaday demo → production ready since version 1 0 0 pikaday is stable and used in production if you do however find bugs or have feature requests please submit them to the github issue tracker also see the changelog installation npm install pikaday usage pikaday can be bound to an input field html input type text id datepicker add the javascript to the end of your document html script src pikaday js script script var picker new pikaday field document getelementbyid datepicker script if youre using jquery make sure to pass only the first element javascript var picker new pikaday field datepicker 0 if the pikaday instance is not bound to a field you can append the element anywhere javascript var field document getelementbyid datepicker var picker new pikaday onselect function date field value picker tostring field parentnode insertbefore picker el field nextsibling formatting by default dates are formatted and parsed using standard javascript date object if moment js is available in scope it will be used to format and parse input values you can pass an additional format option to the configuration which will be passed to the moment constructor see the moment js example for a full version html var picker new pikaday field document getelementbyid datepicker format d mmm yyyy onselect function console log this getmoment format do mmmm yyyy for more advanced and flexible formatting you can pass your own tostring function to the configuration which will be used to format the date object this function has the following signature tostring date format yyyy mm dd you should return a string from it be careful though if the formatted string that you return cannot be correctly parsed by the date parse method or by moment if it is available then you must provide your own parse function in the config this function will be passed the formatted string and the format tostring datestring format yyyy mm dd javascript var picker new pikaday field document getelementbyid datepicker format d m yyyy tostring date format you should do formatting based on the passed format but we will just return d m yyyy for simplicity const day date getdate const month date getmonth 1 const year date getfullyear return day month year parse datestring format datestring is the result of tostring method const parts datestring split const day parseint parts 0 10 const month parseint parts 1 1 10 const year parseint parts 1 10 return new date year month day configuration as the examples demonstrate above pikaday has many useful options field bind the datepicker to a form field trigger use a different element to trigger opening the datepicker see trigger example default to field bound automatically show hide the datepicker on field focus default true if field is set arialabel data attribute on the input field with an aria assistance tekst only applied when bound is set position preferred position of the datepicker relative to the form field e g top right bottom right note automatic adjustment may occur to avoid datepicker from being displayed outside the viewport see positions example default to bottom left reposition can be set to false to not reposition datepicker within the viewport forcing it to take the configured position default true container dom node to render calendar into see container example default undefined format the default output format for tostring and field value requires moment js for custom formatting formatstrict the default flag for moments strict date parsing requires moment js for custom formatting tostring date format function which will be used for custom formatting this function will take precedence over moment parse datestring format function which will be used for parsing input string and getting a date object from it this function will take precedence over moment defaultdate the initial date to view when first opened setdefaultdate make the defaultdate the initial selected value firstday first day of the week 0 sunday 1 monday etc mindate the minimum earliest date that can be selected this should be a native date object e g new date or moment todate maxdate the maximum latest date that can be selected this should be a native date object e g new date or moment todate disableweekends disallow selection of saturdays or sundays disabledayfn callback function that gets passed a date object for each day in view should return true to disable selection of that day yearrange number of years either side e g 10 or array of upper lower range e g 1900 2015 showweeknumber show the iso week number at the head of the row default false pickwholeweek select a whole week instead of a day default false isrtl reverse the calendar for right to left languages i18n language defaults for month and weekday names see internationalization below yearsuffix additional text to append to the year in the title showmonthafteryear render the month after year in the title default false showdaysinnextandpreviousmonths render days of the calendar grid that fall in the next or previous months default false enableselectiondaysinnextandpreviousmonths allows user to select date that is in the next or previous months default false numberofmonths number of visible calendars maincalendar when numberofmonths is used this will help you to choose where the main calendar will be default left can be set to right only used for the first display or when a selected date is not already visible events array of dates that you would like to differentiate from regular days e g sat jun 28 2017 sun jun 29 2017 tue jul 01 2017 theme define a classname that can be used as a hook for styling different themes see theme example default null blurfieldonselect defines if the field is blurred when a date is selected default true onselect callback function for when a date is selected onopen callback function for when the picker becomes visible onclose callback function for when the picker is hidden ondraw callback function for when the picker draws a new month keyboardinput enable keyboard input support default true styling if the reposition configuration option is enabled default pikaday will apply css classes to the datepicker according to how it is positioned top aligned left aligned right aligned bottom aligned note that the dom element at any time will typically have 2 css classes eg top aligned right aligned etc jquery plugin the normal version of pikaday does not require jquery however there is a jquery plugin if that floats your boat see plugins pikaday jquery js in the repository this version requires jquery naturally and can be used like other plugins see the jquery example for a full version html p p activate datepickers for all elements with a class of code datepicker code datepicker pikaday firstday 1 p p chain a few methods for the first datepicker jquery style datepicker eq 0 pikaday show pikaday gotoyear 2042 p p amd support if you use a modular script loader than pikaday is not bound to the global object and will fit nicely in your build process you can require pikaday just like any other module see the amd example for a full version javascript require pikaday function pikaday var picker new pikaday field document getelementbyid datepicker the same applies for the jquery plugin mentioned above see the jquery amd example for a full version javascript require jquery pikaday jquery function datepicker pikaday commonjs module support if you use a commonjs compatible environment you can use the require function to import pikaday javascript var pikaday require pikaday when you bundle all your required modules with browserify and you dont use moment js specify the ignore option browserify main js o bundle js i moment ruby on rails if youre using ruby on rails make sure to check out the pikaday gem methods you can control the date picker after creation javascript var picker new pikaday field document getelementbyid datepicker get and set date picker tostring yyyy mm dd returns the selected date in a string format if moment js exists recommended then pikaday can return any format that moment understands you can also provide your own tostring function and do the formatting yourself read more in the formatting section if neither moment object exists nor tostring function is provided javascripts default todatestring method will be used picker getdate returns a basic javascript date object of the selected day or null if no selection picker setdate 2015 01 01 set the current selection this will be restricted within the bounds of mindate and maxdate options if theyre specified you can optionally pass a boolean as the second parameter to prevent triggering of the onselect callback true allowing the date to be set silently picker getmoment returns a moment js object for the selected date moment must be loaded before pikaday picker setmoment moment 14th february 2014 ddo mmmm yyyy set the current selection with a moment js object see setdate for details change current view picker gotodate new date 2014 1 change the current view to see a specific date this example will jump to february 2014 month is a zero based index picker gototoday shortcut for picker gotodate new date picker gotomonth 2 change the current view by month 0 january 1 februrary etc picker nextmonth picker prevmonth go to the next or previous month this will change year if necessary picker gotoyear change the year being viewed picker setmindate update the minimum earliest date that can be selected picker setmaxdate update the maximum latest date that can be selected picker setstartrange update the range start date for using two pikaday instances to select a date range picker setendrange update the range end date for using two pikaday instances to select a date range show and hide datepicker picker isvisible returns true or false picker show make the picker visible picker adjustposition recalculate and change the position of the picker picker hide hide the picker making it invisible picker destroy hide the picker and remove all event listeners — no going back internationalization the default i18n configuration format looks like this javascript i18n previousmonth previous month nextmonth next month months january february march april may june july august september october november december weekdays sunday monday tuesday wednesday thursday friday saturday weekdaysshort sun mon tue wed thu fri sat you must provide 12 months and 7 weekdays with abbreviations always specify weekdays in this order with sunday first you can change the firstday option to reorder if necessary 0 sunday 1 monday etc you can also set isrtl to true for languages that are read right to left extensions timepicker pikaday is a pure datepicker it will not support picking a time of day however there have been efforts to add time support to pikaday see 1 and 18 these reside in their own fork you can use the work owenmead did most recently at owenmead pikaday a more simple time selection approach done by xeeali at xeeali pikaday is based on version 1 2 0 also stas has a fork stas pikaday but is now quite old browser compatibility ie 7 chrome 8 firefox 3 5 safari 3 opera 10 6 authors david bushell http dbushell com dbushell ramiro rikkert github ramrik thanks to shoogledesigns for the name copyright © 2014 david bushell bsd mit license