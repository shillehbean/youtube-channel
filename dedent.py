#needed to use dedent
import textwrap

def test_textwrap(user_properties):

    print('### No indent in code and no dedent ###')

    output_string_one = """\
Hello my name is {name}
I am a {job}
My favorite color is {color}
    """.format(**user_properties)
    print(output_string_one) 

    ##################################################
    print('### With indent in code and no dedent ###')

    output_string_two = """\
    Hello my name is {name}
    I am a {job}
    My favorite color is {color}
    """.format(**user_properties)

    print(output_string_two)

    ##################################################
    print('### With indent in code and using dedent ###')

    print(textwrap.dedent(output_string_two)) 

       
user_properties = {'name': "Mahmood Shilleh", 'job': "Software Engineer", 'color': "Green"}
test_textwrap(user_properties)
