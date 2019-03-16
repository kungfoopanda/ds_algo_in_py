# ds_algo_in_py
Book DS and Algo in Python

### Variables
* Each *identifier* is implicitly associated with the **memory address** of the object to which it refers.
* The *identifier* has no declared type, the object to which it refers has a definite type.

|Class|Immutable|
|----| ----|
|bool| Y|
|int|Y|
|float|Y|
|tuple|Y|
|str|Y|
|frozenset|Y|
|----|----|
|set|N|
|list|N|
|dict|N|

* A list is a **referential** structure, as it stores a sequence of **references**.
* Only instances of **immutable** types cane be added to a Python set.

|Equality operator|Meaning|Example|
|---|---|---|
|is|same identity|Identifiers *a* and *b* are alias to the same object|
|is not|different identity|
|==|equivalent|*a == b* is even **True** when the identifiers refer to different objects which have same data-types and values|
|!=|not equivalent|

### Operator Precedence
|No.|Type|Symbols|
|----|----|----|
|1|member access|expr.member|
|2|function/method call<br>container subscripts/slices|expr(...)<br>expr[...]|
|3|exponentiation|**|
|4|unary operators|+expr, -expr, ~expr|
|5|multiplication, division|*, /, //, %|
|6|addition, subtraction|+, -|
|7|bitwise shifting|<<, >>|
|8|bitwise-and|&|
|9|bitwise-xor|^|
|10|bitwise-or|&#124;|
|11|comparisons<br>containment|**is, is not**, ==, !=, <, <=, >, >=<br>**in, not in**|
|12|logical-not|**not** expr|
|13|logical-and|**and**|
|14|logical-or|**or**|
|15|conditional|val1 **if** cond **else** val2|
|16|assigment|=, +=, -=, *=, etc.|

### Functions
The default value is evaluated only once. <br>This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
 
### Simple IO
* The separator in *print* function can be customised using sep = '' argument.
<br><code>print(a, b, c, sep=':')<br>>>a:b:c</code><br>
* An alternative trailing string can be designated using argument *end=''*.
* Output can be directed to a file by indicating an output file stream *file=fp*.

##### File Object
|Methods|Explanation|
|---|---|
|open()|returns a file object|
|f.read(size)|at most size bytes are read|
|f.readline()|reads a single line from the file|
|f.readlines()|reads all the lines of a file in a list|
|f.write(string)|writes the contents of string to the file, returning the number of characters written.|
|f.tell()|returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.|
|f.seek(offset, from_what)|To change the file object’s position, position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.|
