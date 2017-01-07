import xml.sax
import asyncio
from cothread import threaded

class EventHandler(xml.sax.ContentHandler):
	def __init__(self, target):
		self.target = target
		self.target.send(None)

	def startElement(self, name, attrs):
		self.target.send(('start', (name, attrs._attrs)))

	def characters(self, text):
		self.target.send(('text', text))

	def endElement(self, name):
		self.target.send(('end', name))


@asyncio.coroutine
def buses_to_dicts(target):
	target.send(None)
	while True:
		event, value = (yield)
		if event == 'start' and value[0] == 'bus':
			busdict ={}
			fragments = []
			while True:
				event, value = (yield)
				if event == 'start':
					fragments = []
				elif event == 'text':
					fragments.append(value)
				elif event == 'end':
					if value != 'bus':
						busdict[value] = "".join(fragments)
					else :
						target.send(busdict)
						break

@asyncio.coroutine
def filter_on_field(fieldname, value, target):
	while True:
		d = (yield)
		if d.get(fieldname) == value:
			target.send(d)
b


@asyncio.coroutine
def bus_locations():
	while True:
		bus = (yield)
		print (bus)


xml.sax.parse('some.xml', EventHandler(buses_to_dicts(  threaded(bus_locations())   )))
















