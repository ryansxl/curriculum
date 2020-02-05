"""
Test Case 3
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: Trying to show already visible cells - should have no effect - then instant loss
SIZE = 10, MINES = 10, random.seed(5)
"""

"""
Test Case 4 - Results
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 54
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXX1XXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 78
Mines: 10
  0123456789
0   1XXXXXXX 0
1  12XXXXXXX 1
2  2XXXXXXXX 2
3  2XXXXXXXX 3
4  1X211XXXX 4
5  1X1 1111X 5
6  1X1    2X 6
7  111    2X 7
8         11 8
9            9
  0123456789
Enter your move (for help enter "H"): 99
Mines: 10
  0123456789
0   1XXXXXXX 0
1  12XXXXXXX 1
2  2XXXXXXXX 2
3  2XXXXXXXX 3
4  1X211XXXX 4
5  1X1 1111X 5
6  1X1    2X 6
7  111    2X 7
8         11 8
9            9
  0123456789
Enter your move (for help enter "H"): 67
Mines: 10
  0123456789
0   1XXXXXXX 0
1  12XXXXXXX 1
2  2XXXXXXXX 2
3  2XXXXXXXX 3
4  1X211XXXX 4
5  1X1 1111X 5
6  1X1    2X 6
7  111    2X 7
8         11 8
9            9
  0123456789
Enter your move (for help enter "H"): 54
Mines: 10
  0123456789
0   1XXXXXXX 0
1  12XXXXXXX 1
2  2XXXXXXXX 2
3  2XXXXXXXX 3
4  1X211XXXX 4
5  1X1 1111X 5
6  1X1    2X 6
7  111    2X 7
8         11 8
9            9
  0123456789
Enter your move (for help enter "H"): 64
Mines: 10
  0123456789
0   1XXXXXXX 0
1  12XXXXX1X 1
2  2XXXXXXXX 2
3  2XXXXXXXX 3
4  1X211MXXX 4
5  1X1 1111X 5
6  1X1    2X 6
7  111    2X 7
8         11 8
9            9
  0123456789
Uh oh! You blew up!
"""
