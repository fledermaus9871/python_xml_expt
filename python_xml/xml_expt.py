from lxml import etree

test = '''
<layers>
	<layer>
		<name>Turtle Duck</name>
	</layer>
	<style>
		<name>Winged Lemur</name>
	</style>
</layers>
'''

def parse_xml(xml_str):
	
	xml_root = etree.XML(xml_str)
	
	return xml_root
	
def create_avatar_xml(pro_list, ant_list, creature_list):
	
	avatar = etree.Element('avatar')
	characters = etree.SubElement(avatar, 'characters')
	protagonists = etree.SubElement(characters, 'protagonists')
	antagonists = etree.SubElement(characters, 'antagonists')
	creatures = etree.SubElement(avatar, 'creatures')
	
	for prot in pro_list:
		protagonist = etree.SubElement(protagonists, 'protagonist')
		protagonist.text = prot
		
	for ant in ant_list:
		antagonist = etree.SubElement(antagonists, 'antagonist')
		antagonist.text = ant
		
	for animal in creature_list:
		creature = etree.SubElement(creatures, 'creature')
		creature.text = animal
		
	return avatar


if __name__ == '__main__':
	
	from lxml import etree
	
	p_list = ['Aang', 'Katara', 'Toph', 'Sokka', 'Momo', 'Appa']
	a_list = ['Azula', 'Zuko', 'Ozai', 'Sparky sparky boom man']
	c_list = ['Winged lemur', 'Air bison', 'Turtle duck', 'Sabertooth moose lion']
	
	avatar_xml = create_avatar_xml(p_list, a_list, c_list)
	
	print "Here's the pretty xml:"
	print etree.tostring(avatar_xml, pretty_print=True)
	
	a_xml = etree.tostring(avatar_xml)
	
	print "Here's the vanilla xml:"
	print a_xml
	
	print "Let's add a new creature."
	root = etree.XML(a_xml)
	creatures = root.find('creatures')
	new_creature = etree.SubElement(creatures, 'creature')
	new_creature.text = 'Cat owl'
	
	print 'Here are the results:'
	print etree.tostring(root, pretty_print=True)
	
	print "Now let's replace Zuko with Sozin."
	
	zuko_path = root.xpath('/avatar/characters/antagonists/antagonist[text()="Zuko"]')
	
	# zuko_path = root.xpath('.//antagonist[text()="Zuko"]'); this also works
	
	print "Let's see what xpath returned:"
	print etree.tostring(zuko_path[0], pretty_print=True)
	
	zuko_path[0].text = 'Sozin'
	
	print "Let's see if that replace worked:"
	print etree.tostring(root, pretty_print=True)
	
	creature_paths = root.xpath('/avatar/creatures')
	
	print "Let's get all creatures using xpath." 
	print etree.tostring(creature_paths[0], pretty_print=True)
	
	
	print "Let's add the 'Lion turtle'."
	lion_turtle = etree.SubElement(creature_paths[0], 'creature')
	lion_turtle.text = 'Lion turtle'
	print etree.tostring(root, pretty_print=True)
	
	print "Here's the original xml:"
	print etree.tostring(avatar_xml, pretty_print=True)

