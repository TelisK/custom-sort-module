# Custom Sorting Module

A Python module made for Level 2 Python Language lesson, at University of Crete.

## Description

The idea is to make a module that will sort all values at the form: 
```python
['0', '1', '2', 'Add', 'addition', 'by', 'Bye', 'αυγό', 'Αυτός', 'Βάτραχος', 'βατράχι'] (the last words are greek)
```
The normal way, .sort() or sorted() produces this result: 
```python
['0', '1', '2', 'Add', 'Bye', 'addition', 'by', 'Αυτός', 'Βάτραχος', 'αυγό', 'βατράχι']
```
The module has two optional parameters, capitalize and original. At default both are false.
At default option, the module turns everything to lowercase letters, so it runs faster.
The same when capitalized = True.

When we choose original = True (capitalize can be True or False. The result will be the same) the module returns the original inserted values sorted. This option is slower, as it uses for loops.

## Details

This module works with: lists, tuples, sets and strings.

The values of lists, tuples and sets must be strings.

The output row is: numbers, english, greek




