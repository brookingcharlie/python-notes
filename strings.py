assert 'foo' == "foo", 'strings can use either single or double quotes'

single_quoted = 'foo\nbar'
double_quoted = "foo\nbar"
raw_string = r'foo\nbar'
triple_quoted = """foo
bar"""

assert single_quoted == double_quoted, 'escape characters work with single or double quotes'
assert single_quoted != raw_string, 'use raw strings when you don\'t want escape chars'
assert single_quoted == triple_quoted, 'use triple quotes for multi-line strings'
