#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given three positive integers, k, m, n, representing a population 
containing k+m+n individuals, where k = homozygous dominant, m = heterozygous,
and n = homozygous recessive. Returns the probability that any two 
mating individuals will display the probability of two randomly selected
organisms will produce an offspring with a dominant allele (and by default
the dominant phenotype).
Created on Tue Jun  9 14:32:36 2020

@author: bram
"""

# function for the dominant probability
def Dom(k: int, m: int, n: int) -> float:
    """
    given three integers for pop with k, n, m number of individuals 
    returns the probability of two random individuals producing an 
    offsring with the dominant allele
    ""
    