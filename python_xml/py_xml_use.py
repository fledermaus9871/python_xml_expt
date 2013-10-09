from xml_expt import *

p_list = ['Aang', 'Katara', 'Toph', 'Sokka', 'Momo', 'Appa']
a_list = ['Azula', 'Zuko', 'Ozai', 'Sparky sparky boom man']
c_list = ['Winged Lemur', 'Air Bison', 'Turtleduck', 'Sabertooth Mooselion']

avatar_xml = create_avatar_xml(pro_list=p_list, ant_list=a_list, creature_list=c_list)

xml_str = etree.tostring(avatar_xml, pretty_print=True)

print "Here's the original xml:\n"
print xml_str

root = etree.XML(xml_str)

print root

print "Here's the root tag:"
print root.tag

print "Now to find a subelement of interest."

creatures = root.find('creatures')
print "Here's the 'creatures' element:"
print creatures
creature = creatures.find('creature')
print "Here's the 'creature' element:"
print creature

print "Let's add a new creature."

new_creature = etree.SubElement(creatures, 'creature')
new_creature.text = 'Armadillobear'

new_xml = etree.tostring(root, pretty_print=True)
print new_xml
