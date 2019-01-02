 #!/usr/bin/python


# - Spammer Gblk:v

# | Description: I'm a handsome Boy :v

# | Author: Star Tamvan :v

# | Date: 02/01/2019

# | Disclaimer: belajar Dari Jalanan ga dari guru!!! 


import spammer_class

spammer = spammer_class.Spammer()

spammer.author = "Star Handsome :v "

try:

    spammer.main()

except KeyboardInterrupt:

    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC

    exit()




