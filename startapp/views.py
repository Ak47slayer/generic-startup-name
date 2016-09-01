from django.shortcuts import render
import random
import re


# Create your views here.
def index(request):
	first_word = [
	404, 411,
	'cookies', 'cryptic',
	'defrag', 'delete',
	'downtime', 'eyecandy',
	'hotspot', 'legacy',
	'deepdive', 'cached',
	'morph', 'multitask',
	'mcLuhanism', 'navigate',
	'ping', 'pluggedin',
	'rant', 'shelfware',
	'unplugged', 'yoyomode',
	'radar', 'pixel',
	'techno', 'script',
	'venture', 'weasel'
	]

	second_word = [
	'dust', 'ground',
	'save', 'bot',
	'bomb', 'state',
	'fusion', 'mecca',
	'verse','leap',
	'giant', 'matrix',
	'merchant', 'agent'
	'sense', 'tropical',
	'paradigm', 'doers',
	'value', 'deck',
	'dime', 'outrage',
	'permalink', 'bender',
	'parade', 'wallet',
	'market', 'glass',
	'ransomware', 'kiddies',
	'smoke', 'fire',
	'junkie', 'squatting',
	'portal', 'capitalist',
	'jam', 'hippie']

	name = '%s %s' %(random.choice(first_word), random.choice(second_word))
	
	regexp = r"(\w)\1{2,}"
	startup_name = re.sub(regexp, repl, name)
	startup_gen_name = len(first_word) * len(second_word)

	context = {
	'name': startup_name,
	'startup_gen_name': startup_gen_name

		}

	return render(request, "startapp/index.html", context)

def repl(m):
 	return m.group()[:2]