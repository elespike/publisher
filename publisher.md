# Introduction

## Highlight examples

**Plaintext**
```
Pre-formatted plaintext.
```

**Bash**
```bash
echo "Pre-formatted inline bash script." && exit 0
```

**Python**
```python
if print('Pre-formatted inline {} script.'.format('python')):
    return
```

### Highlighting specific words
To highlight specific words, use `<span class="hl">text</span>`, as such:  
Let's <span class="hl">highlight</span> the word <span class="hl">highlight</span>.

<pre><code>It can even be made to work within <span class="hl">pre-formatted</span> blocks!</code></pre>
As well as <code>inline <span class="hl">pre-formatted</span> fields</code>!

### Notes, warnings

<div class="nb">
**Please Note**: this is some <span class="hl">important</span> stuff!
</div>

## Using anchors

These are local hyperlinks to the examples found under [Including file contents](#including-file-contents):

- [example.sh](#example.sh)
- [example.py](#example.py)

## Creating tables

| Header 1 | Header 2                           |
|----------|------------------------------------|
| some     | stuff                              |
| more     | <span class="hl">highlights</span> |

---

| Header 1 | Header 2 | Header 3 |
|:---------|:--------:|---------:|
| left     | center   | right    |

## Including images

![Handwriting](static/img/lorem.jpg)
_Handwriting_, by Andrew Allingham, sourced from [https://www.flickr.com/photos/aallingh/8197626825](https://www.flickr.com/photos/aallingh/8197626825) and shared under [CC-BY](https://creativecommons.org/licenses/by/2.0/).

## Including file contents

### example.sh
```bash
#! /bin/bash

echo "Shell script example"
exit 0
```

### example.py
```python
#! /usr/bin/python3

print('Python example')
```

### Including specific lines from files
**The line after line 9.**
```
...
line 10
...
```


**The lines after lines 1, 3, and 5.**
```
...
line 2
...
line 4
...
line 6
...
```

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
```
...
line 8
line 9
line 10
...
line 22
line 23
line 24
...
```

**All lines after line 26.**
```
...
line 27
line 28
line 29
line 30
```

**All lines before, and including, line 4.**
```
line 1
line 2
line 3
line 4
...
```

### Including line numbers
**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
<div class="code">

------------------------------ ---
                               ...
     <span class="ln">8</span> line 8
     <span class="ln">9</span> line 9
    <span class="ln">10</span> line 10
                               ...
    <span class="ln">22</span> line 22
    <span class="ln">23</span> line 23
    <span class="ln">24</span> line 24
                               ...
------------------------------ ---

</div>

**All lines after line 26.**
<div class="code">

------------------------------ ---
                               ...
    <span class="ln">27</span> line 27
    <span class="ln">28</span> line 28
    <span class="ln">29</span> line 29
    <span class="ln">30</span> line 30
    <span class="ln">31</span> 
------------------------------ ---

</div>

**All lines before, and including, line 4.**
<div class="code">

------------------------------ ---
     <span class="ln">1</span> line 1
     <span class="ln">2</span> line 2
     <span class="ln">3</span> line 3
     <span class="ln">4</span> line 4
                               ...
------------------------------ ---

</div>

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

# Chapter 1

Laboriosam laudantium vitae nobis id libero. Non laboriosam est animi sint provident voluptas aspernatur nihil. Exercitationem eius ad facere aliquid commodi impedit sit eaque. Voluptatem ut dignissimos et repellendus voluptas. Vel et repellat doloribus autem voluptas adipisci sit.

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

# Appendix

Laboriosam laudantium vitae nobis id libero. Non laboriosam est animi sint provident voluptas aspernatur nihil. Exercitationem eius ad facere aliquid commodi impedit sit eaque. Voluptatem ut dignissimos et repellendus voluptas. Vel et repellat doloribus autem voluptas adipisci sit.

