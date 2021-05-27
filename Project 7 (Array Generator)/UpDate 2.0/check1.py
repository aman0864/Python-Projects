from pynput.keyboard import Listener


def k():
    def key_detector():
        """This function gives you the information about the key pressed by you and goes to the function named 
    what_to_do_with_the_key_we_get()
    and it also includes an variable key so now the function becames
    what_to_do_with_the_key_we_get(key)
    key is the name of the key pressed by you and in 
    what_to_do_with_the_key_we_get(key) 
    function you can write that what you want to do with that ke i.e. to store it in a file, to print or anything of your choice
    For Example:
    def what_to_do_with_the_key_we_get(key):
        print(key)
    this example will print key pressed by you
        """
        with Listener(on_press=what_to_do_with_the_key_we_get) as l:
            l.join()

    def what_to_do_with_the_key_we_get(key):
        return key

    key_detector()
    return key


k()
print(key+Aman)
