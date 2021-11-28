# Beautiful-Liar
## Detects the most false-witnesses integers in a range.

The inspiration for this project: https://www.youtube.com/watch?v=_MscGSN5J6o

### Result:

55,648 (fifty-five thousand, six-hundred fourty-eight) is the 50,000th composite number. (source: http://www.naturalnumbers.org/composites.html)
I ran the script for each number between 2 to 55,648. Runtime: ~27 minutes on my machine.
The numbers which turned up to be false-witnesses the most times were:

(The number, how many times found lying)

(2401, 183)

(625, 182)

(6561, 173)

(529, 166)

(81, 164)

(729, 152)

(4096, 149)

(4225, 126)

(3481, 125)

(256, 123)

Nice to see that these biggest liars are all (almost) powers of primes:

2401  =7  ^ 4

625   =5  ^ 4

6561  =3  ^ 8

529   =23 ^ 2

81    =3  ^ 4

729   =3  ^ 6

4096  =2  ^ 12

4225  =65 ^ 2 <= 65 isn't a prime!

3481  =59 ^ 2

256   =2  ^ 8
