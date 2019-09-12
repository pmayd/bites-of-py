# Bite 22. Write a decorator with argument

Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:

```python
@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
````

- would return: <p><strong>I code with PyBites</strong></p>

Have fun and start to grok decorators!
