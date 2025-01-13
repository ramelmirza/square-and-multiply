# Square and Multiply Algorithm

This program was created for my former math teacher where a big component of the course was revolving around number theory.
It is intended to be used as a study guide to aid the discrete math & stats students with studying.
Simply input the base, exponent, and modulo, and the program will compute the number it's congruent to in it's non-zero form.
There are many ways to compute this program in terms of time complexity. However, as time goes on and I get more exposed to
mathematics, I will keep coming back to this on a later date in order to find the fastest algorithm that I can build during said time.

___

<br>
$193^{53} \mod 673$
<br>

$193^{53} \is obviously way too big of a number to compute so certain steps are taken to reduce this number in it's lowest form (non-zero) with respect to its modulus.

<br>

This is done in 3 steps:
<br>
  [1]: Converting the exponent, which is in decimal form, to its binary equivalent. <br>
  [2]: Marking out which numbers are needed in product, i.e. 2^5 (32), 2^4 (16), 2^2 (4), 2^1 (2) and completing their squares (numbers in their lowest form of congruency)
  [3]: Product the numbers and divide by modulo to get the final answer 
