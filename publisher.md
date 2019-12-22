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
…
line 10
…
```


**The lines after lines 1, 3, and 5.**
```
…
line 2
…
line 4
…
line 6
…
```

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
```
…
line 8
line 9
line 10
…
line 22
line 23
line 24
…
```

**All lines after line 26.**
```
…
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
…
```

### Including line numbers
**The lines after line 7 up to, and including, line 10,**  
**and the lines after line 21 up to, and including, line 24.**
<div class="code">
<table><tbody>
<tr><td></td><td><pre  ><code >…</code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb2p-8" href="#cb2p-8" title="8">8</a></td><td><pre  ><code >line 8  </code></pre></td></tr>
<tr><td><a class="sourceLine" id="cb2p-9" href="#cb2p-9" title="9">9</a></td><td><pre  ><code >line 9  </code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb2p-10" href="#cb2p-10" title="10">10</a></td><td><pre  ><code >line 10</code></pre></td></tr>
<tr><td></td><td><pre  ><code >…</code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb2p-22" href="#cb2p-22" title="22">22</a></td><td><pre  ><code >line 22  </code></pre></td></tr>
<tr><td><a class="sourceLine" id="cb2p-23" href="#cb2p-23" title="23">23</a></td><td><pre  ><code >line 23  </code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb2p-24" href="#cb2p-24" title="24">24</a></td><td><pre  ><code >line 24  </code></pre></td></tr>
<tr><td></td><td><pre  ><code >…</code></pre></td></tr></tbody></table>
</div>

**All lines after line 26.**
<div class="code">
<table><tbody>
<tr><td></td><td><pre  ><code >…</code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb3p-27" href="#cb3p-27" title="27">27</a></td><td><pre  ><code >line 27  </code></pre></td></tr>
<tr><td><a class="sourceLine" id="cb3p-28" href="#cb3p-28" title="28">28</a></td><td><pre  ><code >line 28  </code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb3p-29" href="#cb3p-29" title="29">29</a></td><td><pre  ><code >line 29  </code></pre></td></tr>
<tr><td><a class="sourceLine" id="cb3p-30" href="#cb3p-30" title="30">30</a></td><td><pre  ><code >line 30</code></pre></td></tr></tbody></table>
</div>

**All lines before, and including, line 4.**
<div class="code">
<table><tbody>
<tr><td><a class="sourceLine" id="cb4p-1" href="#cb4p-1" title="1">1</a></td><td><pre  ><code >line 1  </code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb4p-2" href="#cb4p-2" title="2">2</a></td><td><pre  ><code >line 2  </code></pre></td></tr>
<tr><td><a class="sourceLine" id="cb4p-3" href="#cb4p-3" title="3">3</a></td><td><pre  ><code >line 3  </code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb4p-4" href="#cb4p-4" title="4">4</a></td><td><pre  ><code >line 4  </code></pre></td></tr>
<tr><td></td><td><pre  ><code >…</code></pre></td></tr></tbody></table>
</div>

**With syntax highlighting**
<div class="code">
<table><tbody>
<tr><td></td><td><pre  class="python"><code class="python">…</code></pre></td></tr>
<tr class="even"><td><a class="sourceLine" id="cb1p-3" href="#cb1p-3" title="3">3</a></td><td><pre  class="python"><code class="python"><span class="bu">print</span>(<span class="st">&#39;Python example&#39;</span>)</code></pre></td></tr></tbody></table>
</div>

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

# Chapter 1

Laboriosam laudantium vitae nobis id libero. Non laboriosam est animi sint provident voluptas aspernatur nihil. Exercitationem eius ad facere aliquid commodi impedit sit eaque. Voluptatem ut dignissimos et repellendus voluptas. Vel et repellat doloribus autem voluptas adipisci sit.

<!-- Take up all remaining space in this page and start the next section in a new page -->
<div class="full-page"></div>

# Appendix

Laboriosam laudantium vitae nobis id libero. Non laboriosam est animi sint provident voluptas aspernatur nihil. Exercitationem eius ad facere aliquid commodi impedit sit eaque. Voluptatem ut dignissimos et repellendus voluptas. Vel et repellat doloribus autem voluptas adipisci sit.

