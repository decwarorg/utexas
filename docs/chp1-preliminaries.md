
Page 4, creating a test file. Note that $ is the TOPS-10 echo for the escape key. Where you see \$, hit escape.

    .make test
    *ihello world$ex$$
    .type test
    
chapter1 covers the basics of teco for file editing and octal numbers. it makes sense to include disucssion of the appendices on ddt and teco here, especially since both are dependent on the control characters of the terminal era and these can be an initial speed bump with modern hardware. remembering how to send a bare line feed is a reccuring theme (it's control-j). so before anything else, here's useful notes about some important key combinations. this is for a macbook.

* Terminal Shortcuts: Press Control + [A-Z] to send the matching ASCII code 1 through 26.
* Unicode Hex Input: Enable "Unicode Hex Input" in keyboard settings, then hold Option (⌥) and type the 4-digit hex code (like 0008 for backspace).
* Null (0x00): Control + @
* Backspace (0x08): Control + H (or Delete key)
* Tab (0x09): Control + I
* Line Feed (0x0A): Control + J
* Carriage Return (0x0D): Control + M (Enter)
* Escape (0x1B): Control + [

teco works conceptually much like early video terminal screen editors such as vi and emacs, not surprisingly since it's their direct ancestor. but teco is from the era before video terminals. before teletypes even, since it was created for editing code on paper tape.

it turns out to be very useful to imagine that you are working with a file in a video terminal screen editor, lets say vi. you can move the cursor about in the file, and issue commands. but here's the thing. the video screen is invisible! instead, there is only a physical teletype, or typewriter if you prefer. the video terminal screen editor is there, but invisible, and you have to operate it using the physical teletype in front of you. it sounds worse than it is. once you start seeing the invisible video screen in your minds eye, the actual interactions with teco on the teletype make complete sense and feels very familiar to a vi or emacs user.

another curiosity is the escape key. the escape key is mighty in teco, by far the most important key on the keyboard. this reflects broader dec practice. escape, also known as the alt key, is special in many dec contexts. with teco, return to our invisible video screen and teletype. when we are typing and characters are appearing on the paper in front of us, we need a special key on our keyboard that tells teco when we are finished with the previous command and beginning a new one. we realize most of the keys on the keyboard already have a purpose, but the escape key is free! escape key it is. when we hit escape, a dollar-sign character appears and we can type a new command. if we hit escape twice, two dollar-sign characters appear on the paper, and teco immediately executes all of the commands since the last double-escape.

