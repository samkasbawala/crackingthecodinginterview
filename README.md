# Cracking the Coding Interview
This repo is designed to help me prepare for upcoming coding interviews. In this repo, you will find ***my attempts*** to solving various interview questions. This repo is following the 6th edition of "Cracking the Coding Interview". Note that not every question will be solved. If you stumble across this repo, it might help you get an idea of some of the questions to expect in an interview. This repo is not a replacement for the book or any other medium of studying; it's simply an aid. It allows me to put my code in one place and allows me to access it wherever I go. For the small number of you who do come across this repo, feel free to fork it and add your own spin and don't hesitate to make a pull request if you think I made an error. I highly recommend reading the questions below and trying them yourselves first before looking at my solutions. I know that there is already a github repo for the solutions for this book, but I thought making my own repo would help me learn better. Hope this helps! Happy studying :)

## Contents:
[Chapter 1: Arrays and Strings](#chapter-1-arrays-and-strings)
- [1.1 Is Unique](#11-is-unique)
- [1.2 Check Permutation](#12-check-permutation)
- [1.3 URLify](#13-urlify)
- [1.4 Palindrome Permutation](#14-palindrome-permutation)
- [1.5 One Away](#15-one-away)
- [1.6 String Compression](#16-string-compression)
- [1.7 Rotate Matrix](#17-rotate-matrix)
- [1.8 Zero Matrix](#18-zero-matrix)
- [1.9 String Rotation](#19-string-rotation)

[Chapter 2: Linked Lists](#chapter-2-linked-lists)
- [2.1 Remove Dups](#21-remove-dups)
- [2.2 Return Kth to Last](#22-return-kth-to-last)
- [2.3 Delete Middle Node](#23-delete-middle-node)
- [2.5 Sum Lists](#25-sum-lists)
- [2.6 Palindrome](#26-palindrome)
- [2.7 Intersection](#27-intersection)
- [2.8 Loop Detection](#28-loop-detection)

[Chapter 3: Stacks and Queues](#chapter-3-stacks-and-queues)
- [3.1 Three in One](#31-three-in-one)
- [3.2 Stack Min](#32-stack-min)
- [3.3 Stack of Plates](#33-stack-of-plates)
- [3.4 Queue via Stacks](#34-queue-via-stacks)
- [3.5 Sort Stack](#35-sort-stack)
- [3.6 Animal Shelter](#36-animal-shelter)

[Chapter 4: Trees and Graphs](#chapter-4-trees-and-graphs)
- [4.1 Route Between Nodes](#41-route-between-nodes)
- [4.2 Minimal Tree](#42-minimal-tree)

## Chapter 1: Arrays and Strings
In this chapter we will go over some interview questions regarding arrays and strings. Again, these questions are from the 6th edition of "Cracking the Coding Interview". In this chapter, each of the questions will be listed. You can find my code to each question in the subsequent chapter folders. Each question will have it's own python file.

### 1.1 Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

### 1.2 Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.

### 1.3 URLify
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and the you are given the "true" length of the string.

**EXAMPLE**\
Input:  'Mr John Smith    ', 13\
Output: 'Mr%20John%20Smith'

### 1.4 Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome. You can ignore casing and non-letter characters.

**EXAMPLE**\
Input: Tact Coa\
Output: True (permutations: 'taco cat', 'atco cta', etc.)

### 1.5 One Away
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

**EXAMPLE**\
pale, ple -> True\
pale, pales -> True\
pale, bale -> True\
pale, bake -> False

### 1.6 String Compression
Implement a method to perform basic string compression using the counts od repeated characters. For example the string *aabcccccaaa* would become *a2b1c5a3*. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the sting only has upper case and lowercase letters.

### 1.7 Rotate Matrix
Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

### 1.8 Zero Matrix
Write an algorithm such that if an element in an M x N matrix is 0, its entire row or column is set to 0

### 1.9 String Rotation
Assume you have a method `isSubstring` which checks if one word is a substring of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a rotation of `s1` using only one call to `isSubstring` (e.g. "waterbottle" is a rotation if "erbottlewat")

## Chapter 2: Linked Lists
In this chapter we will go over some interview questions regarding linked lists. Again, these questions are from the 6th edition of "Cracking the Coding Interview". In this chapter, each of the questions will be listed. You can find my code to each question in the subsequent chapter folders. Each question will have it's own python file.

### 2.1 Remove Dups
Write code to remove duplicates from an unsorted linked list

### 2.2 Return Kth to Last
Implement an algorithm to find the kth to last element of a singly linked list

### 2.3 Delete Middle Node
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

### 2.5 Sum Lists
You have two numbers represented by a linked list, where each mode contains a single digit. The digits are stored in *reverse* order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

### 2.6 Palindrome
Implement a function to check if a linked list is a palindrome

### 2.7 Intersection
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the *k*th node of the first linked list is the exact same node (by reference) as the *j*th node of the second linked list, then they are intersecting

### 2.8 Loop Detection
Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop

## Chapter 3: Stacks and Queues
In this chapter, we will go over some interview questions regarding stacks and queues. Again, these questions are from the 6th edition of "Cracking the Coding Interview". In this chapter, each of the questions will be listed. You can find my code to each question in the subsequent chapter folders. Each question will have it's own python file.

### 3.1 Three in One
Describe how you could use a single array to implement three stacks.

### 3.2 Stack Min
How would you design a stack which, in addition to `push` and `pop`, has a function `min` which returns the minimum element? `push`, `pop`, and `min` should all operate in O(1) time

### 3.3 Stack of Plates
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure `SetOfStacks` that mimics this. `SetOfStacks` should be composed of several stacks and should create new stack once the previous one exceeds capacity. `SetOfStacks.pop()` and `SetOfStacks.push()` should behave identically to a single stack. 

### 3.4 Queue via Stacks
Implement a `MyQueue` class which implements a queue using two stacks

### 3.5 Sort Stack
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you may not copy the elements into any other data structure. The stack supports the following operations, `push`, `pop`, `peek`, and `isEmpty`

### 3.6 Animal Shelter
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as `enqueue`, `dequeueAny`, `dequeueDog`, and `dequeueCat`.

## Chapter 4: Trees and Graphs
In this chapter, we will go over some interview questions regarding trees and graphs. Again, these questions are from the 6th edition of "Cracking the Coding Interview". In this chapter, each of the questions will be listed. You can find my code to each question in the subsequent chapter folders. Each question will have it's own python file.

### 4.1 Route Between Nodes
Given a directed graph and two nodes, `S` and `E`, design an algorithm to find out whether there is a route from `S` to `E`

### 4.2 Minimal Tree
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height