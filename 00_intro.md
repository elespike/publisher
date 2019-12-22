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
<+[scripts/example.sh]+>
```

### example.py
```python
<+[scripts/example.py]+>
```

### Including specific lines from files
**The line after line 9.**
```
<+[example.md|9]+>
```


**The lines after lines 1, 3, and 5.**
```
<+[example.md|1,3,5]+>
```

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
```
<+[example.md|7:10,21:24]+>
```

**All lines after line 26.**
```
<+[example.md|26:]+>
```

**All lines before, and including, line 4.**
```
<+[example.md|:4]+>
```

### Including line numbers
**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
<+[example.md|#,7:10,21:24]+>

**All lines after line 26.**
<+[example.md|#,26:]+>

**All lines before, and including, line 4.**
<+[example.md|#,:4]+>

**With syntax highlighting**
<+[scripts/example.py|#python,2:]+>

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

