




def mod_m(m):
	def compute_modulo(n):
		return (n%m)
	return compute_modulo



def linear_probing(m=1009):
	def hf(key,attempt):
		return (hash(key) + attempt) % m
	return hf

def double_hashing(hf2,m=1009):
	def hf(key,attempt):
		return (hash(key) + attempt * hf2(key)) % m
	return hf


class DeletedEntry:
	pass

class DHT(object):
	def __init__(self, hash_function, m=1009):
		self.entries = [None for i range(m)]
		self.hash = hash_function
		self.deleted_entry = DeletedEntry()


	def __getitem__(self,key):
		entry = self.get_entry(key)
		if entry is None:
			raise KeyError(key)
		return entry[1]
	def __contains__(self,key):
		return self.get_entry(key) is not None

	def __setitem__(self,key,value):
		if value is None: raise 'Cannot store no value'
		del self[key]
		for attempt in xrange(len(self.entries)):
			h = self.hash(key,attemp)
			if self.entries[h] is None or \
				self.entries[h] is self.deleted_entry:
				self.entries[h] = (key,value)
				return
		raise 'Too many items already'