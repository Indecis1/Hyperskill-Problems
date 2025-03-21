# Naïves Bayes Classifier

## Problem description

We have 1 corpus that has 3 texts in 3 languages (English, French, Norwegian).
Our goal is given a n-gram predict the language of that n-gram.
It is a classification Task. We should resolve this problem using a Naïves Bayes Classifier

## Formalisation of the problem

Given that we use a Naïves Bayes classifier, we have this:
$$ P\left(class_i\;\middle|\omega_1\omega_2...\omega_n\right) = \frac{P\left(\omega_1\omega_2...\omega_n\;\middle|class_i\right) P\left(class_i\right)}{P\left(\omega_1\omega_2...\omega_n\right)} $$
Where $class_i$ is the one of the class to predict. In our case $class_i$ represent
a language.

For our problem $P\left(class_i\right)$ and $P\left(\omega_1\omega_2...\omega_n\right)$ are equal for all the 3 languages
so we will drop them. Our output will be $class = \underset{i}{\arg\max} \: P\left(class_i\;\middle|\omega_1\omega_2...\omega_n\right) = \underset{i}{\arg\max} \: P\left(\omega_1\omega_2...\omega_n\;\middle|class_i\right)$
Given that we are working with Naïve Bayes our assumption is that all the features are independant, so we can rewrite our equation as 
$$P\left(\omega_1\omega_2...\omega_n\;\middle|class_i\right) = P\left(\omega_1\;\middle|class_i\right) \times P\left(\omega_2\;\middle|class_i\right) \times ... \times P\left(\omega_n\;\middle|class_i\right)$$
Then
$$class = \underset{i}{\arg\max} \: P\left(class_i\;\middle|\omega_1\omega_2...\omega_n\right) = \underset{i}{\arg\max} \: P\left(\omega_1\;\middle|class_i\right) \times P\left(\omega_2\;\middle|class_i\right) \times ... \times P\left(\omega_n\;\middle|class_i\right) $$

There is a problem in this formula: it is if we are given a word that isn't in training dataset we will 
have a $P\left(\omega_i\;\middle|class_i\right) = 0$ that will set the probability to 0. To avoid that there
exists smoothing technique. We decide to implement a simple one Laplace Smoothing.


## Preprocessing

For our problem we decide strip the punctuation as they don't provide much information. We also normalise the text. 
All the texts are convert in lowercase.


## Output

Our output is for each n-gram the language (the class) predicted with the probability (don't forget we only compute $P\left(\omega_1\omega_2...\omega_n\;\middle|class_i\right)$).
If there are multiple predicted languages (they have the same probability), we will output all of them and are then end their probability.
The probability is given in first a non-reduce fraction then in a reduce one. the denormalized form can be used to check the inner computation.
