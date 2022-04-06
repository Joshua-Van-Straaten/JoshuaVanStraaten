# JoshuaVanStraaten
Corigine Technical Assessment

**The program calculates the sum of any parsed factorial's digits.**
- First, the factorial of the number is found using numpy
- Thereafter, a while loop iterates through each digit of the factorial and adds it to the previous digit. The sum is stored in "sum_of_digits"

**The packages used are:**
- Numpy
- Argparse

**Docker build and run:**
- The docker image is built using:
docker build -t factorial-digits .

- The image is run using:
docker run --rm factorial-digits [number input]
