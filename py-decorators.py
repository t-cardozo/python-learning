
def cough_dec(func):

    def func_wrapper():
        print('Cough Cough..')
        func()
        print('Cough Cough..')
    return func_wrapper



@cough_dec
def question():
    print('can you give me a discount on that?')

question()