##
## EPITECH PROJECT, 2021
## Math
## File description:
## Makefile
##

NAME 	=		201yams

MAIN	=		src/yam.py

MAIN_TEST =		test/test.py

all: $(MAIN)
		cp $(MAIN) $(NAME)
		chmod 755 $(NAME)

clean:
		rm -f $(NAME)

fclean: 
		rm -rf */__pycache__
		rm -f $(NAME)

unitTest:
		python3 -m unittest test/test_yams.py

re: fclean all