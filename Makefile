##
## EPITECH PROJECT, 2021
## Math
## File description:
## Makefile
##

NAME 	=		205IQ

MAIN	=		src/main.py

MAIN_TEST = 	test/test_iq.py

all: $(MAIN)
		cp $(MAIN) $(NAME)
		chmod 755 $(NAME)

clean:
		rm -rf test/__pycache__
		rm -rf src/__pycache__

fclean: clean
		rm -f $(NAME)

test_run:
		python3 -m unittest test/test_iq.py

re: fclean all