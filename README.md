# itertools_product_bigData
Python 3 - Itertools Cartesian Product For Big Data.

A set of two tools for working with big data, and Cartesian Product.

Allow extraction of (n)th product from any record set size, without compiling entire record set to memory first.

Consistent speed of execution regardless of set sizes. Can process millions, and billions of permutations with a constant speed.

## specific_product(sets, n):
```
Extract single permutation of Cartesian product iteration in an consistent speed regardless of list/set sizes.

:arg sets: The same arg used for itertools.product, iterates.
:arg n: Integer of the specific permutation of the product you want to extract.

This is better then the current itertools generator/yield when dealing with massive amounts of sets/permutations.
```
## total_product(*args)
```
Calculate total permutations of a Cartesian product

:args args is the iterates that would of eventually been passed to more_itertools.specific_product()

Used to get an integer of for iteration over with specific Cartesian product
```