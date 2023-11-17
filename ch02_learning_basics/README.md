# Chapter 2 Learning Basics

We make use of <b>variables</b> in our programs to store and label data elements like a piece of text or a number. We will make use of these constructs regularly - for instance, to hold the user score in a game, or keep track on how many lives are left. We might need to store different data elements in different scenarios.

## Tasks



## Creating Variables

### How to create a variable

To create a variable we must give it a unique name and it is a good idea to pick a name that briefly describes what data is being stored. What the variable then stores is called a <b>value</b>. When we create a variable and give it a value we normally say *_assigning a value to a variable_*.

For example:

```
score = 0
print(score) # we can output the value of score to the screen
```
<pre>
0
</pre>

### Using numbers

As we already say, we can use variables to store a whole number or `integer` which in turn can be used in arithmetic calculations.

An example of a simple calculation:

```
x = 2
y = x * 3
print(y) 
```

<pre>
6
</pre>

At any point in the program you can change the value of a variable. All you need to do is assign it to a different value.

```
x = 5
print(y) # Do you think the value of y will change now?
```
<pre>
6
</pre>

You guessed it. For `y` to reflect the new value of `x` we need to perform the calculation again. This is because the computer executes statements line by line and to get the results expected our instructions need to be written in the correct order.

```
x = 5
y = x * 3
print(y)
```
<pre>
15
</pre>

Simple mathematical operators:

|  Symbol  | Meaning | Usage       |
| -------- | ------- |-------------|
| +        | plus    | `z = x + y` |
| -        | minus   | `z = x - y` |
| *        | times   | `z = x * y` |
| /        | divide  | `z = x / y` |

More difficult mathematical operators:

|  Symbol  | Meaning      | Usage       |
| -------- | ------------ |-------------|
| //       | floor divide | `z = x // y`|
| %        | remainder    | `z = x % y` |
| **       | power        | `z = x ** y`|

When we code, different types of numbers can be stored in our variables. Whole numbers are of type `integer` and numbers with a decimal point in them are of type `float`. Both types of numbers can be used in arithmetic calculations.

### Working with strings

A <b>string</b> is data that is made up of <b>a sequence of letters or other characters</b> like punctuation symbols and numbers. Words and sentences are stored as strings in our programs. Most programs use at least one of these kind of variables. Anything that you can type in your keyboard can be stored in a string variable. When using the `input()` function to ask the user to type something you should treat the value as a string.

```
favourite_colour = "orange"
print(favourite_colour)
```

Python gives us a lot of <b>built-in functionality</b> to work with our string variables.

1. We can join strings together using the `+` operator

```
favourite_colour = input("Enter your favourite colour: ") # ask user to enter a value
sentence = "Your favourite colour is " + favourite_colour + "."
print(sentence)
```
<pre>
Enter your favourite colour: 
orange
Your favourite colour is orange.
</pre>

2. We can get the length of a string using the `len()` function

```
message = "Hey there, giraffe..."
message_length = len(message) # we need to store the length in a variable to use it later
print(message_length)
```
<pre>
21
</pre>

3. Other string functions you can experiment with on a string variable e.g. `str`

|  Function  | Description                          | Usage                       | Example            |
| ---------- | ------------------------------------ | --------------------------- | ------------------ |
| `strip()`  | Remove leading and trailing spaces   | `str.strip()`               | `"  hi  " >> "hi"` |
| `lower()`  | Convert characters to lower case     | `str.lower()`               | `"Hi" >> "hi"`     |
| `upper()`  | Convert characters to upper case     | `str.upper()`               | `"Hi" >> "HI"`     |
| `count()`  | Count occurrance of a letter or word | `str.count(phrase)`         | `"Hi", "i" >> 1`   |

```
message = "   Hey there, giraffe...   "
message = message.strip() # our string variable is message in this case
print(message)
```
<pre>
"Hey there, giraffe..."
</pre>

### Making lists

Simple variables are great but we also need to be able to store a group of data items. We can create <b>list</b> variables to <b>store multiple data items under one label</b>. There are many use cases in which lists could be useful in games. For example, a list can store a deck of cards for a game of Twenty-One. Upon request, the next card is dealt from the list. A deck consists of 52 unique cards, so rather than creating 52 variables to store cards, we can store all the card values in a list variable.

```
deck = ["1 hearts", "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts"]
```

Every value in a list has a <b>unique position</b> which is identified with a number. The very first position in the list has a value of 0. We can use the position to get individual values from a list variable.

To access a memory location within a list we need to type the name of the list variable e.g., `deck`, followed by the item's position in the list within square brackets `[]`, e.g., `[2]`. To access the third data item we write `deck[2]`. Here is an example:

```
firstItem = deck[0] # a single value in a list can be treated like a simple variable
thirdItem = deck[2]

print(firstItem)
print(thirdItem)
print(deck[0])
print(deck[2])
```

<pre>
1 hearts
3 hearts
1 hearts
3 hearts
</pre>

Python gives us a lot of <b>built-in functionality</b> to work with our list variables. Some functions will already seem familiar to you.

1. We can get the length of a list using the `len()` function

```
numbers = [10, 5, 8, 9]
numbers_length = len(numbers) # we need to store the length in a variable to use it later
print(numbers_length)
```
<pre>
4
</pre>

2. We can get the number of occurrances of a data item in a list using the `count()` function

```
fruit = ["apple", "orange", "apple", "kiwi", "banana"]
count_apple = fruit.count("apple")
print(count_apple)
```
<pre>
2
</pre>

3. Other list functions you can experiment with on a list variable e.g. `mylist`

|  Function  | Description                          | Usage                       |
| ---------- | ------------------------------------ | --------------------------- |
| `append()` | Add a data item at the end of list   | `mylist.append(item)`       |
| `clear()`  | Remove all data items in a list      | `mylist.clear()`            |
| `insert()` | Put a data item at a position        | `mylist.insert(pos, item)`  |
| `pop()`    | Get the last item and remove it      | `mylist.pop()`              |
| `remove()` | Remove one data item from the list   | `mylist.remove(item)`       |
| `reverse()`| Reverse the position list items      | `mylist.reverse() `         |
| `sort()`   | Sort data items in ascending order   | `mylist.sort()`             |

## Making decisions

Decision making is an important part of our logical thinking and it is often based on answers to questions like, "Do I have any lives yet?" or, "Am I close to reaching the high score?". We want our algorithms to have this ability to "make decisions". Making computers answer human questions is obviously difficult, but, computers are very good at <b>comparing two values</b> and most of the time this is enough to create very interesting game play.

### Making comparisons

The questions that computers are able to answer have only two possible outcomes: `True` or `False`. You know by now that these two <b>Boolean</b> values are the backbone of computer science because they represent <b>binary</b>. You can create variables that store a Boolean value, just note that in Python, these values are special words and must start with a capital letter.

```
answer_true = True
answer_false = False
```

The questions our algorithms will ask are essentially made up of a series of <b>comparisons between two values</b>. A computer is able to <b>make comparisons</b> by using <b>logical operators</b>. These questions are actually called <b>Boolean expressions</b>.

```
player_age = 7
are_they_equal = (player_age == 10) # Boolean expression
print(are_they_equal) 
```

<pre>
False
</pre>

|  Symbol  | Meaning     | Boolean Expression       | Question                         |
| -------- | ----------- |--------------------------|----------------------------------|
| ==       | equal to    | `x == y`                 | Is x <b>equal to</b> y?          |
| !=       | not equal to| `x != y`                 | Is x <b>not equal to</b> y?      |
| <        | less than   | `x < y`                  | Is x <b>less than</b> y?         |
| >        | greater than| `x > y`                  | Is x <b>greater than</b> y?      |

Do you remember how we illustrate decision making in flowcharts?

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="371px" viewBox="-0.5 -0.5 371 501" content="&lt;mxfile&gt;&lt;diagram id=&quot;bMRsobfcPnyK9mfBw7rN&quot; name=&quot;Page-1&quot;&gt;&lt;mxGraphModel dx=&quot;566&quot; dy=&quot;440&quot; grid=&quot;1&quot; gridSize=&quot;10&quot; guides=&quot;1&quot; tooltips=&quot;1&quot; connect=&quot;1&quot; arrows=&quot;1&quot; fold=&quot;1&quot; page=&quot;1&quot; pageScale=&quot;1&quot; pageWidth=&quot;827&quot; pageHeight=&quot;1169&quot; math=&quot;0&quot; shadow=&quot;0&quot;&gt;&lt;root&gt;&lt;mxCell id=&quot;0&quot;/&gt;&lt;mxCell id=&quot;1&quot; parent=&quot;0&quot;/&gt;&lt;mxCell id=&quot;10&quot; style=&quot;edgeStyle=none;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;2&quot; target=&quot;3&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;2&quot; value=&quot;&amp;lt;font face=&amp;quot;Courier New&amp;quot;&amp;gt;START&amp;lt;/font&amp;gt;&quot; style=&quot;ellipse;whiteSpace=wrap;html=1;fillColor=#a20025;fontColor=#ffffff;strokeColor=#6F0000;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;60&quot; y=&quot;30&quot; width=&quot;80&quot; height=&quot;50&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;9&quot; style=&quot;edgeStyle=none;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;3&quot; target=&quot;4&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;3&quot; value=&quot;&amp;lt;font face=&amp;quot;Courier New&amp;quot;&amp;gt;x = 12&amp;lt;br&amp;gt;y = 5&amp;lt;/font&amp;gt;&quot; style=&quot;rounded=0;whiteSpace=wrap;html=1;shadow=0;fillColor=#d80073;fontColor=#ffffff;strokeColor=#A50040;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;40&quot; y=&quot;120&quot; width=&quot;120&quot; height=&quot;60&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;6&quot; style=&quot;edgeStyle=none;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;4&quot; target=&quot;5&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&lt;Array as=&quot;points&quot;&gt;&lt;mxPoint x=&quot;200&quot; y=&quot;260&quot;/&gt;&lt;/Array&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;11&quot; style=&quot;edgeStyle=none;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;4&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&lt;mxPoint x=&quot;100&quot; y=&quot;360&quot; as=&quot;targetPoint&quot;/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;4&quot; value=&quot;&amp;lt;font face=&amp;quot;Courier New&amp;quot;&amp;gt;is x &amp;amp;lt; y&amp;lt;/font&amp;gt;&quot; style=&quot;rhombus;whiteSpace=wrap;html=1;fillColor=#60a917;fontColor=#ffffff;strokeColor=#2D7600;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;40&quot; y=&quot;220&quot; width=&quot;120&quot; height=&quot;80&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;18&quot; style=&quot;edgeStyle=none;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;5&quot; target=&quot;14&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&lt;Array as=&quot;points&quot;&gt;&lt;mxPoint x=&quot;310&quot; y=&quot;505&quot;/&gt;&lt;/Array&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;5&quot; value=&quot;&amp;quot;x is &amp;lt;br&amp;gt;less than y&amp;quot;&quot; style=&quot;shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fontFamily=Courier New;fillColor=#1ba1e2;fontColor=#ffffff;strokeColor=#006EAF;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;230&quot; y=&quot;230&quot; width=&quot;160&quot; height=&quot;60&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;8&quot; value=&quot;TRUE&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontFamily=Courier New;fontStyle=1&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;175&quot; y=&quot;235&quot; width=&quot;50&quot; height=&quot;30&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;15&quot; style=&quot;edgeStyle=none;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fontFamily=Courier New;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;12&quot; target=&quot;14&quot;&gt;&lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;12&quot; value=&quot;&amp;quot;x is &amp;lt;br&amp;gt;greater &amp;lt;br&amp;gt;or equal to y&amp;quot;&quot; style=&quot;shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fontFamily=Courier New;fillColor=#1ba1e2;fontColor=#ffffff;strokeColor=#006EAF;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;20&quot; y=&quot;360&quot; width=&quot;160&quot; height=&quot;60&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;14&quot; value=&quot;&amp;lt;font face=&amp;quot;Courier New&amp;quot;&amp;gt;END&amp;lt;/font&amp;gt;&quot; style=&quot;ellipse;whiteSpace=wrap;html=1;fillColor=#a20025;fontColor=#ffffff;strokeColor=#6F0000;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;60&quot; y=&quot;480&quot; width=&quot;80&quot; height=&quot;50&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=&quot;19&quot; value=&quot;FALSE&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontFamily=Courier New;fontStyle=1&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&lt;mxGeometry x=&quot;100&quot; y=&quot;315&quot; width=&quot;60&quot; height=&quot;30&quot; as=&quot;geometry&quot;/&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;&lt;/diagram&gt;&lt;/mxfile&gt;" onclick="(function(svg){var src=window.event.target||window.event.srcElement;while (src!=null&amp;&amp;src.nodeName.toLowerCase()!='a'){src=src.parentNode;}if(src==null){if(svg.wnd!=null&amp;&amp;!svg.wnd.closed){svg.wnd.focus();}else{var r=function(evt){if(evt.data=='ready'&amp;&amp;evt.source==svg.wnd){svg.wnd.postMessage(decodeURIComponent(svg.getAttribute('content')),'*');window.removeEventListener('message',r);}};window.addEventListener('message',r);svg.wnd=window.open('https://viewer.diagrams.net/?client=1&amp;page=0&amp;edit=_blank');}}})(this);" style="cursor:pointer;max-width:100%;max-height:501px;"><defs/><g><path d="M 80 50 L 80 83.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 80 88.88 L 76.5 81.88 L 80 83.63 L 83.5 81.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><ellipse cx="80" cy="25" rx="40" ry="25" fill="#a20025" stroke="#6f0000" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 25px; margin-left: 41px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;"><font face="Courier New">START</font></div></div></div></foreignObject><text x="80" y="29" fill="#ffffff" font-family="Helvetica" font-size="12px" text-anchor="middle">START</text></switch></g><path d="M 80 150 L 80 183.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 80 188.88 L 76.5 181.88 L 80 183.63 L 83.5 181.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="20" y="90" width="120" height="60" fill="#d80073" stroke="#a50040" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 120px; margin-left: 21px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;"><font face="Courier New">x = 12<br />y = 5</font></div></div></div></foreignObject><text x="80" y="124" fill="#ffffff" font-family="Helvetica" font-size="12px" text-anchor="middle">x = 12...</text></switch></g><path d="M 140 230 L 170 230 Q 180 230 190 230 L 213.63 230" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 218.88 230 L 211.88 233.5 L 213.63 230 L 211.88 226.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 80 270 L 80 323.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 80 328.88 L 76.5 321.88 L 80 323.63 L 83.5 321.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 80 190 L 140 230 L 80 270 L 20 230 Z" fill="#60a917" stroke="#2d7600" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 230px; margin-left: 21px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;"><font face="Courier New">is x &lt; y</font></div></div></div></foreignObject><text x="80" y="234" fill="#ffffff" font-family="Helvetica" font-size="12px" text-anchor="middle">is x &lt; y</text></switch></g><path d="M 290 260 L 290 465 Q 290 475 280 475 L 126.37 475" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 121.12 475 L 128.12 471.5 L 126.37 475 L 128.12 478.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 210 260 L 230 200 L 370 200 L 350 260 Z" fill="#1ba1e2" stroke="#006eaf" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 158px; height: 1px; padding-top: 230px; margin-left: 211px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: &quot;Courier New&quot;; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">"x is <br />less than y"</div></div></div></foreignObject><text x="290" y="234" fill="#ffffff" font-family="Courier New" font-size="12px" text-anchor="middle">"x is...</text></switch></g><rect x="155" y="205" width="50" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 220px; margin-left: 180px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: &quot;Courier New&quot;; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; font-weight: bold; white-space: nowrap;">TRUE</div></div></div></foreignObject><text x="180" y="224" fill="rgb(0, 0, 0)" font-family="Courier New" font-size="12px" text-anchor="middle" font-weight="bold">TRUE</text></switch></g><path d="M 80 390 L 80 443.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 80 448.88 L 76.5 441.88 L 80 443.63 L 83.5 441.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 0 390 L 20 330 L 160 330 L 140 390 Z" fill="#1ba1e2" stroke="#006eaf" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 158px; height: 1px; padding-top: 360px; margin-left: 1px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: &quot;Courier New&quot;; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">"x is <br />greater <br />or equal to y"</div></div></div></foreignObject><text x="80" y="364" fill="#ffffff" font-family="Courier New" font-size="12px" text-anchor="middle">"x is...</text></switch></g><ellipse cx="80" cy="475" rx="40" ry="25" fill="#a20025" stroke="#6f0000" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 475px; margin-left: 41px;"><div data-drawio-colors="color: #ffffff; " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;"><font face="Courier New">END</font></div></div></div></foreignObject><text x="80" y="479" fill="#ffffff" font-family="Helvetica" font-size="12px" text-anchor="middle">END</text></switch></g><rect x="80" y="285" width="60" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 300px; margin-left: 110px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: &quot;Courier New&quot;; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; font-weight: bold; white-space: nowrap;">FALSE</div></div></div></foreignObject><text x="110" y="304" fill="rgb(0, 0, 0)" font-family="Courier New" font-size="12px" text-anchor="middle" font-weight="bold">FALSE</text></switch></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>

Simple questions in the Python language use the following format:

```
if answer_true: 
    print("Yes, answer is True!")
else:
    print(No, answer is False!)
```

Example:

```
x = 12
y = 5
if x < y:
   print("x is less than y")
else:
   print("x is greater or equal to y")
```
<pre>
x is greater or equal to y
</pre>

## Multiple comparisons using logic gates

To make multiple comparisons or ask more complex questions in one statement we use <b>logic gate operations</b> like `and`, `or` and `not`. 

```
monters = 3
coins = 4

is_game_over = (monters == 4 or coins == 0) # complex Boolean expression that evaluates to True or False

if is_game_over == True
   print("Game over!")
```
Remember from <a target="blank" href="">Chapter 10</a> that when using `or` only one answer needs to be `True` for the entire expression to be `True`, when using `and`, all answers need to be `True` for the expression to be `True`.

For example, let us imagine that to go up a level in a game the player must have collected at least 1 star <b>and</b> score over 500 points. First, we will create variables to store the amount of stars and the points. Then, we write a Boolean expression so that the algorithm can decide whether another level is unlocked or not.

```
score = 493
stars = 2

if score > 500 and stars > 0:
   print("Congratulations, you unlocked a new level!")
else:
   print("Oh no. Seems like you are stuck. Better luck next time.")
```
<pre>
Oh no. Seems like you are stuck. Better luck next time.
</pre>

### Branching 

You probably already guessed that we pose questions in a certain way so that the <b>computer can decide which parts of our program need to run</b> based on a <b>condition</b> or <b>test</b>. When we write have multiple code blocks but only one should run, we call it <b>branching</b>.

1. One branch

This is the simplest example which is an `if` statement on its own. There is only one outcome, so only one branch. The code snippet in the branch will run only when the condition is `True`.

```
spells = 11
if spells > 10:
   print("You gained the title Enchanter!")
```

In this example, we are simply checking whether the value of <b>spells is greater than 10</b>, this is our Boolean expression. If the expression is `True`, for instance, if spells has a value of 12, then the player will receive a message "You gained the title Enchanter!". However, nothing special happens when the condition is `False` and the program will skip the message display and proceed with the rest of the program.

2. Two branches

This is the example we have used before where if an expression is `True` then one code snippet will run, if `False` then an alternative snippet will run. Since there are two possible outcomes then we have two branches for which we can use an `if-else` statement.

Recall the example of deciding whether a player has unlocked a level:

```
if score > 500 and stars > 0:
   print("Congratulations, you unlocked a new level!")
else:
   print("Oh no. Seems like you are stuck. Better luck next time.")
```

For a player to go up a level he must have collected at least 1 star and gained over 500 points. The expression is made up of <b>two conditions</b> with an `and` in between. Both conditions need to be `True` for the player to see the good news on screen. In the event that the Boolean expression is `False` then the player needs to try again, so the program jumps to execute the `else` statement. 

3. More than two branches

When we have three or more possible outcomes, we need to use the `elif` command.

```
lives = 1
pellets = 36

if lives == 0:
   print("Game over!")
elif pellets == 50:
   print("Woo-hoo! Press Enter key to go to the next level.")
else:
   print("Watch out for those ghosts!")
```
In this program, we are imagining a game of Pac-Man. The player is initially given three lives and has to navigate a complex maze containing pellets that need to be eaten. Except, there are ghosts in the maze and if the player gets eaten by a ghost, a live is lost.

There is a hard rule that when all lives are lost the game ends. This is the first branch. Therefore, when the value of lives is equal to zero, the player sees "Game over!". But, in the chance that the player managed to eat all the pellets (and lives still remain) then the player is automatically passed to the next level. This is the second branch. If neither of these hard rules are `True` then the player is still trying to win the level, and so for encouragement the game prints out "Watch out for those ghosts!". This is the third branch.

You always must use an `elif` after an `if` and before an `else`.

## Playing With Loops 


