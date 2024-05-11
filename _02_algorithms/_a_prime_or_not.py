"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    num = simpledialog.askinteger(title="Prime or not", prompt="Enter a number...")
    for i in range(2, num, 1):
        if num % i == 0:
            messagebox.showinfo(title="Not prime", message="" + str(num) + " is not prime! The lowest common factor it is divisible by is " + str(i))
            break
        elif i == num - 1:
            messagebox.showinfo(title="Prime", message="" + str(num) + " is prime!")
            break
    pass
