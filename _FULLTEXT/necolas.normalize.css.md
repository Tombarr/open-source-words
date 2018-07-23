normalize.css A modern alternative to CSS resets NPM sh npm install --save normalize.css CDN See https://yarnpkg.com/en/package/normalize.css Download See https://necolas.github.io/normalize.css/latest/normalize.css What does it do? Preserves useful defaults, unlike many CSS resets. Normalizes styles for a wide range of elements. Corrects bugs and common browser inconsistencies. Improves usability with subtle modifications. Explains what code does using detailed comments. Browser support Chrome Edge Firefox ESR+ Internet Explorer 10+ Safari 8+ Opera Extended details and known issues Additional detail and explanation of the esoteric parts of normalize.css. pre, code, kbd, samp The font-family: monospace, monospace hack fixes the inheritance and scaling of font-size for preformatted text. The duplication of monospace is intentional. Source. sub, sup Normally, using sub or sup affects the line-box height of text in all browsers. Source. select By default, Chrome on OS X and Safari on OS X allow very limited styling of select, unless a border property is set. The default font weight on optgroup elements cannot safely be changed in Chrome on OSX and Safari on OS X. [type="checkbox"] It is recommended that you do not style checkbox and radio inputs as Firefoxs implementation does not respect box-sizing, padding, or width. [type="number"] Certain font size values applied to number inputs cause the cursor style of the decrement button to change from default to text. [type="search"] The search input is not fully stylable by default. In Chrome and Safari on OSX/iOS you cant control font, padding, border, or background. In Chrome and Safari on Windows you cant control border properly. It will apply border-width but will only show a border color (which cannot be controlled) for the outer 1px of that border. Applying -webkit-appearance: textfield addresses these issues without removing the benefits of search inputs (e.g. showing past searches). Contributing Please read the contribution guidelines in order to make the contribution process easy and effective for everyone involved.