# Cracking the Coding Interview
This repo is designed to help me prepare for upcoming coding interviews. In this repo, you will find ***my attempts*** to solving various interview questions. This repo is following the 6th edition of "Cracking the Coding Interview". Note that not every question will be solved. If you stumble across this repo, it might help you get an idea of some of the questions to expect in an interview. This repo is not a replacement for the book or any other medium of studying; it's simply an aid. It allows me to put my code in one place and allows me to access it wherever I go. For the small number of you who do come across this repo, feel free to fork it and add your own spin and don't hesitate to make a pull request if you think I made an error. I highly reccommend reading the questions below and trying them yourselves first before looking at my solutions. I know that there is already a github repo for the solutions for this book, but I thought making my own repo would help me learn better. Hope this helps! Happy studying :)

## Contents:
[Chapter 1: Arrays and Strings](#chapter-1-arrays-and-strings)
- [1.1: Is Unique](#11-is-unique)
- [1.2: Check Permutation](#12-check-permutation)
- [1.3: URLify](#13-urlify)
- [1.4: Palindrome Permutation](#14-palindrome-permutation)
- [1.5: One Away](#15-one-away)
- [1.6: String Compression](#16-string-compression)
- [1.7: Rotate Matrix](#17-rotate-matrix)
- [1.8: Zero Matrix](#18-zero-matrix)
- [1.9: String Rotation](#19-string-rotation)

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
Output: True (permuattions: 'taco cat', 'atco cta', etc.)

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
Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the imaage by 90 degrees. Can you do this in place?

### 1.8 Zero Matrix
Write an algorithm such that if an element in an M x N matrix is 0, its entire row or column is set to 0

### 1.9 String Rotation
Assume you have a method `isSubstring` which checks if one word is a substring of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a rotation of `s1` using only one call to `isSubstring` (e.g. "waterbottle" is a rotation if "erbottlewat")