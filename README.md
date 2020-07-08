# Cracking the Coding Interview
This repo is designed to help me prepare for upcoming coding interviews. In this repo, you will find ***my attempts*** to solving various interview questions. This repo is following the 6th edition of "Cracking the Coding Interview". Note that not every question will be solved. If you stumble across this repo, it might help you get an idea of some of the questions to expect in an interview. This repo is not a replacement for the book or any other medium of studying; it's simply an aid. It allows me to put my code in one place and allows me to access it wherever I go. For the small number of you who do come across this repo, feel free to fork it and add your own spin and don't hesitate to make a pull request if you think I made an error. Happy studying :)

Contents:
- [Big O](#big-o)

## Big O
In this section, we will be going over the additional Big O problems in the book and I will offer my explanation as to how I solved each question
### Problem 1
**The following code computes the product of *a* and *b*. What is the runtime?**
```python
def product(a, b):
    sum =  0
    for i in range(b):
        sum += a
    return sum
```
The runtime for this function will be *O(b)* since we add *a* to *sum* a total of *b* times. Since adding *a* to *sum* takes, constant time, the overall running tume is *O(b)*

### Problem 2
**The following code computes *a<sup>b</sup>*. What is its runtime**
```python
def power(a, b):
    if b < 0:
        return 0 # error
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1)
```
The runtime for this function will be *O(b)* since it subtracts 1 at each level.

### Problem 3
**The following code computes *a % b*. What is its runtime?**
```python
def mod(a, b):
    if b <= 0:
        return -1
    div = a / b
    return a - div * b
```
This function will take constant time, *O(1)*, since mathetmatic operations take constant time.
