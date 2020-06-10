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

import sys

# Function for determining offspring with dominant alleles 
def Dom(k: int, m: int, n: int) -> float:
    """
    given three integers for pop with k, n, m number of individuals 
    returns the probability of two random individuals producing an 
    offsring with the dominant allele
    """
    # Total population size
    total = k + m + n
    
    # Given two alleles (ie. Aa) from each parent there are 9 possible 
    # combinations that lead to three outcomes, AA, Aa, and aa
    # Calculating the probability of each. Add all that lead to dominant 
    # allele expression (ie. Having one or more dominant allele)
    AA_AA = (k / total) * ((k - 1) / (total - 1))
    AA_Aa = (k / total) * (m / (total - 1))
    AA_aa = (k / total) * (n / (total - 1))
    Aa_AA = (m / total) * (k / (total - 1))
    Aa_Aa = (m / total) * ((m - 1) / (total - 1))
    Aa_aa = (m / total) * (n / (total - 1))
    aa_AA = (n / total) * (k / (total - 1))
    aa_Aa = (n / total) * (m / (total - 1))
    aa_aa = (n / total) * ((n - 1) / (total - 1))
    
    # Calculate overall probability of having offspring with dominant allele
    return AA_AA + AA_Aa + AA_aa + Aa_AA + (0.75 * Aa_Aa) + (0.5 * Aa_aa) + aa_AA + (0.5 * aa_Aa)
    
# Assign command line arguments to variables 
k, m, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

# Determine the probability of having Offspring with dominant allele given population of k, m, n individuals 
probDom = Dom(k, m, n)
print(f"Probability of two randomly selected individuals producing an offspring with dominant allele: {probDom}")
